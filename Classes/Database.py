import sqlite3


class Database():
    db_name = 'tasks.db'
    connection: sqlite3.Connection

    def __init__(self):
        # self.db_name = db_name
        self.db_init()

    def db_connect(self):
        conn = sqlite3.connect(self.db_name)
        self.connection = conn
        return self.connection

    def db_init(self):
        conn = self.db_connect()
        cursor = self.connection.cursor()
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
        self.db_close()

    def db_close(self):
        self.connection.close()
        print('Database closed')

    def get_connection(self):
        return self.connection
