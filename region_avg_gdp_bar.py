import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/india_states.csv")
avg = df.groupby("region").agg(
    avg_gdp=("gdp_billion_usd", "mean"),
    avg_literacy=("literacy_rate", "mean")
).reset_index()

x = range(len(avg))
plt.figure(figsize=(10, 6))
plt.bar(avg["region"], avg["avg_gdp"], color="cornflowerblue", alpha=0.8)
plt.ylabel("Average GDP (Billion USD)")
plt.title("Average GDP per State by Region")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.savefig("charts/region_avg_gdp.png", dpi=150)
print("Saved.")
