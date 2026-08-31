import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/india_states.csv")
corr_matrix = df[["population_millions", "literacy_rate", "gdp_billion_usd", "density_per_sq_km", "area_sq_km"]].corr()

fig, ax = plt.subplots(figsize=(8, 6))
im = ax.imshow(corr_matrix, cmap="coolwarm", vmin=-1, vmax=1)
plt.colorbar(im)
ax.set_xticks(range(len(corr_matrix)))
ax.set_yticks(range(len(corr_matrix)))
ax.set_xticklabels(corr_matrix.columns, rotation=45, ha="right", fontsize=8)
ax.set_yticklabels(corr_matrix.columns, fontsize=8)
for i in range(len(corr_matrix)):
    for j in range(len(corr_matrix)):
        ax.text(j, i, f"{corr_matrix.iloc[i, j]:.2f}", ha="center", va="center", fontsize=8)
plt.title("Correlation Matrix — All Numeric Features")
plt.tight_layout()
plt.savefig("charts/full_correlation_matrix.png", dpi=150)
print("Saved.")
