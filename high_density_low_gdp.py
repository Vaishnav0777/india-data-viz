import pandas as pd

df = pd.read_csv("data/india_states.csv")
density_med = df["density_per_sq_km"].median()
gdp_med = df["gdp_billion_usd"].median()

result = df[(df["density_per_sq_km"] > density_med) & (df["gdp_billion_usd"] < gdp_med)]
print("High Density, Low GDP states:")
print(result[["state", "region", "density_per_sq_km", "gdp_billion_usd"]].to_string(index=False))
