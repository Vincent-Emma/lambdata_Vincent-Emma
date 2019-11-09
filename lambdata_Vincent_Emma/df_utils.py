
import numpy as np
import pandas as pd

ONES = pd.Series(np.ones(20))
ZEROS = pd.Series(np.zeros(20))

def isna(df):
	print(df.isna().sum())


def correlation_matrix(df):
	print(df.corr())



