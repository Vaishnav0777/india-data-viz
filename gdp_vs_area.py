import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/india_states.csv")

plt.figure(figsize=(10, 7))
plt.scatter(df["area_sq_km"], df["gdp_billion_usd"], s=80, alpha=0.7, color="mediumorchid")

for _, row in df.iterrows():
    plt.annotate(row["state"], (row["area_sq_km"], row["gdp_billion_usd"]),
                 fontsize=7, alpha=0.6, xytext=(3, 3), textcoords="offset points")

plt.xlabel("Area (sq km)")
plt.ylabel("GDP (Billion USD)")
plt.title("GDP vs Land Area by State")
plt.tight_layout()
plt.savefig("charts/gdp_vs_area.png", dpi=150)
print("Saved.")
