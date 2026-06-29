import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/india_states.csv")
top5 = df.nlargest(5, "literacy_rate")

plt.figure(figsize=(8, 5))
plt.bar(top5["state"], top5["literacy_rate"], color="seagreen")
plt.ylabel("Literacy Rate (%)")
plt.title("Top 5 States by Literacy Rate")
plt.tight_layout()
plt.savefig("charts/top5_literacy.png", dpi=150)
print("Saved.")
