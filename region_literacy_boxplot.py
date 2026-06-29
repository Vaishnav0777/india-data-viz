import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/india_states.csv")
regions = df["region"].unique()
data = [df[df["region"] == r]["literacy_rate"].values for r in regions]

plt.figure(figsize=(9, 6))
plt.boxplot(data, labels=regions, patch_artist=True)
plt.ylabel("Literacy Rate (%)")
plt.title("Literacy Rate Distribution by Region")
plt.tight_layout()
plt.savefig("charts/region_literacy_boxplot.png", dpi=150)
print("Saved.")
