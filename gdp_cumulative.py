import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/india_states.csv").sort_values("gdp_billion_usd", ascending=False)
df["cumulative_gdp"] = df["gdp_billion_usd"].cumsum()
df["cumulative_pct"] = (df["cumulative_gdp"] / df["gdp_billion_usd"].sum()) * 100

plt.figure(figsize=(10, 6))
plt.plot(range(1, len(df) + 1), df["cumulative_pct"], marker="o", color="darkorange")
plt.axhline(80, color="red", linestyle="--", alpha=0.6, label="80% threshold")
plt.xlabel("Number of States")
plt.ylabel("Cumulative GDP (%)")
plt.title("Cumulative GDP Contribution — States Ranked by GDP")
plt.legend()
plt.tight_layout()
plt.savefig("charts/gdp_cumulative.png", dpi=150)
print("Saved.")
