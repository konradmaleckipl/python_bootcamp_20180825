import pandas as pd

data = pd.read_csv("./szablony_cwiczen/files_pandas_21_01_2017/titanic_train.csv")
print(data.head(20))

data = pd.read_csv("./szablony_cwiczen/files_pandas_21_01_2017/titanic_train.csv", nrows=10)
print(data.head(20))

data = pd.read_csv("./szablony_cwiczen/files_pandas_21_01_2017/titanic_train.csv", skiprows=1)
print(data.head(20))
