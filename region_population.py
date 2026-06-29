import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/india_states.csv")
region_pop = df.groupby("region")["population_millions"].sum().sort_values()

plt.figure(figsize=(8, 5))
region_pop.plot(kind="barh", color="cornflowerblue")
plt.xlabel("Total Population (Millions)")
plt.title("Total Population by Region")
plt.tight_layout()
plt.savefig("charts/region_population.png", dpi=150)
print("Saved.")
