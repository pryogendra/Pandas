import pandas as pd 
import numpy as np
import matplotlib as plt

tit=pd.read_csv("titanic.csv")
print(tit.head(8)) #printing 8 rows data from top
print(tit.tail()) # printing botton default 5 rows data
print(tit.describe())
print(tit.dtypes)
