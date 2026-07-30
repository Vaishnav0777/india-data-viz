import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/india_states.csv")
bottom10 = df.nsmallest(10, "gdp_billion_usd").sort_values("gdp_billion_usd")

plt.figure(figsize=(10, 6))
plt.barh(bottom10["state"], bottom10["gdp_billion_usd"], color="salmon")
plt.xlabel("GDP (Billion USD)")
plt.title("Bottom 10 States by GDP")
plt.tight_layout()
plt.savefig("charts/bottom10_gdp.png", dpi=150)
print("Saved.")
