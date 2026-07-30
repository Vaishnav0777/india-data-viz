import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/india_states.csv")
bubble_size = (df["population_millions"] / df["population_millions"].max()) * 2000

plt.figure(figsize=(11, 7))
plt.scatter(df["area_sq_km"], df["gdp_billion_usd"], s=bubble_size, alpha=0.5, color="seagreen")

for _, row in df.iterrows():
    plt.annotate(row["state"], (row["area_sq_km"], row["gdp_billion_usd"]),
                 fontsize=7, alpha=0.7, xytext=(3, 3), textcoords="offset points")

plt.xlabel("Area (sq km)")
plt.ylabel("GDP (Billion USD)")
plt.title("Area vs GDP — Bubble Size = Population")
plt.tight_layout()
plt.savefig("charts/area_vs_gdp_bubble.png", dpi=150)
print("Saved.")
