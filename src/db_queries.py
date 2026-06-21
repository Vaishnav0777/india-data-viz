"""
Run analytical SQL queries against the states SQLite database.
Assumes db_loader.py has been run to build data/india_states.db.
"""
from pathlib import Path
import sqlite3

ROOT = Path(__file__).resolve().parent.parent
DB = ROOT / "data" / "india_states.db"

QUERIES = {
    "Top 5 states by GDP": """
        SELECT state, gdp_billion_usd
        FROM states ORDER BY gdp_billion_usd DESC LIMIT 5
    """,
    "Top 5 by GDP per capita": """
        SELECT state, ROUND(gdp_per_capita, 1) AS gdp_per_capita
        FROM states ORDER BY gdp_per_capita DESC LIMIT 5
    """,
    "Regional averages": """
        SELECT region,
               COUNT(*) AS states,
               ROUND(AVG(literacy_rate), 1) AS avg_literacy,
               ROUND(SUM(gdp_billion_usd), 1) AS total_gdp
        FROM states GROUP BY region ORDER BY total_gdp DESC
    """,
    "Highest literacy states": """
        SELECT state, literacy_rate
        FROM states ORDER BY literacy_rate DESC LIMIT 5
    """,
}


def run():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    for title, sql in QUERIES.items():
        print(f"\n{title}")
        print("-" * len(title))
        for row in cur.execute(sql).fetchall():
            print("  " + "  ".join(str(c) for c in row))
    conn.close()


if __name__ == "__main__":
    run()
