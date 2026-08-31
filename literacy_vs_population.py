import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("data/india_states.csv")

plt.figure(figsize=(10, 7))
plt.scatter(df["population_millions"], df["literacy_rate"], s=80, alpha=0.7, color="mediumorchid")

m, b = np.polyfit(df["population_millions"], df["literacy_rate"], 1)
x = np.linspace(df["population_millions"].min(), df["population_millions"].max(), 100)
plt.plot(x, m * x + b, color="red", linewidth=1.5, linestyle="--", label="Trend line")

for _, row in df.iterrows():
    plt.annotate(row["state"], (row["population_millions"], row["literacy_rate"]),
                 fontsize=7, alpha=0.6, xytext=(3, 3), textcoords="offset points")

plt.xlabel("Population (Millions)")
plt.ylabel("Literacy Rate (%)")
plt.title("Population vs Literacy Rate with Trend Line")
plt.legend()
plt.tight_layout()
plt.savefig("charts/literacy_vs_population.png", dpi=150)
print("Saved.")
