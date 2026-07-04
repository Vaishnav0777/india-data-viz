import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/india_states.csv")
avg_density = df.groupby("region")["density_per_sq_km"].mean().sort_values(ascending=False)

plt.figure(figsize=(8, 5))
avg_density.plot(kind="bar", color="tomato", edgecolor="white")
plt.ylabel("Avg Density (per sq km)")
plt.title("Average Population Density by Region")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.savefig("charts/avg_density_by_region.png", dpi=150)
print("Saved.")
