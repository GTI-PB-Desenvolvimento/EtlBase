import os

import pandas as pd
from pandas import DataFrame


_DATA_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '_data')


def get_municipios() -> DataFrame:
    return pd.read_parquet(os.path.join(_DATA_PATH, 'municipios.parquet'))


def get_unidades_saude() -> DataFrame:
    return pd.read_parquet(os.path.join(_DATA_PATH, 'unidades_saude.parquet'))
