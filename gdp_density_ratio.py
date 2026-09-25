import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/india_states.csv")
df["gdp_density_ratio"] = df["gdp_billion_usd"] / df["density_per_sq_km"]
df = df.sort_values("gdp_density_ratio", ascending=False).head(10)

plt.figure(figsize=(10, 6))
plt.bar(df["state"], df["gdp_density_ratio"], color="darkcyan")
plt.xticks(rotation=45, ha="right")
plt.ylabel("GDP / Density Ratio")
plt.title("Top 10 States by GDP to Density Ratio")
plt.tight_layout()
plt.savefig("charts/gdp_density_ratio.png", dpi=150)
print("Saved.")
