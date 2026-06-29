import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/india_states.csv")
df = df.sort_values("density_per_sq_km", ascending=False).head(15)

plt.figure(figsize=(10, 6))
plt.barh(df["state"], df["density_per_sq_km"], color="tomato")
plt.xlabel("Population Density (per sq km)")
plt.title("Top 15 States by Population Density")
plt.tight_layout()
plt.savefig("charts/population_density.png", dpi=150)
print("Saved.")
