"""Plot population distribution across Indian states."""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from pathlib import Path
from analyze import load_data


def plot_population_bar(df: pd.DataFrame) -> None:
    """Horizontal bar chart of state populations."""
    df_sorted = df.sort_values("population_millions", ascending=True)

    fig, ax = plt.subplots(figsize=(10, 12))

    colors = sns.color_palette("YlOrRd", n_colors=len(df_sorted))
    ax.barh(df_sorted["state"], df_sorted["population_millions"], color=colors)

    ax.set_xlabel("Population (millions)", fontsize=12)
    ax.set_title("Population of Indian States", fontsize=16, fontweight="bold", pad=20)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    # Add value labels
    for i, (val, name) in enumerate(zip(df_sorted["population_millions"], df_sorted["state"])):
        ax.text(val + 1, i, f"{val:.1f}M", va="center", fontsize=8)

    plt.tight_layout()
    output = Path(__file__).parent.parent / "plots" / "population_bar.png"
    output.parent.mkdir(exist_ok=True)
    plt.savefig(output, dpi=150, bbox_inches="tight")
    print(f"  Saved: {output}")
    plt.close()


def plot_population_pie(df: pd.DataFrame) -> None:
    """Pie chart showing top 5 states vs rest."""
    top5 = df.nlargest(5, "population_millions")
    rest = df.nsmallest(len(df) - 5, "population_millions")

    labels = list(top5["state"]) + ["Others"]
    sizes = list(top5["population_millions"]) + [rest["population_millions"].sum()]
    colors = sns.color_palette("Set2", len(labels))

    fig, ax = plt.subplots(figsize=(8, 8))
    wedges, texts, autotexts = ax.pie(
        sizes, labels=labels, autopct="%1.1f%%", colors=colors,
        startangle=90, pctdistance=0.85
    )
    for text in autotexts:
        text.set_fontsize(9)

    ax.set_title("Population Share — Top 5 States vs Rest", fontsize=14, fontweight="bold")
    plt.tight_layout()
    output = Path(__file__).parent.parent / "plots" / "population_pie.png"
    plt.savefig(output, dpi=150, bbox_inches="tight")
    print(f"  Saved: {output}")
    plt.close()


if __name__ == "__main__":
    df = load_data()
    print("\nGenerating population plots...")
    plot_population_bar(df)
    plot_population_pie(df)
    print("Done!")
