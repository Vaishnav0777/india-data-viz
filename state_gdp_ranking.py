import pandas as pd

df = pd.read_csv("data/india_states.csv")
df["gdp_rank"] = df["gdp_billion_usd"].rank(ascending=False).astype(int)
df_sorted = df[["state", "region", "gdp_billion_usd", "gdp_rank"]].sort_values("gdp_rank")
print(df_sorted.to_string(index=False))
df_sorted.to_csv("data/gdp_rankings.csv", index=False)
print("Saved to data/gdp_rankings.csv")
