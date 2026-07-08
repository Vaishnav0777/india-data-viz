import pandas as pd

df = pd.read_csv("data/india_states.csv")
df["literacy_rank"] = df["literacy_rate"].rank(ascending=False).astype(int)
ranked = df[["state", "region", "literacy_rate", "literacy_rank"]].sort_values("literacy_rank")
print(ranked.to_string(index=False))
ranked.to_csv("data/literacy_rankings.csv", index=False)
print("Saved to data/literacy_rankings.csv")
