import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/india_states.csv")
bottom5 = df.nsmallest(5, "density_per_sq_km").sort_values("density_per_sq_km")

plt.figure(figsize=(9, 5))
plt.barh(bottom5["state"], bottom5["density_per_sq_km"], color="lightskyblue")
plt.xlabel("Population Density (per sq km)")
plt.title("5 Least Densely Populated States")
plt.tight_layout()
plt.savefig("charts/bottom5_density.png", dpi=150)
print("Saved.")
