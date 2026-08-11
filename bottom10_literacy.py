import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/india_states.csv")
bottom10 = df.nsmallest(10, "literacy_rate").sort_values("literacy_rate")

plt.figure(figsize=(10, 6))
plt.barh(bottom10["state"], bottom10["literacy_rate"], color="tomato")
plt.xlabel("Literacy Rate (%)")
plt.title("Bottom 10 States by Literacy Rate")
plt.tight_layout()
plt.savefig("charts/bottom10_literacy.png", dpi=150)
print("Saved.")
