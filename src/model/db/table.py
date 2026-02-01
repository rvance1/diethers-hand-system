import polars as pl
import os

class Table:
    def __init__(self, base_path: str, name: str, columns: dict[str, pl.DataType]):
        self.path = base_path + "/" + name
        self.name = name
        self.columns = columns

    def to_dict(self) -> dict:
        return {
            'name': self.name,
            'columns': self.columns
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'Table':
        return cls(
            name = data['name'],
            columns = data['columns']
        )

    def get_path(self, year: int | None = None) -> str:
        if year:
            return f"{self.base_path}/{self.name}_{self.year}.parquet"
        else:
            return f"{self.base_path}/{self.name}_*.parquet"
    
    def path_exists(self, year: int | None = None) -> bool:
        return os.path.exists(self.get_path(year))

    def table_exists(self) -> bool:
        return os.path.exists(self.path)