import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/india_states.csv")
bubble_size = (df["gdp_billion_usd"] / df["gdp_billion_usd"].max()) * 2000

plt.figure(figsize=(11, 7))
plt.scatter(df["population_millions"], df["literacy_rate"], s=bubble_size, alpha=0.5, color="darkorange")

for _, row in df.iterrows():
    plt.annotate(row["state"], (row["population_millions"], row["literacy_rate"]),
                 fontsize=7, alpha=0.7, xytext=(3, 3), textcoords="offset points")

plt.xlabel("Population (Millions)")
plt.ylabel("Literacy Rate (%)")
plt.title("Literacy vs Population — Bubble Size = GDP")
plt.tight_layout()
plt.savefig("charts/literacy_population_bubble.png", dpi=150)
print("Saved.")
