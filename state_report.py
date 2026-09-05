import pandas as pd

df = pd.read_csv("data/india_states.csv")
df["gdp_rank"] = df["gdp_billion_usd"].rank(ascending=False).astype(int)
df["literacy_rank"] = df["literacy_rate"].rank(ascending=False).astype(int)
df["density_rank"] = df["density_per_sq_km"].rank(ascending=False).astype(int)
df["pop_rank"] = df["population_millions"].rank(ascending=False).astype(int)

report = df[["state", "region", "gdp_rank", "literacy_rank", "density_rank", "pop_rank"]]
print(report.sort_values("gdp_rank").to_string(index=False))
report.to_csv("data/state_full_report.csv", index=False)
print("Saved to data/state_full_report.csv")
