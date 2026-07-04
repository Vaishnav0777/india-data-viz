import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/india_states.csv")

plt.figure(figsize=(10, 7))
plt.scatter(df["area_sq_km"], df["population_millions"], s=80, alpha=0.7, color="darkcyan")

for _, row in df.iterrows():
    plt.annotate(row["state"], (row["area_sq_km"], row["population_millions"]),
                 fontsize=7, alpha=0.6, xytext=(3, 3), textcoords="offset points")

plt.xlabel("Area (sq km)")
plt.ylabel("Population (Millions)")
plt.title("Area vs Population by State")
plt.tight_layout()
plt.savefig("charts/area_vs_population.png", dpi=150)
print("Saved.")
