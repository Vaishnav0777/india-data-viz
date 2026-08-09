import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/india_states.csv")
top10 = df.nlargest(10, "literacy_rate").sort_values("literacy_rate")

plt.figure(figsize=(10, 6))
plt.barh(top10["state"], top10["literacy_rate"], color="mediumseagreen")
plt.xlabel("Literacy Rate (%)")
plt.title("Top 10 States by Literacy Rate")
plt.tight_layout()
plt.savefig("charts/top10_literacy.png", dpi=150)
print("Saved.")
