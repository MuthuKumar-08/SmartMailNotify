from database.connection import get_connection


def email_exists(gmail_id):
    """
    Check whether an email already exists.
    """

    connection = get_connection()

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
    Save email into database.
    """

    connection = get_connection()

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


def show_all_emails():
    """
    Display all emails stored in database.
    """

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            gmail_id,
            sender,
            subject,
            received_time,
            category,
            status
        FROM email_logs
    """)

    rows = cursor.fetchall()

    connection.close()

    if not rows:
        print("\n📭 Database is empty.\n")
        return

    print("\n========== DATABASE ==========\n")

    for row in rows:
        print(f"Gmail ID : {row[0]}")
        print(f"Sender   : {row[1]}")
        print(f"Subject  : {row[2]}")
        print(f"Received : {row[3]}")
        print(f"Category : {row[4]}")
        print(f"Status   : {row[5]}")
        print("-" * 70)