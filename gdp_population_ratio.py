import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/india_states.csv")
df["gdp_pop_ratio"] = df["gdp_billion_usd"] / df["population_millions"]
df = df.sort_values("gdp_pop_ratio", ascending=False).head(10)

plt.figure(figsize=(10, 6))
plt.bar(df["state"], df["gdp_pop_ratio"], color="cornflowerblue")
plt.xticks(rotation=45, ha="right")
plt.ylabel("GDP / Population (Billion USD per Million)")
plt.title("Top 10 States by GDP to Population Ratio")
plt.tight_layout()
plt.savefig("charts/gdp_population_ratio.png", dpi=150)
print("Saved.")
