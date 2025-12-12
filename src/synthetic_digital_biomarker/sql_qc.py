import sqlite3
import pandas as pd
import os

def run_sql_qc(db_path="data/biomarker.db"):
    conn = sqlite3.connect(db_path)

    print("\n🔍 Running SQL QC Checks...")

    checks = {}

    # 1. Check for NULLs
    checks["null_steps"] = pd.read_sql_query(
        "SELECT COUNT(*) AS nulls FROM steps WHERE steps IS NULL;", conn)

    checks["null_reaction_time"] = pd.read_sql_query(
        "SELECT COUNT(*) AS nulls FROM cognitive_tests WHERE reaction_time IS NULL;", conn)

    # 2. Check for impossible ranges
    checks["invalid_steps"] = pd.read_sql_query(
        "SELECT COUNT(*) AS invalid FROM steps WHERE steps < 0 OR steps > 100000;", conn)

    checks["invalid_rt"] = pd.read_sql_query(
        "SELECT COUNT(*) AS invalid FROM cognitive_tests WHERE reaction_time < 50 OR reaction_time > 2000;", conn)

    # 3. Check for duplicates
    checks["duplicate_rows"] = pd.read_sql_query(
        """
        SELECT user_id, day, COUNT(*) AS cnt
        FROM steps
        GROUP BY user_id, day
        HAVING cnt > 1;
        """, conn)

    # Save QC Results
    os.makedirs("data/qc", exist_ok=True)
    qc_file = "data/qc/sql_qc_results.txt"

    with open(qc_file, "w") as f:
        for name, df in checks.items():
            f.write(f"\n--- {name} ---\n")
            f.write(df.to_string(index=False))
            f.write("\n")

    print(f"✅ SQL QC complete → {qc_file}")

    conn.close()
