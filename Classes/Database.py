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
            id INTEGER PRIMARY KEY,
            title TEXT UNIQUE,
            duration TEXT,
            start_time TEXT,
            end_time TEXT,
            is_tracking INTEGER
            );
        ''')
        print('Database initialized')
        # Commit the changes to the database
        conn.commit()
        # Close the cursor and connection
        cursor.close()
        # self.db_close()

    def db_close(self):
        self.connection.close()
        print('Database closed')

    def get_connection(self):
        return self.connection

    def insert_task(self, title, duration, start_time, end_time, is_tracking):
        conn = self.db_connect()
        cursor = self.connection.cursor()
        try:
            cursor.execute('''
            INSERT INTO tasks (title, duration, start_time, end_time, is_tracking)
            VALUES (?, ?, ?, ?, ?);
            ''', (title, duration, start_time, end_time, is_tracking))
            conn.commit()
            print(f"Finished creating task: {title}")
            self.read_task_by_title(title)
        except sqlite3.IntegrityError as e:
            print(f"Task {title} already exists")
        cursor.close()
        self.db_close()

    def db_read(self):
        conn = self.db_connect()
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT title, duration, start_time, end_time, is_tracking FROM tasks ORDER BY end_time;
            """)
        rows = cursor.fetchall()
        print(rows)

    def read_task_by_title(self, title):
        conn = self.db_connect()
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT id, title, duration, start_time, end_time, is_tracking FROM tasks WHERE title =?
            """, (title,))
        rows = cursor.fetchall()
        print(rows)
