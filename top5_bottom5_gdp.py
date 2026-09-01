import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/india_states.csv")
top5 = df.nlargest(5, "gdp_billion_usd")
bottom5 = df.nsmallest(5, "gdp_billion_usd")
combined = pd.concat([top5, bottom5])

colors = ["steelblue"] * 5 + ["tomato"] * 5
plt.figure(figsize=(10, 6))
plt.barh(combined["state"], combined["gdp_billion_usd"], color=colors)
plt.xlabel("GDP (Billion USD)")
plt.title("Top 5 vs Bottom 5 States by GDP")
plt.tight_layout()
plt.savefig("charts/top5_bottom5_gdp.png", dpi=150)
print("Saved.")
