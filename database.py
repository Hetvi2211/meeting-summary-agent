import sqlite3

def save_to_db(summary):
    conn = sqlite3.connect("meeting_summaries.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS summaries(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        summary TEXT
    )
    """)

    cursor.execute(
        "INSERT INTO summaries(summary) VALUES(?)",
        (summary,)
    )

    conn.commit()
    conn.close()


def get_all_summaries():
    conn = sqlite3.connect("meeting_summaries.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS summaries(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        summary TEXT
    )
    """)

    cursor.execute("""
    SELECT id, summary
    FROM summaries
    ORDER BY id DESC
    """)

    summaries = cursor.fetchall()

    conn.close()

    return summaries