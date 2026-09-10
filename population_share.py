import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/india_states.csv")
df["pop_share"] = (df["population_millions"] / df["population_millions"].sum()) * 100
df = df.sort_values("pop_share", ascending=False)

plt.figure(figsize=(12, 6))
plt.bar(df["state"], df["pop_share"], color="cornflowerblue")
plt.xticks(rotation=60, ha="right", fontsize=7)
plt.ylabel("Population Share (%)")
plt.title("Each State's Share of Total Population")
plt.tight_layout()
plt.savefig("charts/population_share.png", dpi=150)
print("Saved.")
