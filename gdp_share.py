import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/india_states.csv")
df["gdp_share"] = (df["gdp_billion_usd"] / df["gdp_billion_usd"].sum()) * 100
df = df.sort_values("gdp_share", ascending=False)

plt.figure(figsize=(12, 6))
plt.bar(df["state"], df["gdp_share"], color="mediumseagreen")
plt.xticks(rotation=60, ha="right", fontsize=7)
plt.ylabel("GDP Share (%)")
plt.title("Each State's Share of Total GDP")
plt.tight_layout()
plt.savefig("charts/gdp_share.png", dpi=150)
print("Saved.")
