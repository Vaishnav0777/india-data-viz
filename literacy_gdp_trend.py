import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("data/india_states.csv")

plt.figure(figsize=(10, 7))
plt.scatter(df["literacy_rate"], df["gdp_billion_usd"], s=80, alpha=0.6, color="darkorange")

m, b = np.polyfit(df["literacy_rate"], df["gdp_billion_usd"], 1)
x = np.linspace(df["literacy_rate"].min(), df["literacy_rate"].max(), 100)
plt.plot(x, m * x + b, color="red", linewidth=1.5, linestyle="--", label="Trend line")

for _, row in df.iterrows():
    plt.annotate(row["state"], (row["literacy_rate"], row["gdp_billion_usd"]),
                 fontsize=7, alpha=0.6, xytext=(3, 3), textcoords="offset points")

plt.xlabel("Literacy Rate (%)")
plt.ylabel("GDP (Billion USD)")
plt.title("Literacy Rate vs GDP with Trend Line")
plt.legend()
plt.tight_layout()
plt.savefig("charts/literacy_gdp_trend.png", dpi=150)
print("Saved.")
