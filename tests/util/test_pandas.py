import pytest
import pandas as pd
import numpy as np

from etl_base.util.pandas import to_interger


@pytest.fixture
def df():
    return pd.DataFrame([{
        'num': '2',
        'char': 'a'
    }])


def test_to_interger(df):
    assert to_interger(df['num']).item() == 2
    assert np.isnan(to_interger(df['char']).item())
