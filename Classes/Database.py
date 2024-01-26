import sqlite3

class Database():
    db_name = 'tasks.db'

    def __init__(self, db_name):
        self.db_name = db_name
        self.db_init()

    def db_connect(self):
        conn = sqlite3.connect(self.db_name)
        return conn


    def db_init(self):
        conn = self.db_connect()
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
            duration TEXT
            start_time TEXT
            end_time TEXT
            is_tracking INTEGER
            )
        ''')
        print('Database initialized')

        # Commit the changes to the database
        conn.commit()

        # Close the cursor and connection
        cursor.close()
        conn.close()

