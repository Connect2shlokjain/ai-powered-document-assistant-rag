import sqlite3
from datetime import datetime

from app.utils.config import settings


class HistoryService:
    """
    Service responsible for storing and retrieving chat history.
    """

    def __init__(self):
        self.db_path = settings.DATABASE_URL.replace("sqlite:///", "")
        self._create_table()

    def _connect(self):
        return sqlite3.connect(self.db_path)

    def _create_table(self):
        conn = self._connect()
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS chat_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                question TEXT NOT NULL,
                answer TEXT NOT NULL,
                created_at TEXT NOT NULL
            )
        """)

        conn.commit()
        conn.close()

    def save_chat(self, question: str, answer: str):
        """
        Save a question-answer pair.
        """

        conn = self._connect()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO chat_history
            (question, answer, created_at)
            VALUES (?, ?, ?)
            """,
            (
                question,
                answer,
                datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            )
        )

        conn.commit()
        conn.close()

    def get_history(self):
        """
        Retrieve complete chat history.
        """

        conn = self._connect()
        conn.row_factory = sqlite3.Row

        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM chat_history
            ORDER BY id DESC
        """)

        rows = cursor.fetchall()

        conn.close()

        return [dict(row) for row in rows]

    def clear_history(self):
        """
        Delete all chat history.
        """

        conn = self._connect()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM chat_history")

        conn.commit()
        conn.close()