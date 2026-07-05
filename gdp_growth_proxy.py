import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/india_states.csv")
df["gdp_per_sq_km"] = df["gdp_billion_usd"] / (df["area_sq_km"] / 1000)
df = df.sort_values("gdp_per_sq_km", ascending=False).head(10)

plt.figure(figsize=(10, 6))
plt.barh(df["state"], df["gdp_per_sq_km"], color="darkorange")
plt.xlabel("GDP per 1000 sq km (Billion USD)")
plt.title("Top 10 States — GDP Efficiency by Land Area")
plt.tight_layout()
plt.savefig("charts/gdp_per_sq_km.png", dpi=150)
print("Saved.")
