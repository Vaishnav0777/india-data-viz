import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/india_states.csv")
df["score"] = (
    df["gdp_billion_usd"].rank() +
    df["literacy_rate"].rank() +
    df["population_millions"].rank(ascending=False)
)
top10 = df.nlargest(10, "score")

plt.figure(figsize=(10, 6))
plt.barh(top10["state"], top10["score"], color="mediumpurple")
plt.xlabel("Composite Score (GDP + Literacy + Population ranks)")
plt.title("Top 10 States — Multi-Metric Composite Score")
plt.tight_layout()
plt.savefig("charts/multi_metric_top10.png", dpi=150)
print("Saved.")
