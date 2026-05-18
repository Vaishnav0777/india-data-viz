"""Plot top and bottom 5 states across key metrics."""

import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path
from analyze import load_data


def plot_top_bottom(df):
    metrics = {
        "literacy_rate": "Literacy Rate (%)",
        "gdp_billion_usd": "GDP (Billion USD)",
        "sex_ratio": "Sex Ratio",
        "density_per_sq_km": "Pop. Density (per sq km)",
    }
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle("Top 5 vs Bottom 5 States", fontsize=16, fontweight="bold", y=1.02)
    for ax, (col, label) in zip(axes.flat, metrics.items()):
        top5 = df.nlargest(5, col).sort_values(col)
        bot5 = df.nsmallest(5, col).sort_values(col)
        combined = pd.concat([bot5, top5])
        colors = ["#e74c3c"] * 5 + ["#2ecc71"] * 5
        ax.barh(combined["state"], combined[col], color=colors)
        ax.set_xlabel(label)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
    plt.tight_layout()
    output = Path(__file__).parent.parent / "plots" / "top_bottom_comparison.png"
    plt.savefig(output, dpi=150, bbox_inches="tight")
    print(f"  Saved: {output}")
    plt.close()


if __name__ == "__main__":
    df = load_data()
    plot_top_bottom(df)
    print("Done!")
