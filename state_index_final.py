import pandas as pd

df = pd.read_csv("data/india_states.csv")
cols = ["gdp_billion_usd", "literacy_rate", "population_millions", "area_sq_km"]

for col in cols:
    df[col + "_norm"] = (df[col] - df[col].min()) / (df[col].max() - df[col].min())

df["final_index"] = (
    df["gdp_billion_usd_norm"] * 0.4 +
    df["literacy_rate_norm"] * 0.3 +
    df["population_millions_norm"] * 0.2 +
    df["area_sq_km_norm"] * 0.1
).round(4)

result = df[["state", "region", "final_index"]].sort_values("final_index", ascending=False)
print(result.to_string(index=False))
result.to_csv("data/final_state_index.csv", index=False)
print("Saved to data/final_state_index.csv")
