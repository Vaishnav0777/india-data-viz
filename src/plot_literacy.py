"""Plot literacy rate analysis across Indian states."""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from pathlib import Path
from analyze import load_data


def plot_literacy_bar(df: pd.DataFrame) -> None:
    """Bar chart of literacy rates with a national average line."""
    df_sorted = df.sort_values("literacy_rate", ascending=True)
    avg = df["literacy_rate"].mean()

    fig, ax = plt.subplots(figsize=(10, 12))

    colors = ["#e74c3c" if rate < avg else "#2ecc71" for rate in df_sorted["literacy_rate"]]
    ax.barh(df_sorted["state"], df_sorted["literacy_rate"], color=colors)
    ax.axvline(avg, color="#333", linestyle="--", linewidth=1.5, label=f"Average: {avg:.1f}%")

    ax.set_xlabel("Literacy Rate (%)", fontsize=12)
    ax.set_title("Literacy Rate by State", fontsize=16, fontweight="bold", pad=20)
    ax.legend(fontsize=11)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.tight_layout()
    output = Path(__file__).parent.parent / "plots" / "literacy_bar.png"
    output.parent.mkdir(exist_ok=True)
    plt.savefig(output, dpi=150, bbox_inches="tight")
    print(f"  Saved: {output}")
    plt.close()


def plot_literacy_by_region(df: pd.DataFrame) -> None:
    """Box plot of literacy rates grouped by region."""
    fig, ax = plt.subplots(figsize=(10, 6))

    region_order = df.groupby("region")["literacy_rate"].median().sort_values(ascending=False).index
    sns.boxplot(data=df, x="region", y="literacy_rate", order=region_order, hue="region", palette="viridis", legend=False, ax=ax)
    sns.stripplot(data=df, x="region", y="literacy_rate", order=region_order,
                  color="black", size=5, alpha=0.5, ax=ax)

    ax.set_xlabel("Region", fontsize=12)
    ax.set_ylabel("Literacy Rate (%)", fontsize=12)
    ax.set_title("Literacy Rate Distribution by Region", fontsize=14, fontweight="bold")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.tight_layout()
    output = Path(__file__).parent.parent / "plots" / "literacy_region_box.png"
    plt.savefig(output, dpi=150, bbox_inches="tight")
    print(f"  Saved: {output}")
    plt.close()


if __name__ == "__main__":
    df = load_data()
    print("\nGenerating literacy plots...")
    plot_literacy_bar(df)
    plot_literacy_by_region(df)
    print("Done!")
