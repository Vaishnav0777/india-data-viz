import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/india_states.csv")

plt.figure(figsize=(8, 5))
plt.hist(df["density_per_sq_km"], bins=8, color="steelblue", edgecolor="white")
plt.xlabel("Population Density (per sq km)")
plt.ylabel("Number of States")
plt.title("Distribution of Population Density Across States")
plt.tight_layout()
plt.savefig("charts/density_histogram.png", dpi=150)
print("Saved.")
