import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/india_states.csv")
df["gdp_area_ratio"] = df["gdp_billion_usd"] / (df["area_sq_km"] / 1000)
df = df.sort_values("gdp_area_ratio", ascending=False).head(10)

plt.figure(figsize=(10, 6))
plt.barh(df["state"], df["gdp_area_ratio"], color="mediumorchid")
plt.xlabel("GDP per 1000 sq km")
.title("Top 10 States by GDP per Land Area")
plt.tight_layout()
plt.savefig("charts/gdp_area_efficiency.png", dpi=150)
print("Saved.")
