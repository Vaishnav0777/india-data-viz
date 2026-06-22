import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/india_states.csv")

plt.figure(figsize=(10, 7))
sns.scatterplot(
    data=df,
    x="literacy_rate",
    y="gdp_billion_usd",
    hue="region",
    s=100
)

for _, row in df.iterrows():
    plt.annotate(row["state"], (row["literacy_rate"], row["gdp_billion_usd"]),
                 fontsize=7, alpha=0.7, xytext=(4, 4), textcoords="offset points")

plt.title("GDP vs Literacy Rate by State")
plt.xlabel("Literacy Rate (%)")
plt.ylabel("GDP (Billion USD)")
plt.tight_layout()
plt.savefig("charts/gdp_vs_literacy.png", dpi=150)
plt.show()
print("Saved to charts/gdp_vs_literacy.png")
