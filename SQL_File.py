import psycopg2
from psycopg2.extras import RealDictCursor


class DatabaseManager:
    def __init__(self):
        self.config = {
            "host": "db.klcbzywmjdkeuvqmorkx.supabase.co",
            "port": 5432,
            "user": "postgres.klcbzywmjdkeuvqmorkx",
            "password": "mobjeH-jewmom-kewde0",
            "dbname": "postgres",
            "sslmode": "require"
        }
        self.connection = None

    def _get_connection(self):
        if self.connection is None or self.connection.closed != 0:
            self.connection = psycopg2.connect(**self.config)
        return self.connection

    def execute_query(self, command, params=None):
        conn = self._get_connection()

        try:
            with conn.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute(command, params)

                if command.strip().upper().startswith("SELECT"):
                    return cursor.fetchall()
                else:
                    conn.commit()
                    return cursor.rowcount

        except Exception as e:
            conn.rollback()
            print("Database error:", e)
            return None

    def disconnect(self):
        if self.connection and self.connection.closed == 0:
            self.connection.close()
            self.connection = None


db = DatabaseManager()