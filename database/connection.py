"""
Database connection module.
"""

import sqlite3
from config.settings import DATABASE_NAME


def get_connection():
    """
    Return SQLite database connection.
    """
    return sqlite3.connect(DATABASE_NAME)