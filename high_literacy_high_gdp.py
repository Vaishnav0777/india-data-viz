import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/india_states.csv")
lit_thresh = df["literacy_rate"].median()
gdp_thresh = df["gdp_billion_usd"].median()
df["category"] = "Low-Low"
df.loc[(df["literacy_rate"] >= lit_thresh) & (df["gdp_billion_usd"] >= gdp_thresh), "category"] = "High-High"
df.loc[(df["literacy_rate"] >= lit_thresh) & (df["gdp_billion_usd"] < gdp_thresh), "category"] = "High Lit / Low GDP"
df.loc[(df["literacy_rate"] < lit_thresh) & (df["gdp_billion_usd"] >= gdp_thresh), "category"] = "Low Lit / High GDP"

colors = {"High-High": "green", "High Lit / Low GDP": "steelblue", "Low Lit / High GDP": "orange", "Low-Low": "red"}
plt.figure(figsize=(10, 7))
for cat, grp in df.groupby("category"):
    plt.scatter(grp["literacy_rate"], grp["gdp_billion_usd"], label=cat, color=colors[cat], s=90)
    for _, row in grp.iterrows():
        plt.annotate(row["state"], (row["literacy_rate"], row["gdp_billion_usd"]), fontsize=7, alpha=0.6)
plt.xlabel("Literacy Rate (%)")
plt.ylabel("GDP (Billion USD)")
plt.title("States by Literacy-GDP Quadrant")
plt.legend()
plt.tight_layout()
plt.savefig("charts/literacy_gdp_quadrant.png", dpi=150)
print("Saved.")
