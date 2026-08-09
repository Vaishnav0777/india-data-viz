import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("data/india_states.csv")
top5 = df.nlargest(5, "gdp_billion_usd")

metrics = ["gdp_billion_usd", "population_millions", "literacy_rate", "density_per_sq_km"]
x = np.arange(len(metrics))
width = 0.15

fig, ax = plt.subplots(figsize=(12, 6))
for i, (_, row) in enumerate(top5.iterrows()):
    vals = [row[m] / df[m].max() for m in metrics]
    ax.bar(x + i * width, vals, width, label=row["state"])

ax.set_xticks(x + width * 2)
ax.set_xticklabels(["GDP", "Population", "Literacy", "Density"])
ax.set_ylabel("Normalized Score (0-1)")
ax.set_title("Multi-Metric Comparison — Top 5 GDP States")
ax.legend()
plt.tight_layout()
plt.savefig("charts/multi_metric_comparison.png", dpi=150)
print("Saved.")
