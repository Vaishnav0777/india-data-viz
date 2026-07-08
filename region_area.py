import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/india_states.csv")
region_area = df.groupby("region")["area_sq_km"].sum().sort_values()

plt.figure(figsize=(8, 5))
region_area.plot(kind="barh", color="cadetblue")
plt.xlabel("Total Area (sq km)")
plt.title("Total Land Area by Region")
plt.tight_layout()
plt.savefig("charts/region_area.png", dpi=150)
print("Saved.")
