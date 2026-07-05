import pandas as pd

df = pd.read_csv("data/india_states.csv")
df["pop_rank"] = df["population_millions"].rank(ascending=False).astype(int)
ranked = df[["state", "region", "population_millions", "pop_rank"]].sort_values("pop_rank")
print(ranked.to_string(index=False))
ranked.to_csv("data/population_rankings.csv", index=False)
print("Saved to data/population_rankings.csv")
