import sqlite3
from datetime import datetime, timezone

DB_NAME = "bot.db"


def get_connection():
    conn = sqlite3.connect(
        DB_NAME,
        timeout=30,
        check_same_thread=False
    )
    conn.row_factory = sqlite3.Row
    return conn


def get_now():
    return datetime.now(timezone.utc).isoformat()


def init_db():
    conn = get_connection()

    try:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                chat_id INTEGER PRIMARY KEY,
                telegram_username TEXT,
                first_name TEXT,
                user_id TEXT,
                language TEXT DEFAULT 'hi',
                state TEXT NOT NULL DEFAULT 'waiting_for_id',
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL
            )
        """)

        # Add language column if migrating existing database
        try:
            conn.execute("ALTER TABLE users ADD COLUMN language TEXT DEFAULT 'hi'")
        except Exception:
            pass

        conn.commit()

    finally:
        conn.close()


def get_user(chat_id):
    conn = get_connection()

    try:
        return conn.execute(
            "SELECT * FROM users WHERE chat_id = ?",
            (chat_id,)
        ).fetchone()

    finally:
        conn.close()


def create_or_update_user(chat_id, username, first_name, language=None):
    now = get_now()
    conn = get_connection()

    try:
        # Check existing user
        existing = conn.execute("SELECT language FROM users WHERE chat_id = ?", (chat_id,)).fetchone()
        user_lang = language or (existing["language"] if existing and existing["language"] else None)

        conn.execute("""
            INSERT INTO users (
                chat_id,
                telegram_username,
                first_name,
                user_id,
                language,
                state,
                created_at,
                updated_at
            )
            VALUES (?, ?, ?, NULL, ?, 'waiting_for_id', ?, ?)

            ON CONFLICT(chat_id) DO UPDATE SET
                telegram_username = excluded.telegram_username,
                first_name = excluded.first_name,
                language = COALESCE(excluded.language, users.language),
                updated_at = excluded.updated_at
        """, (
            chat_id,
            username,
            first_name,
            user_lang,
            now,
            now
        ))

        conn.commit()

    finally:
        conn.close()


def set_user_language(chat_id, language):
    now = get_now()
    conn = get_connection()

    try:
        conn.execute("""
            UPDATE users
            SET language = ?, updated_at = ?
            WHERE chat_id = ?
        """, (language, now, chat_id))
        conn.commit()

    finally:
        conn.close()


def get_user_language(chat_id) -> str:
    conn = get_connection()

    try:
        row = conn.execute("SELECT language FROM users WHERE chat_id = ?", (chat_id,)).fetchone()
        if row and row["language"]:
            return row["language"]
        return "hi"

    finally:
        conn.close()


def update_user_id(chat_id, user_id):
    now = get_now()
    conn = get_connection()

    try:
        conn.execute("""
            UPDATE users
            SET
                user_id = ?,
                state = 'waiting_for_support',
                updated_at = ?
            WHERE chat_id = ?
        """, (
            user_id,
            now,
            chat_id
        ))

        conn.commit()

    finally:
        conn.close()


def update_state(chat_id, state):
    now = get_now()
    conn = get_connection()

    try:
        conn.execute("""
            UPDATE users
            SET
                state = ?,
                updated_at = ?
            WHERE chat_id = ?
        """, (
            state,
            now,
            chat_id
        ))

        conn.commit()

    finally:
        conn.close()


def delete_user(chat_id):
    conn = get_connection()

    try:
        conn.execute(
            "DELETE FROM users WHERE chat_id = ?",
            (chat_id,)
        )

        conn.commit()

    finally:
        conn.close()