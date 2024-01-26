import time
import typer
from Classes.Task import Task
from Classes.Database import Database as db

app = typer.Typer()

# Initialize Task object
task = Task(title='')


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


def main(title):
    x = Task(title)
    x.start_task()
    time.sleep(1)
    x.end_task()


if __name__ == "__main__":
    app()
