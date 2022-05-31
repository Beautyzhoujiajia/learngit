import numpy as np
import pandas as pd
#load the data

df=pd.read_csv("pd_hoa_activities.csv")

print(df.head())
print(df.shape)
#explore the data
print("number of participants:",df.shape[0])

df.replace("?",np.NaN,inplace=True)

print(df.isnull().sum())

df.dropna(inplace=True)
print("after dropping rows with missing values")

print(df.isnull().sum())
print(df.shape)
df.reset_index(inplace=True,drop=True)
print(df.tail())
 
#clean the class column
class_ser = df["class"].copy()
for i in range(len(class_ser)):
    curr_class = str(class_ser.iloc[i])
    print(curr_class)
    curr_class=curr_class.lower()
   
    if "hoa" in curr_class or "healthy" in curr_class:
        print("------------")
        class_ser.iloc[i] = "hoa"

print(class_ser.value_counts())
#check  column types
