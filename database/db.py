import sqlite3

DATABASE_NAME = "database/smartmail.db"


def create_database():
    """
    Creates the database and email_logs table
    if they don't already exist.
    """

    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS email_logs (

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


def email_exists(gmail_id):
    """
    Returns True if email already exists.
    """

    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute(
        "SELECT gmail_id FROM email_logs WHERE gmail_id=?",
        (gmail_id,)
    )

    result = cursor.fetchone()

    connection.close()

    return result is not None


def save_email(
    gmail_id,
    sender,
    subject,
    received_time,
    category="Unknown",
    status="Pending"
):
    """
    Saves email into database.
    """

    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        INSERT OR IGNORE INTO email_logs
        (
            gmail_id,
            sender,
            subject,
            received_time,
            category,
            status
        )
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        gmail_id,
        sender,
        subject,
        received_time,
        category,
        status
    ))

    connection.commit()

    connection.close()