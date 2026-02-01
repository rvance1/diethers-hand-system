import polars as pl
import dataframely as dy

class ReturnsSchema(dy.Schema):
    date = dy.DateTime()
    id = dy.String()
    price = dy.Float64()
    ret = dy.Float64()
    size = dy.UInt32()

class SignalsSchema(dy.Schema):
    date = dy.DateTime()
    id = dy.String()
    signal = dy.Float64()

class AlphaSchema(dy.Schema):
    date = dy.DateTime()
    id = dy.String()
    alpha = dy.Float64()

class ActiveWeightsSchema(dy.Schema):
    date = dy.DateTime()
    id = dy.String()
    weight = dy.Float64()