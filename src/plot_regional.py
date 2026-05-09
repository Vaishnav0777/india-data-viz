"""Plot regional comparison charts."""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from pathlib import Path
from analyze import load_data


def plot_regional_overview(df: pd.DataFrame) -> None:
    """Multi-panel comparison of regions across key metrics."""
    regional = df.groupby("region").agg(
        total_pop=("population_millions", "sum"),
        avg_literacy=("literacy_rate", "mean"),
        total_gdp=("gdp_billion_usd", "sum"),
        avg_sex_ratio=("sex_ratio", "mean"),
        num_states=("state", "count"),
    ).sort_values("total_pop", ascending=False)

    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle("Regional Comparison — Indian States", fontsize=16, fontweight="bold", y=1.02)

    # Total population
    ax = axes[0, 0]
    colors = sns.color_palette("Set2", len(regional))
    ax.bar(regional.index, regional["total_pop"], color=colors)
    ax.set_title("Total Population (millions)")
    ax.set_ylabel("Population (M)")

    # Average literacy
    ax = axes[0, 1]
    ax.bar(regional.index, regional["avg_literacy"], color=colors)
    ax.set_title("Average Literacy Rate (%)")
    ax.axhline(df["literacy_rate"].mean(), color="red", linestyle="--", alpha=0.7)

    # Total GDP
    ax = axes[1, 0]
    ax.bar(regional.index, regional["total_gdp"], color=colors)
    ax.set_title("Total GDP (Billion USD)")
    ax.set_ylabel("GDP ($B)")

    # Average sex ratio
    ax = axes[1, 1]
    ax.bar(regional.index, regional["avg_sex_ratio"], color=colors)
    ax.set_title("Average Sex Ratio")
    ax.axhline(1000, color="red", linestyle="--", alpha=0.7)

    for ax in axes.flat:
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.tick_params(axis="x", rotation=30)

    plt.tight_layout()
    output = Path(__file__).parent.parent / "plots" / "regional_overview.png"
    output.parent.mkdir(exist_ok=True)
    plt.savefig(output, dpi=150, bbox_inches="tight")
    print(f"  Saved: {output}")
    plt.close()


def plot_correlation_heatmap(df: pd.DataFrame) -> None:
    """Heatmap of correlations between numeric variables."""
    numeric_cols = ["population_millions", "area_sq_km", "density_per_sq_km",
                    "literacy_rate", "sex_ratio", "gdp_billion_usd"]
    corr = df[numeric_cols].corr()

    fig, ax = plt.subplots(figsize=(9, 7))
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="RdBu_r", center=0,
                square=True, linewidths=0.5, ax=ax,
                xticklabels=[c.replace("_", " ").title() for c in numeric_cols],
                yticklabels=[c.replace("_", " ").title() for c in numeric_cols])

    ax.set_title("Correlation Heatmap — Indian States Data", fontsize=14, fontweight="bold", pad=20)

    plt.tight_layout()
    output = Path(__file__).parent.parent / "plots" / "correlation_heatmap.png"
    plt.savefig(output, dpi=150, bbox_inches="tight")
    print(f"  Saved: {output}")
    plt.close()


if __name__ == "__main__":
    df = load_data()
    print("\nGenerating regional plots...")
    plot_regional_overview(df)
    plot_correlation_heatmap(df)
    print("Done!")
