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

    @staticmethod
    def to_date(col, **kwargs):
        return pd.to_datetime(
            col,
            format=kwargs.get('format', '%Y-%m-%d'),
            errors=kwargs.get('errors', 'coerce')
        ).dt.date

    @staticmethod
    def to_interger(col):
        return col.apply(lambda x : int(x) if pd.notnull(x) else np.NaN)
