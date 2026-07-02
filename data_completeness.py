import pandas as pd

df = pd.read_csv("data/india_states.csv")
print("Shape:", df.shape)
print("\nMissing values:")
print(df.isnull().sum())
print("\nData types:")
print(df.dtypes)
print("\nBasic stats:")
print(df.describe().round(2))
