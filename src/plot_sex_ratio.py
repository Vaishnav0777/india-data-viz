"""Plot sex ratio analysis across Indian states."""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from pathlib import Path
from analyze import load_data


def plot_sex_ratio(df: pd.DataFrame) -> None:
    """Horizontal bar chart of sex ratio with the 1000 baseline."""
    df_sorted = df.sort_values("sex_ratio", ascending=True)

    fig, ax = plt.subplots(figsize=(10, 12))
    colors = ["#e74c3c" if ratio < 950 else "#f39c12" if ratio < 1000 else "#2ecc71"
              for ratio in df_sorted["sex_ratio"]]

    ax.barh(df_sorted["state"], df_sorted["sex_ratio"], color=colors)
    ax.axvline(1000, color="#333", linestyle="--", linewidth=1.5, label="Equal ratio (1000)")
    ax.axvline(df["sex_ratio"].mean(), color="#3498db", linestyle=":", linewidth=1.5,
               label=f"Average: {df['sex_ratio'].mean():.0f}")

    ax.set_xlabel("Sex Ratio (females per 1000 males)", fontsize=12)
    ax.set_title("Sex Ratio by State", fontsize=16, fontweight="bold", pad=20)
    ax.legend(fontsize=10)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.tight_layout()
    output = Path(__file__).parent.parent / "plots" / "sex_ratio.png"
    output.parent.mkdir(exist_ok=True)
    plt.savefig(output, dpi=150, bbox_inches="tight")
    print(f"  Saved: {output}")
    plt.close()


def plot_sex_ratio_vs_literacy(df: pd.DataFrame) -> None:
    """Scatter plot exploring correlation between literacy and sex ratio."""
    fig, ax = plt.subplots(figsize=(10, 7))

    sns.regplot(data=df, x="literacy_rate", y="sex_ratio",
                scatter_kws={"s": 80, "alpha": 0.7}, line_kws={"color": "red"}, ax=ax)

    for _, row in df.iterrows():
        if row["sex_ratio"] > 1000 or row["sex_ratio"] < 900 or row["literacy_rate"] > 88:
            ax.annotate(row["state"], (row["literacy_rate"], row["sex_ratio"]),
                       fontsize=8, ha="left")

    ax.set_xlabel("Literacy Rate (%)", fontsize=12)
    ax.set_ylabel("Sex Ratio (per 1000 males)", fontsize=12)
    ax.set_title("Does Literacy Correlate with Sex Ratio?", fontsize=14, fontweight="bold")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.tight_layout()
    output = Path(__file__).parent.parent / "plots" / "sex_ratio_vs_literacy.png"
    plt.savefig(output, dpi=150, bbox_inches="tight")
    print(f"  Saved: {output}")
    plt.close()


if __name__ == "__main__":
    df = load_data()
    print("\nGenerating sex ratio plots...")
    plot_sex_ratio(df)
    plot_sex_ratio_vs_literacy(df)
    print("Done!")
