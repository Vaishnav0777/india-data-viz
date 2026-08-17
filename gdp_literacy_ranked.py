import pandas as pd

df = pd.read_csv("data/india_states.csv")
df["gdp_rank"] = df["gdp_billion_usd"].rank(ascending=False).astype(int)
df["literacy_rank"] = df["literacy_rate"].rank(ascending=False).astype(int)
df["rank_diff"] = df["gdp_rank"] - df["literacy_rank"]

result = df[["state", "region", "gdp_rank", "literacy_rank", "rank_diff"]].sort_values("rank_diff")
print(result.to_string(index=False))
result.to_csv("data/gdp_literacy_rank_comparison.csv", index=False)
print("Saved to data/gdp_literacy_rank_comparison.csv")
