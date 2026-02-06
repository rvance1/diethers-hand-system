from datetime import date
from poplib import CR
import polars as pl
import wrds
from tqdm import tqdm

from core.config import settings

from src.model.schema.table_schema import CRSPMonthlySchema, CRSPMonthlyDF

crsp_schema = {
    "date": pl.Date,
    "permno": pl.Int64,
    "cusip": pl.String,
    "ret": pl.Float64,
    "retx": pl.Float64,
    "prc": pl.Float64,
    "vol": pl.Int64,
    "openprc": pl.Float64,
    "askhi": pl.Float64,
    "bidlo": pl.Float64,
    "shrout": pl.Int64,
    "ticker": pl.String,
    "shrcd": pl.Int64,
    "exchcd": pl.Int64,
}

class CRSPService:
    def __init__(self):
        self.user = settings.wrds_username
        self.wrds_db = wrds.Connection(wrds_username=self.user)


    def fetch_crsp_monthly_df(self, start_date: date, end_date: date) -> CRSPMonthlyDF:

        df = self.wrds_db.raw_sql(
            f"""
            SELECT
                date,
                permno,
                cusip,
                ret,
                retx,
                prc,
                vol,
                shrout
            FROM crsp_m_stock.msf a
            WHERE a.date BETWEEN '{start_date}' AND '{end_date}'
            ;
            """
        )
        df = pl.from_pandas(df, schema_overrides=crsp_schema)

        return CRSPMonthlySchema.validate(df)