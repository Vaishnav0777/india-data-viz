import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/india_states.csv")
max_gdp = df.loc[df.groupby("region")["gdp_billion_usd"].idxmax()][["region", "state", "gdp_billion_usd"]]

plt.figure(figsize=(9, 5))
plt.bar(max_gdp["region"], max_gdp["gdp_billion_usd"], color="darkorange")
plt.ylabel("GDP (Billion USD)")
plt.title("Highest GDP State per Region")
for i, row in enumerate(max_gdp.itertuples()):
    plt.text(i, row.gdp_billion_usd + 5, row.state, ha="center", fontsize=8)
plt.tight_layout()
plt.savefig("charts/region_max_gdp.png", dpi=150)
print("Saved.")
