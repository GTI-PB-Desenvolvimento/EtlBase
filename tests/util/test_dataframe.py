from datetime import datetime

import pytest
import pandas as pd
import numpy as np

from etl_base.util import PandasUtils


@pytest.fixture
def df():
    return pd.DataFrame({
        'date': ['2023-12-01 11:11:11'],
        'num': '2',
        'char': 'a'
    })

def test_to_datetime(df):
    assert PandasUtils.to_datetime(df['date']).item() == datetime(2023,12,1,11,11,11)

def test_to_date(df):
    assert PandasUtils.to_date(df['date']).item() == datetime(2023,12,1).date()

def test_to_interger(df):
    assert PandasUtils.to_interger(df['num']).item() == 2
    assert np.isnan(PandasUtils.to_interger(df['char']).item())
