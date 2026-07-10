import pandas as pd

df = pd.read_csv("data/india_states.csv")
summary = df.groupby("region").agg(
    states=("state", "count"),
    total_population=("population_millions", "sum"),
    avg_literacy=("literacy_rate", "mean"),
    total_gdp=("gdp_billion_usd", "sum"),
    total_area=("area_sq_km", "sum")
).round(2)

print(summary.to_string())
summary.to_csv("data/region_summary.csv")
print("Saved to data/region_summary.csv")
