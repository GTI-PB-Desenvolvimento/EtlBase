import numpy as np
import pandas as pd


def to_interger(col):
    return col.apply(
        lambda x : int(x) if pd.notnull(x) and str.isdigit(x) else np.NaN
    )
