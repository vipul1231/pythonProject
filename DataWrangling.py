import pandas as pd
import numpy as ny
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

other_path = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN" \
             "-SkillsNetwork/labs/Data%20files/auto.csv"

df = pd.read_csv(other_path, header=None)

headers = ["symboling", "normalized-losses", "make", "fuel-type", "aspiration", "num-of-doors", "body-style",
           "drive-wheels", "engine-location", "wheel-base", "length", "width", "height", "curb-weight", "engine-type",
           "num-of-cylinders", "engine-size", "fuel-system", "bore", "stroke", "compression-ratio", "horsepower",
           "peak-rpm", "city-mpg", "highway-mpg", "price"]
df.columns = headers

print(df.head(5))
df.replace("?", ny.NAN, inplace=True)
missing_data = df.isnull()

print(missing_data.head(5))


for column in missing_data.columns.values.tolist():
    print(column)
    print(missing_data[column].value_counts())
    print(" ")

#Average of a columns

avg_norm_loss = df["normalized-losses"].astype("float").mean(axis=0)
print("Average normalized losses: ", avg_norm_loss)

df["normalized-losses"].replace(ny.nan, avg_norm_loss, inplace=True)
print("New after replacing NAN with Average normalized losses: ", avg_norm_loss)

print(df["num-of-doors"].value_counts())
print(df["num-of-doors"].value_counts().idxmax())

#Group by usage

df_test = df[["drive-wheels", "body-style", "price"]]
df_test = df_test.dropna(subset=["price"], axis=0, inplace=False)
df_test = df_test.astype({'price': 'int32'})

print(df_test.dtypes)
#as_index will just change the view of the table.
df_group = df_test.groupby(['drive-wheels', 'body-style'], as_index=False).mean()
print(df_group)
df_pivot = df_group.pivot(index="drive-wheels", columns="body-style")
print(df_pivot)


# plt.pcolor(df_pivot, cmap='RdBu')
# plt.colorbar()
# plt.show()

#reg-plot

path = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/automobileEDA.csv"
df2 = pd.read_csv(path)
print(df2[["engine-size","price"]].corr())
sns.regplot(x="engine-size", y="price", data=df2)
plt.ylim(0,)
plt.show()

sns.regplot(x="highway-mpg", y="price", data=df2)
plt.ylim(0,)
plt.show()
print(df2[["highway-mpg","price"]].corr())

sns.boxplot(x='body-style', y="price", data=df2)
plt.show()

print("Unique wheels drive: ", df2["drive-wheels"].unique())


pearson_coef, p_value = stats.pearsonr(df2['wheel-base'], df2['price'])
print("Person Coefficient: ",pearson_coef, " and its P-Value: ", p_value)

# print(df.head(10))
# # print(df.describe(include="all"))
# df1 = df.replace("?", ny.NAN)
#
# print(df1.head())
#
# df1.dropna(subset=["price"], axis=0, inplace=True)
# # print(df1.head(20))
#
# df1['symboling'] = df1['symboling'] + 1
# # print(df1.head())
# df1.rename(columns={"symboling": "trust"}, inplace=True)
# # print(df1.head())
#
# #Binning in data pre processing
#
# df1["price"] = df1["price"].astype("int")
# bins = ny.linspace(min(df1["price"]), max(df1["price"]), 4)
#
# group_names = ["Low", "Medium", "High"]
# df1["binned_price"] = pd.cut(df1["price"], bins, labels=group_names, include_lowest=True)
# print(df1.head(100))
#
# print(df1[["fuel-system"]])
# print(df1["fuel-system"].unique())
# print(pd.get_dummies(df["fuel-system"]))
# df.to_csv("new.csv", index=False)
# print(df.info())
