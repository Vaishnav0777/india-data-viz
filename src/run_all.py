"""Run all visualization scripts and generate every plot."""

import sys
from pathlib import Path

# Add src to path so imports work
sys.path.insert(0, str(Path(__file__).parent))

from analyze import load_data
from plot_population import plot_population_bar, plot_population_pie
from plot_literacy import plot_literacy_bar, plot_literacy_by_region
from plot_gdp import plot_gdp_bar, plot_gdp_vs_population, plot_gdp_per_capita
from plot_density import plot_density_bar, plot_area_vs_density
from plot_sex_ratio import plot_sex_ratio, plot_sex_ratio_vs_literacy
from plot_regional import plot_regional_overview, plot_correlation_heatmap
from plot_top_bottom import plot_top_bottom


def main():
    df = load_data()
    print("=" * 50)
    print("  Generating all visualizations...")
    print("=" * 50)

    print("\n[1/6] Population plots")
    plot_population_bar(df)
    plot_population_pie(df)

    print("\n[2/6] Literacy plots")
    plot_literacy_bar(df)
    plot_literacy_by_region(df)

    print("\n[3/6] GDP plots")
    plot_gdp_bar(df)
    plot_gdp_vs_population(df)
    plot_gdp_per_capita(df)

    print("\n[4/6] Density plots")
    plot_density_bar(df)
    plot_area_vs_density(df)

    print("\n[5/6] Sex ratio plots")
    plot_sex_ratio(df)
    plot_sex_ratio_vs_literacy(df)

    print("\n[6/7] Regional plots")
    plot_regional_overview(df)
    plot_correlation_heatmap(df)

    

    print("\n" + "=" * 50)
    print("  All 14 plots saved to plots/ folder!")
    print("=" * 50)

    print("\n[7/7] Top/Bottom comparison")
    plot_top_bottom(df)

if __name__ == "__main__":
    main()
