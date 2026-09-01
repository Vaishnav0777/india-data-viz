import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("data/india_states.csv")
metrics = ["gdp_billion_usd", "literacy_rate", "population_millions", "density_per_sq_km"]

for m in metrics:
    df[m + "_norm"] = (df[m] - df[m].min()) / (df[m].max() - df[m].min())

top5 = df.nlargest(5, "gdp_billion_usd")
norm_cols = [m + "_norm" for m in metrics]
labels = ["GDP", "Literacy", "Population", "Density"]

x = np.arange(len(labels))
width = 0.15

fig, ax = plt.subplots(figsize=(11, 6))
for i, (_, row) in enumerate(top5.iterrows()):
    ax.bar(x + i * width, row[norm_cols].values, width, label=row["state"])

ax.set_xticks(x + width * 2)
ax.set_xticklabels(labels)
ax.set_ylabel("Normalized Score (0-1)")
ax.set_title("Normalized Metrics — Top 5 GDP States")
ax.legend()
plt.tight_layout()
plt.savefig("charts/normalized_metrics.png", dpi=150)
print("Saved.")
