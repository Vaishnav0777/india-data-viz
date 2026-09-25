import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("data/india_states.csv")

plt.figure(figsize=(10, 7))
plt.scatter(df["area_sq_km"], df["literacy_rate"], s=80, alpha=0.7, color="mediumseagreen")

m, b = np.polyfit(df["area_sq_km"], df["literacy_rate"], 1)
x = np.linspace(df["area_sq_km"].min(), df["area_sq_km"].max(), 100)
plt.plot(x, m * x + b, color="red", linewidth=1.5, linestyle="--", label="Trend line")

for _, row in df.iterrows():
    plt.annotate(row["state"], (row["area_sq_km"], row["literacy_rate"]),
                 fontsize=7, alpha=0.6, xytext=(3, 3), textcoords="offset points")

plt.xlabel("Area (sq km)")
plt.ylabel("Literacy Rate (%)")
plt.title("Area vs Literacy Rate with Trend Line")
plt.legend()
plt.tight_layout()
plt.savefig("charts/area_vs_literacy.png", dpi=150)
print("Saved.")
