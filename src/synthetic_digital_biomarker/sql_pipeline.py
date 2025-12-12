import sqlite3
import pandas as pd
import os

def run_sql_pipeline(db_path="data/biomarker.db"):

    # Ensure folder exists
    os.makedirs("data", exist_ok=True)

    # Connect to SQLite DB
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # -----------------------------
    # 1. Create raw sensor tables
    # -----------------------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS steps (
        user_id INTEGER,
        day TEXT,
        steps INTEGER
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS cognitive_tests (
        user_id INTEGER,
        day TEXT,
        reaction_time REAL,
        memory_score REAL
    );
    """)

    # -----------------------------
    # 2. Insert synthetic data
    # -----------------------------
    steps_df = pd.DataFrame({
        "user_id": [1,1,1,2,2],
        "day": ["2024-01-01","2024-01-02","2024-01-03","2024-01-01","2024-01-02"],
        "steps": [5500, 6200, 7000, 4300, 5000]
    })

    cognitive_df = pd.DataFrame({
        "user_id": [1,1,2,2],
        "day": ["2024-01-01","2024-01-02","2024-01-01","2024-01-02"],
        "reaction_time": [480, 500, 520, 530],
        "memory_score": [72, 70, 68, 69]
    })

    steps_df.to_sql("steps", conn, if_exists="replace", index=False)
    cognitive_df.to_sql("cognitive_tests", conn, if_exists="replace", index=False)

    # -----------------------------
    # 3. Run SQL joins + aggregation
    # -----------------------------
    query = """
    SELECT
        s.user_id,
        s.day,
        s.steps,
        c.reaction_time,
        c.memory_score,
        CASE WHEN c.memory_score < 70 THEN 1 ELSE 0 END AS cognitive_risk
    FROM steps s
    LEFT JOIN cognitive_tests c
        ON s.user_id = c.user_id AND s.day = c.day;
    """

    result = pd.read_sql_query(query, conn)

    # -----------------------------
    # 4. Save cleaned output
    # -----------------------------
    os.makedirs("data/sql_output", exist_ok=True)
    result.to_csv("data/sql_output/merged_sensor_data.csv", index=False)

    print("SQL pipeline complete → data/sql_output/merged_sensor_data.csv")

    conn.close()
