import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/india_states.csv")
bottom10 = df.nsmallest(10, "population_millions").sort_values("population_millions")

plt.figure(figsize=(10, 6))
plt.barh(bottom10["state"], bottom10["population_millions"], color="lightskyblue")
plt.xlabel("Population (Millions)")
plt.title("10 Least Populous States")
plt.tight_layout()
plt.savefig("charts/bottom10_population.png", dpi=150)
print("Saved.")
