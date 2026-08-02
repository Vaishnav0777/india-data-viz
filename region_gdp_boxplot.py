import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/india_states.csv")
regions = df["region"].unique()
data = [df[df["region"] == r]["gdp_billion_usd"].values for r in regions]

plt.figure(figsize=(9, 6))
plt.boxplot(data, labels=regions, patch_artist=True)
plt.ylabel("GDP (Billion USD)")
plt.title("GDP Distribution by Region")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.savefig("charts/region_gdp_boxplot.png", dpi=150)
print("Saved.")
