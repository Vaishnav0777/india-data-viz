import pandas as pd

df = pd.read_csv("data/india_states.csv")
corr = df["literacy_rate"].corr(df["gdp_billion_usd"])
print(f"Pearson correlation (literacy vs GDP): {corr:.4f}")

corr2 = df["literacy_rate"].corr(df["density_per_sq_km"])
print(f"Pearson correlation (literacy vs density): {corr2:.4f}")

corr3 = df["population_millions"].corr(df["gdp_billion_usd"])
print(f"Pearson correlation (population vs GDP): {corr3:.4f}")
