"""
Load the India states CSV into a SQLite database.
Creates a single `states` table with typed columns and a derived
gdp_per_capita field, so downstream queries run against SQL instead of
re-reading the CSV each time.
"""
from pathlib import Path
import sqlite3
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
CSV = ROOT / "data" / "india_states.csv"
DB = ROOT / "data" / "india_states.db"


def build_database():
    df = pd.read_csv(CSV)
    df["gdp_per_capita"] = df["gdp_billion_usd"] * 1000 / df["population_millions"]

    conn = sqlite3.connect(DB)
    df.to_sql("states", conn, if_exists="replace", index=False)

    cur = conn.cursor()
    cur.execute("CREATE INDEX IF NOT EXISTS idx_region ON states(region)")
    conn.commit()

    count = cur.execute("SELECT COUNT(*) FROM states").fetchone()[0]
    print(f"Loaded {count} states into {DB}")
    conn.close()


if __name__ == "__main__":
    build_database()
