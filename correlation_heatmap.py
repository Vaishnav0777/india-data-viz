import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/india_states.csv")

numeric_cols = ["population_millions", "literacy_rate", "density_per_sq_km", "gdp_billion_usd", "area_sq_km"]
corr = df[numeric_cols].corr()

plt.figure(figsize=(9, 7))
sns.heatmap(
    corr,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    square=True,
    linewidths=0.5,
    cbar_kws={"shrink": 0.8}
)
plt.title("Correlation Matrix — Indian States")
plt.tight_layout()
plt.savefig("charts/correlation_heatmap.png", dpi=150)
plt.show()
print("Saved to charts/correlation_heatmap.png")
