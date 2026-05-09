"""Plot population density analysis."""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from pathlib import Path
from analyze import load_data


def plot_density_bar(df: pd.DataFrame) -> None:
    """Bar chart of population density."""
    df_sorted = df.sort_values("density_per_sq_km", ascending=True)

    fig, ax = plt.subplots(figsize=(10, 12))
    colors = sns.color_palette("magma", n_colors=len(df_sorted))
    ax.barh(df_sorted["state"], df_sorted["density_per_sq_km"], color=colors)

    ax.set_xlabel("Population Density (per sq km)", fontsize=12)
    ax.set_title("Population Density — Indian States", fontsize=16, fontweight="bold", pad=20)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.tight_layout()
    output = Path(__file__).parent.parent / "plots" / "density_bar.png"
    output.parent.mkdir(exist_ok=True)
    plt.savefig(output, dpi=150, bbox_inches="tight")
    print(f"  Saved: {output}")
    plt.close()


def plot_area_vs_density(df: pd.DataFrame) -> None:
    """Scatter plot of area vs density."""
    fig, ax = plt.subplots(figsize=(10, 7))

    scatter = ax.scatter(df["area_sq_km"], df["density_per_sq_km"],
                         s=df["population_millions"] * 3, alpha=0.6,
                         c=df["population_millions"], cmap="YlOrRd", edgecolors="black", linewidth=0.5)

    for _, row in df.iterrows():
        if row["density_per_sq_km"] > 500 or row["area_sq_km"] > 250000:
            ax.annotate(row["state"], (row["area_sq_km"], row["density_per_sq_km"]),
                       fontsize=8, ha="left")

    plt.colorbar(scatter, label="Population (millions)")
    ax.set_xlabel("Area (sq km)", fontsize=12)
    ax.set_ylabel("Density (per sq km)", fontsize=12)
    ax.set_title("Area vs Density — Bubble Size = Population", fontsize=14, fontweight="bold")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.tight_layout()
    output = Path(__file__).parent.parent / "plots" / "area_vs_density.png"
    plt.savefig(output, dpi=150, bbox_inches="tight")
    print(f"  Saved: {output}")
    plt.close()


if __name__ == "__main__":
    df = load_data()
    print("\nGenerating density plots...")
    plot_density_bar(df)
    plot_area_vs_density(df)
    print("Done!")
