from database.connection import get_connection


def create_database():
    """
    Create database tables if they don't exist.
    """

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS email_logs(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            gmail_id TEXT UNIQUE,

            sender TEXT,

            subject TEXT,

            received_time TEXT,

            category TEXT,

            status TEXT
        )
    """)

    connection.commit()
    connection.close()

    print("✅ Database Ready")