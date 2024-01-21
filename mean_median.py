import pandas as pd 
import numpy as np
import matplotlib as plt

tit=pd.read_csv("titanic.csv")
print(tit.info())

print(tit[["Name","Sex"]]) #print the selected column "Name"  and "Sex" only
p=tit[tit["Cabin"].notna()] # print the data having not null value in cabin column
print(p)
print(tit.plot.box())

print(tit.plot.area(figsize=(12,4),subplots=True))

print(tit["Age"].mean())  #displays the mean
print(tit["Fare"].median()) #display Median

print(tit[["Sex","Age"]].groupby("Sex"))
print(tit[["Sex","Age"]].groupby("Sex").mean())

print(tit.sort_values(by=["Age"]).head())

print(tit.sort_values(by=["Age","Name","Sex"],ascending=False).head())

print(tit["Age"].hist()) 
print(tit.plot()) 
