import polars as pl
import dataframely as dy
from typing import TypeAlias

class ReturnsSchema(dy.Schema):
    date = dy.Date()
    id = dy.String()
    price = dy.Float64()
    ret = dy.Float64()
    size = dy.UInt32()

class SignalsSchema(dy.Schema):
    date = dy.Date()
    id = dy.String()
    signal = dy.Float64()

class AlphaSchema(dy.Schema):
    date = dy.Date()
    id = dy.String()
    alpha = dy.Float64()

class ActiveWeightsSchema(dy.Schema):
    date = dy.Date()
    id = dy.String()
    weight = dy.Float64()

class CRSPMonthlySchema(dy.Schema):
    date = dy.Date()
    permno = dy.Int64()
    cusip = dy.String()
    ret = dy.Float64(nullable=True)
    retx = dy.Float64(nullable=True)
    prc = dy.Float64(nullable=True)
    vol = dy.Int64(nullable=True)
    shrout = dy.Int64(nullable=True)

CRSPMonthlyDF: TypeAlias = dy.DataFrame[CRSPMonthlySchema]