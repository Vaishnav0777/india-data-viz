import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/india_states.csv")

plt.figure(figsize=(10, 7))
plt.scatter(df["density_per_sq_km"], df["literacy_rate"], s=80, alpha=0.7, color="teal")

for _, row in df.iterrows():
    plt.annotate(row["state"], (row["density_per_sq_km"], row["literacy_rate"]),
                 fontsize=7, alpha=0.6, xytext=(3, 3), textcoords="offset points")

plt.xlabel("Population Density (per sq km)")
plt.ylabel("Literacy Rate (%)")
plt.title("Literacy Rate vs Population Density")
plt.tight_layout()
plt.savefig("charts/literacy_vs_density.png", dpi=150)
print("Saved.")
