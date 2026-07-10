import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/india_states.csv")
df = df.sort_values("density_per_sq_km")

plt.figure(figsize=(10, 8))
bars = plt.barh(df["state"], df["density_per_sq_km"],
                color=plt.cm.YlOrRd([x / df["density_per_sq_km"].max() for x in df["density_per_sq_km"]]))
plt.xlabel("Population Density (per sq km)")
plt.title("All States Ranked by Population Density")
plt.tight_layout()
plt.savefig("charts/state_density_ranked.png", dpi=150)
print("Saved.")
