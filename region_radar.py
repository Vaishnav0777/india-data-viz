import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("data/india_states.csv")
metrics = ["gdp_billion_usd", "literacy_rate", "population_millions", "density_per_sq_km"]
region_avg = df.groupby("region")[metrics].mean()

for m in metrics:
    region_avg[m] = (region_avg[m] - region_avg[m].min()) / (region_avg[m].max() - region_avg[m].min())

labels = ["GDP", "Literacy", "Population", "Density"]
angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
colors = ["steelblue", "tomato", "seagreen", "darkorange", "mediumpurple"]

for i, (region, row) in enumerate(region_avg.iterrows()):
    values = row.tolist() + [row.tolist()[0]]
    ax.plot(angles, values, label=region, color=colors[i], linewidth=2)
    ax.fill(angles, values, alpha=0.1, color=colors[i])

ax.set_thetagrids(np.degrees(angles[:-1]), labels)
ax.set_title("Regional Radar — Normalized Metrics", fontsize=13, pad=20)
ax.legend(loc="upper right", bbox_to_anchor=(1.3, 1.1))
plt.tight_layout()
plt.savefig("charts/region_radar.png", dpi=150)
print("Saved.")
