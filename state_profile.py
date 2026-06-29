import pandas as pd

def get_profile(state_name):
    df = pd.read_csv("data/india_states.csv")
    row = df[df["state"].str.lower() == state_name.lower()]
    if row.empty:
        print(f"State '{state_name}' not found.")
        return
    r = row.iloc[0]
    print(f"\n--- {r['state']} ---")
    print(f"Region:      {r['region']}")
    print(f"Population:  {r['population_millions']}M")
    print(f"Literacy:    {r['literacy_rate']}%")
    print(f"Density:     {r['density_per_sq_km']} per sq km")
    print(f"GDP:         ${r['gdp_billion_usd']}B")

get_profile("Kerala")
get_profile("Maharashtra")
