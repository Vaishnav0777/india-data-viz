import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/india_states.csv")
counts = df["region"].value_counts()

plt.figure(figsize=(8, 5))
counts.plot(kind="bar", color="mediumpurple", edgecolor="white")
plt.ylabel("Number of States")
plt.title("Number of States per Region")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.savefig("charts/region_state_count.png", dpi=150)
print("Saved.")
