import sqlite3
from lib import CONN, CURSOR

class Employee:
    # Existing code for Employee class

    def reviews(self):
        from lib.models.review import Review  # Import within the method to avoid circular imports
        CURSOR.execute("SELECT * FROM reviews WHERE employee_id = ?", (self.id,))
        rows = CURSOR.fetchall()
        return [Review.instance_from_db(row) for row in rows]
