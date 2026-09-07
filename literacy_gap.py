import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/india_states.csv")
nat_avg = df["literacy_rate"].mean()
df["literacy_gap"] = df["literacy_rate"] - nat_avg
df = df.sort_values("literacy_gap")

colors = ["tomato" if x < 0 else "seagreen" for x in df["literacy_gap"]]
plt.figure(figsize=(10, 8))
plt.barh(df["state"], df["literacy_gap"], color=colors)
plt.axvline(0, color="black", linewidth=0.8)
plt.xlabel("Deviation from National Average (%)")
plt.title("Literacy Rate Gap from National Average")
plt.tight_layout()
plt.savefig("charts/literacy_gap.png", dpi=150)
print("Saved.")
