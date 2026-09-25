import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/india_states.csv")
regions = df["region"].unique()
data = [df[df["region"] == r]["density_per_sq_km"].values for r in regions]

plt.figure(figsize=(9, 6))
plt.boxplot(data, labels=regions, patch_artist=True)
plt.ylabel("Population Density (per sq km)")
plt.title("Population Density Distribution by Region")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.savefig("charts/region_density_boxplot.png", dpi=150)
print("Saved.")
