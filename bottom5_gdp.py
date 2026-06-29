import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/india_states.csv")
bottom5 = df.nsmallest(5, "gdp_billion_usd")

plt.figure(figsize=(8, 5))
plt.bar(bottom5["state"], bottom5["gdp_billion_usd"], color="salmon")
plt.ylabel("GDP (Billion USD)")
plt.title("Bottom 5 States by GDP")
plt.tight_layout()
plt.savefig("charts/bottom5_gdp.png", dpi=150)
print("Saved.")
