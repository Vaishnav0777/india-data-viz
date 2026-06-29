import pandas as pd

df = pd.read_csv("data/india_states.csv")
stats = df.describe().round(2)
print(stats)
stats.to_csv("data/summary_stats.csv")
print("Saved to data/summary_stats.csv")
