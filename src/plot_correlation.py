"""Plot correlation heatmap across Indian state metrics."""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from pathlib import Path
from analyze import load_data


def plot_correlation_heatmap(df: pd.DataFrame) -> None:
    """Correlation heatmap of numeric state metrics, including derived GDP per capita."""
    df = df.copy()
    df["gdp_per_capita"] = (df["gdp_billion_usd"] * 1000) / df["population_millions"]

    metrics = [
        "population_millions",
        "area_sq_km",
        "density_per_sq_km",
        "literacy_rate",
        "sex_ratio",
        "gdp_billion_usd",
        "gdp_per_capita",
    ]
    labels = [
        "Population",
        "Area",
        "Density",
        "Literacy",
        "Sex Ratio",
        "GDP",
        "GDP/capita",
    ]

    corr = df[metrics].corr()

    fig, ax = plt.subplots(figsize=(9, 8))
    mask = np.triu(np.ones_like(corr, dtype=bool), k=1)
    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt=".2f",
        cmap="coolwarm",
        center=0,
        vmin=-1,
        vmax=1,
        square=True,
        linewidths=0.5,
        cbar_kws={"shrink": 0.8, "label": "Pearson r"},
        xticklabels=labels,
        yticklabels=labels,
        ax=ax,
    )

    ax.set_title("Correlation of Indian State Metrics", fontsize=15, fontweight="bold", pad=16)
    plt.xticks(rotation=45, ha="right")
    plt.yticks(rotation=0)

    plt.tight_layout()
    output = Path(__file__).parent.parent / "plots" / "correlation_heatmap.png"
    output.parent.mkdir(exist_ok=True)
    plt.savefig(output, dpi=150, bbox_inches="tight")
    print(f"  Saved: {output}")
    plt.close()


def print_strongest_pairs(df: pd.DataFrame, top_n: int = 5) -> None:
    """Print the strongest metric correlations, ignoring self-pairs."""
    df = df.copy()
    df["gdp_per_capita"] = (df["gdp_billion_usd"] * 1000) / df["population_millions"]

    metrics = [
        "population_millions",
        "area_sq_km",
        "density_per_sq_km",
        "literacy_rate",
        "sex_ratio",
        "gdp_billion_usd",
        "gdp_per_capita",
    ]

    corr = df[metrics].corr().abs()
    pairs = (
        corr.where(np.triu(np.ones(corr.shape, dtype=bool), k=1))
        .stack()
        .sort_values(ascending=False)
    )

    print(f"\n  Top {top_n} strongest correlations:")
    for (a, b), val in pairs.head(top_n).items():
        print(f"    {a} <-> {b}: {val:.2f}")


if __name__ == "__main__":
    df = load_data()
    print("\nGenerating correlation plots...")
    plot_correlation_heatmap(df)
    print_strongest_pairs(df)
    print("Done!")
