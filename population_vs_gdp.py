import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/india_states.csv")

plt.figure(figsize=(10, 7))
plt.scatter(df["population_millions"], df["gdp_billion_usd"], s=80, alpha=0.7, color="darkorange")

for _, row in df.iterrows():
    plt.annotate(row["state"], (row["population_millions"], row["gdp_billion_usd"]),
                 fontsize=7, alpha=0.6, xytext=(3, 3), textcoords="offset points")

plt.xlabel("Population (Millions)")
plt.ylabel("GDP (Billion USD)")
plt.title("Population vs GDP by State")
plt.tight_layout()
plt.savefig("charts/population_vs_gdp.png", dpi=150)
print("Saved.")
