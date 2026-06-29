import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/india_states.csv")
region_avg = df.groupby("region")["literacy_rate"].mean().sort_values()

plt.figure(figsize=(8, 5))
region_avg.plot(kind="barh", color="mediumseagreen")
plt.xlabel("Average Literacy Rate (%)")
plt.title("Average Literacy Rate by Region")
plt.tight_layout()
plt.savefig("charts/literacy_by_region.png", dpi=150)
print("Saved.")
