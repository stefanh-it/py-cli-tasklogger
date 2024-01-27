import time
import typer
from Classes.Task import Task
from Classes.Database import Database as db

app = typer.Typer()

# Initialize Task object


@app.command()
def create(title: str):
    task = Task(title)


@app.command()
def start(title: str):
    """Start a new task."""
    task.start_task()
    print(task.title)


@ app.command()
def stop(title: str):
    """Stop the current task."""
    task.end_task()
    print(task.duration)


@app.command()
def testdb():
    """Test the database."""
    first_db = db()
    print(first_db.get_connection())


@app.command()
def create_test():
    first_db = db()
    first_db.insert_task(title="Test Task", duration="0",
                         start_time="0", end_time="0", is_tracking=0)


@app.command()
def readtestdb():
    first_db = db()
    first_db.db_read()


def main(title):
    x = Task(title)
    x.start_task()
    time.sleep(1)
    x.end_task()


if __name__ == "__main__":
    app()
