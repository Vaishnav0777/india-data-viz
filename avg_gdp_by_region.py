import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/india_states.csv")
avg = df.groupby("region")["gdp_billion_usd"].mean().sort_values()

plt.figure(figsize=(8, 5))
avg.plot(kind="barh", color="steelblue")
plt.xlabel("Average GDP (Billion USD)")
plt.title("Average GDP by Region")
plt.tight_layout()
plt.savefig("charts/avg_gdp_by_region.png", dpi=150)
print("Saved.")
