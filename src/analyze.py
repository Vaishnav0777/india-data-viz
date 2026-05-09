"""
Main analysis script — loads data, prints summary statistics, and runs all plots.
"""

import pandas as pd
from pathlib import Path


def load_data() -> pd.DataFrame:
    """Load the India states dataset."""
    data_path = Path(__file__).parent.parent / "data" / "india_states.csv"
    df = pd.read_csv(data_path)
    return df


def print_summary(df: pd.DataFrame) -> None:
    """Print key summary statistics."""
    print("=" * 60)
    print("  INDIA STATES — DATA SUMMARY")
    print("=" * 60)

    print(f"\n  Total states: {len(df)}")
    print(f"  Total population: {df['population_millions'].sum():.1f} million")
    print(f"  Average literacy rate: {df['literacy_rate'].mean():.1f}%")
    print(f"  Average sex ratio: {df['sex_ratio'].mean():.0f}")
    print(f"  Total GDP: ${df['gdp_billion_usd'].sum():.0f} billion")

    print(f"\n  Most populous: {df.loc[df['population_millions'].idxmax(), 'state']}")
    print(f"  Least populous: {df.loc[df['population_millions'].idxmin(), 'state']}")
    print(f"  Highest literacy: {df.loc[df['literacy_rate'].idxmax(), 'state']} ({df['literacy_rate'].max()}%)")
    print(f"  Lowest literacy: {df.loc[df['literacy_rate'].idxmin(), 'state']} ({df['literacy_rate'].min()}%)")
    print(f"  Highest GDP: {df.loc[df['gdp_billion_usd'].idxmax(), 'state']}")

    print("\n  Region breakdown:")
    for region, group in df.groupby("region"):
        print(f"    {region}: {len(group)} states, {group['population_millions'].sum():.1f}M people")

    print("=" * 60)


if __name__ == "__main__":
    df = load_data()
    print_summary(df)
    print("\nRun individual plot scripts in src/ to generate visualizations.")
