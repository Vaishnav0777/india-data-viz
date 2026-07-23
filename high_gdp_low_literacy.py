import pandas as pd

df = pd.read_csv("data/india_states.csv")
lit_med = df["literacy_rate"].median()
gdp_med = df["gdp_billion_usd"].median()

anomalies = df[(df["gdp_billion_usd"] > gdp_med) & (df["literacy_rate"] < lit_med)]
print("High GDP, Low Literacy states:")
print(anomalies[["state", "region", "gdp_billion_usd", "literacy_rate"]].to_string(index=False))
