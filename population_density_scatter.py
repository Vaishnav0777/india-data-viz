import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/india_states.csv")
bubble_size = (df["area_sq_km"] / df["area_sq_km"].max()) * 2000

plt.figure(figsize=(11, 7))
plt.scatter(df["population_millions"], df["density_per_sq_km"], s=bubble_size, alpha=0.5, color="crimson")

for _, row in df.iterrows():
    plt.annotate(row["state"], (row["population_millions"], row["density_per_sq_km"]),
                 fontsize=7, alpha=0.7, xytext=(3, 3), textcoords="offset points")

plt.xlabel("Population (Millions)")
plt.ylabel("Density (per sq km)")
plt.title("Population vs Density — Bubble Size = Area")
plt.tight_layout()
plt.savefig("charts/population_density_scatter.png", dpi=150)
print("Saved.")
