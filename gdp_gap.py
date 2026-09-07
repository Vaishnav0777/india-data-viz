import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/india_states.csv")
nat_avg = df["gdp_billion_usd"].mean()
df["gdp_gap"] = df["gdp_billion_usd"] - nat_avg
df = df.sort_values("gdp_gap")

colors = ["tomato" if x < 0 else "steelblue" for x in df["gdp_gap"]]
plt.figure(figsize=(10, 8))
plt.barh(df["state"], df["gdp_gap"], color=colors)
plt.axvline(0, color="black", linewidth=0.8)
plt.xlabel("Deviation from National Average (Billion USD)")
plt.title("GDP Gap from National Average")
plt.tight_layout()
plt.savefig("charts/gdp_gap.png", dpi=150)
print("Saved.")
