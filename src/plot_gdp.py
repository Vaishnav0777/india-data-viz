"""Plot GDP analysis across Indian states."""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from pathlib import Path
from analyze import load_data


def plot_gdp_bar(df: pd.DataFrame) -> None:
    """Top 10 states by GDP."""
    top10 = df.nlargest(10, "gdp_billion_usd").sort_values("gdp_billion_usd", ascending=True)

    fig, ax = plt.subplots(figsize=(10, 7))
    colors = sns.color_palette("Blues_d", n_colors=len(top10))
    ax.barh(top10["state"], top10["gdp_billion_usd"], color=colors)

    for i, val in enumerate(top10["gdp_billion_usd"]):
        ax.text(val + 2, i, f"${val:.0f}B", va="center", fontsize=10)

    ax.set_xlabel("GDP (Billion USD)", fontsize=12)
    ax.set_title("Top 10 Indian States by GDP", fontsize=16, fontweight="bold", pad=20)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.tight_layout()
    output = Path(__file__).parent.parent / "plots" / "gdp_top10.png"
    output.parent.mkdir(exist_ok=True)
    plt.savefig(output, dpi=150, bbox_inches="tight")
    print(f"  Saved: {output}")
    plt.close()


def plot_gdp_vs_population(df: pd.DataFrame) -> None:
    """Scatter plot of GDP vs population with regression line."""
    fig, ax = plt.subplots(figsize=(10, 7))

    sns.regplot(data=df, x="population_millions", y="gdp_billion_usd",
                scatter_kws={"s": 80, "alpha": 0.7}, line_kws={"color": "red"}, ax=ax)

    for _, row in df.iterrows():
        if row["gdp_billion_usd"] > 100 or row["population_millions"] > 80:
            ax.annotate(row["state"], (row["population_millions"], row["gdp_billion_usd"]),
                       fontsize=8, ha="left", va="bottom")

    ax.set_xlabel("Population (millions)", fontsize=12)
    ax.set_ylabel("GDP (Billion USD)", fontsize=12)
    ax.set_title("GDP vs Population — Indian States", fontsize=14, fontweight="bold")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.tight_layout()
    output = Path(__file__).parent.parent / "plots" / "gdp_vs_population.png"
    plt.savefig(output, dpi=150, bbox_inches="tight")
    print(f"  Saved: {output}")
    plt.close()


def plot_gdp_per_capita(df: pd.DataFrame) -> None:
    """GDP per capita comparison."""
    df = df.copy()
    df["gdp_per_capita"] = (df["gdp_billion_usd"] * 1000) / df["population_millions"]
    df_sorted = df.sort_values("gdp_per_capita", ascending=True)

    fig, ax = plt.subplots(figsize=(10, 12))
    colors = sns.color_palette("RdYlGn", n_colors=len(df_sorted))
    ax.barh(df_sorted["state"], df_sorted["gdp_per_capita"], color=colors)

    ax.set_xlabel("GDP per Capita (USD)", fontsize=12)
    ax.set_title("GDP per Capita by State", fontsize=16, fontweight="bold", pad=20)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.tight_layout()
    output = Path(__file__).parent.parent / "plots" / "gdp_per_capita.png"
    plt.savefig(output, dpi=150, bbox_inches="tight")
    print(f"  Saved: {output}")
    plt.close()


if __name__ == "__main__":
    df = load_data()
    print("\nGenerating GDP plots...")
    plot_gdp_bar(df)
    plot_gdp_vs_population(df)
    plot_gdp_per_capita(df)
    print("Done!")
