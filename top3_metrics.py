import pandas as pd

df = pd.read_csv("data/india_states.csv")
metrics = {
    "GDP": "gdp_billion_usd",
    "Literacy": "literacy_rate",
    "Population": "population_millions",
    "Density": "density_per_sq_km",
    "Area": "area_sq_km"
}

for label, col in metrics.items():
    top3 = df.nlargest(3, col)[["state", col]]
    print(f"\nTop 3 by {label}:")
    print(top3.to_string(index=False))
