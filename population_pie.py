import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/india_states.csv")
top6 = df.nlargest(6, "population_millions")
others = pd.DataFrame([{"state": "Others", "population_millions": df[~df.index.isin(top6.index)]["population_millions"].sum()}])
data = pd.concat([top6[["state", "population_millions"]], others])

plt.figure(figsize=(8, 8))
plt.pie(data["population_millions"], labels=data["state"], autopct="%1.1f%%", startangle=140)
plt.title("Population Share — Top 6 States vs Others")
plt.tight_layout()
plt.savefig("charts/population_pie.png", dpi=150)
print("Saved.")
