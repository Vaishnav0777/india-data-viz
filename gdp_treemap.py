import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

df = pd.read_csv("data/india_states.csv").sort_values("gdp_billion_usd", ascending=False)
top12 = df.head(12)

fig, ax = plt.subplots(figsize=(12, 7))
colors = plt.cm.RdYlGn(np.linspace(0.3, 0.9, len(top12)))

x, y, w_total = 0, 0, 10
sizes = (top12["gdp_billion_usd"] / top12["gdp_billion_usd"].sum() * 100).values

for i, (size, color) in enumerate(zip(sizes, colors)):
    width = size / 10
    rect = mpatches.FancyBboxPatch((x, y), width, 1.5, boxstyle="round,pad=0.05",
                                    facecolor=color, edgecolor="white", linewidth=2)
    ax.add_patch(rect)
    ax.text(x + width/2, y + 0.75, top12.iloc[i]["state"],
            ha="center", va="center", fontsize=7, fontweight="bold")
    x += width

ax.set_xlim(0, 10)
ax.set_ylim(0, 2)
ax.axis("off")
plt.title("GDP Share — Top 12 States", fontsize=13)
plt.tight_layout()
plt.savefig("charts/gdp_treemap.png", dpi=150)
print("Saved.")
