import polars as pl
import dataframely as dy
import os
import datetime as dt

class TimeSeriesTable:
    def __init__(self, base_path: str, name: str, schema: dy.Schema):
        self.path = base_path + "/" + name
        self.name = name
        self.schema = schema

    def to_dict(self) -> dict:
        return {
            'name': self.name,
            'schema': self.schema
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'TimeSeriesTable':
        return cls(
            name = data['name'],
            schema = data['schema']
        )


    def get_path(self, year: int | None = None) -> str:
        if year:
            return f"{self.path}/{self.name}_{self.year}.parquet"
        else:
            return f"{self.base_path}/{self.name}_*.parquet"
    

    def path_exists(self, year: int | None = None) -> bool:
        return os.path.exists(self.get_path(year))


    def create_table_if_not_exists(self) -> None:
        if not os.path.exists(self.path):
            os.makedirs(self.path, exist_ok=True)
    
    
    def write_table(self, df: dy.DataFrame) -> None:
        pass

    def read_table(self, start_date: dt.date, end_date: dt.date) -> dy.DataFrame:
        pass