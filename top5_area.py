import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/india_states.csv")
top5 = df.nlargest(5, "area_sq_km").sort_values("area_sq_km")

plt.figure(figsize=(9, 5))
plt.barh(top5["state"], top5["area_sq_km"], color="slategray")
plt.xlabel("Area (sq km)")
plt.title("Top 5 Largest States by Area")
plt.tight_layout()
plt.savefig("charts/top5_area.png", dpi=150)
print("Saved.")
