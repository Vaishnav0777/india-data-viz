import pandas as pd

def compare(s1, s2):
    df = pd.read_csv("data/india_states.csv")
    r1 = df[df["state"].str.lower() == s1.lower()].iloc[0]
    r2 = df[df["state"].str.lower() == s2.lower()].iloc[0]
    metrics = ["population_millions", "literacy_rate", "density_per_sq_km", "gdp_billion_usd"]
    print(f"\n{'Metric':<25} {r1['state']:<20} {r2['state']}")
    print("-" * 60)
    for m in metrics:
        print(f"{m:<25} {r1[m]:<20} {r2[m]}")

compare("Kerala", "Bihar")
