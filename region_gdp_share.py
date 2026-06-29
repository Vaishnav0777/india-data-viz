import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/india_states.csv")
region_gdp = df.groupby("region")["gdp_billion_usd"].sum()

plt.figure(figsize=(7, 7))
plt.pie(region_gdp, labels=region_gdp.index, autopct="%1.1f%%", startangle=140)
plt.title("Regional Share of Total GDP")
plt.tight_layout()
plt.savefig("charts/region_gdp_share.png", dpi=150)
print("Saved.")
