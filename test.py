import pandas as pd

populations = [24.8, 21.1, 7.9, 2.6]
cities = ["Shanghai", "Beijing","Hangzhou","Zibo"]
pop_ser = pd.Series(populations,index=cities)
print(pop_ser)
pop_ser.name="population"
print(pop_ser)

#indexing/slicing
print(pop_ser["Beijing"])
print(pop_ser[["Beijing", "Zibo"]])
print("**")
print(pop_ser["Beijing": "Zibo"])
print(pop_ser.iloc[1])
print(pop_ser.iloc[[1, 3]])
print(pop_ser.iloc[1: 3])
# summary statistics
print("average population:", pop_ser.mean())
print("standard deviation population:", pop_ser.std())
#add new data
pop_ser["Liuzhou"] = 2.1
print(pop_ser, len(pop_ser), pop_ser.shape)
#create empty series
pop_ser2 = pd.Series(dtype=float)
pop_ser2["Liuzhou"] = 2.1
print(pop_ser2)
#2D

pop_data = [
    ["Shanghai", 24.8, "Large"],
    ["Beijing", 21.1, "Large"],
    ["Hangzhou", 7.9, "Medium"],
    ["Zibo", 2.6, "Small"]
]
header = ["city", "population", "class"]
pop_df = pd.DataFrame(pop_data, columns=header)
pop_df = pop_df.set_index("city")
print(pop_df)
#indexing/slicing
pop_ser3 = pop_df["population"]
print(pop_ser3)
print(pop_df.iloc[:, 0])
#a simple
print(pop_df["population"]["Shanghai"])
print(pop_df.iloc[0, 0])

#use loc to mix
print(pop_df.loc["Shanghai", "population"])
print("-----------------------------")
#join demo
regions_df = pd.read_csv("regions.csv", index_col=0)
print(regions_df)
merged_df = pop_df.merge(regions_df, on=["city"], how="outer")
print(merged_df)
#grouped
grouped_by_class = merged_df.groupby("class")
print(grouped_by_class["population"].mean())
#save
merged_df.to_csv("merged.csv")
#warm up
large_df = merged_by_class.get_group("Large")
print(large_df)
large_df = merged_df(merged_df["class"]=="Large")
print(large_df)
#value_counts
print(len(merged_df["class"].value_counts()))
print(merged_df["class"].unique())
#append
new_row_ser = pd.Series([18.8,"Large","S"],name="Guangzhou",index=merged_df.columns)
merged_df = merged_df.append(new_row_ser)
print(merged_df)
#sort_values
merged_df = merged_df.sort_values("populaton",ascending=False)
print(merged_df)


