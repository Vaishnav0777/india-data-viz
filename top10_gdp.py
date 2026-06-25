import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/india_states.csv")
top10 = df.nlargest(10, "gdp_billion_usd").sort_values("gdp_billion_usd")

plt.figure(figsize=(10, 6))
plt.barh(top10["state"], top10["gdp_billion_usd"], color="steelblue")
plt.xlabel("GDP (Billion USD)")
plt.title("Top 10 Indian States by GDP")
plt.tight_layout()
plt.savefig("charts/top10_gdp.png", dpi=150)
plt.show()
print("Saved to charts/top10_gdp.png")
