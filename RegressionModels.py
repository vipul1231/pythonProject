import pandas as pd
import numpy as ny
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from sklearn.linear_model import LinearRegression

lm = LinearRegression()
path = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork" \
       "-DA0101EN-SkillsNetwork/labs/Data%20files/automobileEDA.csv"
df = pd.read_csv(path)

X = df[["highway-mpg"]]
Y = df["price"]

lm.fit(X, Y)
print(lm.predict(X))
print(lm.coef_)
print(lm.intercept_)
