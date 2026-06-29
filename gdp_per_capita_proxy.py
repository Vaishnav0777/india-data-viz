import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/india_states.csv")
df["gdp_per_capita_proxy"] = (df["gdp_billion_usd"] * 1000) / df["population_millions"]
df = df.sort_values("gdp_per_capita_proxy", ascending=False).head(10)

plt.figure(figsize=(10, 6))
plt.bar(df["state"], df["gdp_per_capita_proxy"], color="mediumpurple")
plt.xticks(rotation=45, ha="right")
plt.ylabel("GDP per Capita Proxy (Million USD)")
plt.title("Top 10 States — GDP per Capita Proxy")
plt.tight_layout()
plt.savefig("charts/gdp_per_capita_proxy.png", dpi=150)
print("Saved.")
