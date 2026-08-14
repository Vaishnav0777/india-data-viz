import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/india_states.csv")
df["pop_density_ratio"] = df["population_millions"] / (df["area_sq_km"] / 1000)
df = df.sort_values("pop_density_ratio", ascending=False).head(10)

plt.figure(figsize=(10, 6))
plt.bar(df["state"], df["pop_density_ratio"], color="steelblue")
plt.xticks(rotation=45, ha="right")
plt.ylabel("Population per 1000 sq km")
plt.title("Top 10 States by Population per Land Area")
plt.tight_layout()
plt.savefig("charts/population_growth_proxy.png", dpi=150)
print("Saved.")
