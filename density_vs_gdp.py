import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/india_states.csv")

plt.figure(figsize=(10, 7))
plt.scatter(df["density_per_sq_km"], df["gdp_billion_usd"], s=80, alpha=0.7, color="slateblue")

for _, row in df.iterrows():
    plt.annotate(row["state"], (row["density_per_sq_km"], row["gdp_billion_usd"]),
                 fontsize=7, alpha=0.6, xytext=(3, 3), textcoords="offset points")

plt.xlabel("Population Density (per sq km)")
plt.ylabel("GDP (Billion USD)")
plt.title("Population Density vs GDP")
plt.tight_layout()
plt.savefig("charts/density_vs_gdp.png", dpi=150)
print("Saved.")
