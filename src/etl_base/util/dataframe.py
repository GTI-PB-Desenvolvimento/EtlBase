import pandas as pd
import numpy as np


class PandasUtils:
    
    @staticmethod
    def to_datetime(col, **kwargs):
        return pd.to_datetime(
            col,
            format=kwargs.get('format', '%Y-%m-%d %H:%M:%S'),
            errors=kwargs.get('errors', 'coerce')
        )

    @classmethod
    def to_date(cls, col, **kwargs):
        return cls.to_datetime(col, **kwargs).dt.date

    @staticmethod
    def to_interger(col):
        return col.apply(
            lambda x : int(x) if pd.notnull(x) and str.isdigit(x) else np.NaN
        )
