import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/india_states.csv")
top10 = df.nlargest(10, "density_per_sq_km").sort_values("density_per_sq_km")

plt.figure(figsize=(10, 6))
plt.barh(top10["state"], top10["density_per_sq_km"], color="tomato")
plt.xlabel("Population Density (per sq km)")
plt.title("Top 10 Most Densely Populated States")
plt.tight_layout()
plt.savefig("charts/top10_density.png", dpi=150)
print("Saved.")
