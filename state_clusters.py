import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/india_states.csv")
df["gdp_norm"] = (df["gdp_billion_usd"] - df["gdp_billion_usd"].min()) / (df["gdp_billion_usd"].max() - df["gdp_billion_usd"].min())
df["lit_norm"] = (df["literacy_rate"] - df["literacy_rate"].min()) / (df["literacy_rate"].max() - df["literacy_rate"].min())

def cluster(row):
    if row["gdp_norm"] > 0.5 and row["lit_norm"] > 0.5:
        return "Advanced"
    elif row["gdp_norm"] > 0.5:
        return "Wealthy"
    elif row["lit_norm"] > 0.5:
        return "Educated"
    return "Developing"

df["cluster"] = df.apply(cluster, axis=1)
colors = {"Advanced": "green", "Wealthy": "gold", "Educated": "steelblue", "Developing": "tomato"}

plt.figure(figsize=(10, 7))
for cl, grp in df.groupby("cluster"):
    plt.scatter(grp["literacy_rate"], grp["gdp_billion_usd"], label=cl, color=colors[cl], s=90)
    for _, row in grp.iterrows():
        plt.annotate(row["state"], (row["literacy_rate"], row["gdp_billion_usd"]), fontsize=7, alpha=0.6)

plt.xlabel("Literacy Rate (%)")
plt.ylabel("GDP (Billion USD)")
plt.title("State Clusters by GDP and Literacy")
plt.legend()
plt.tight_layout()
plt.savefig("charts/state_clusters.png", dpi=150)
print("Saved.")
