import pandas as pd

df = pd.read_csv("data/india_states.csv")

for col in ["gdp_billion_usd", "literacy_rate"]:
    df[col + "_norm"] = (df[col] - df[col].min()) / (df[col].max() - df[col].min())

density_inv = 1 - (df["density_per_sq_km"] - df["density_per_sq_km"].min()) / (df["density_per_sq_km"].max() - df["density_per_sq_km"].min())

df["wealth_index"] = (
    df["gdp_billion_usd_norm"] * 0.6 +
    df["literacy_rate_norm"] * 0.3 +
    density_inv * 0.1
).round(4)

ranked = df[["state", "region", "wealth_index"]].sort_values("wealth_index", ascending=False)
print(ranked.to_string(index=False))
ranked.to_csv("data/wealth_index.csv", index=False)
print("Saved to data/wealth_index.csv")
