import sqlite3
import time
import typer
from Classes.Task import Task

app = typer.Typer()


task = Task(title='')

@app.command()
def start(title: str):
    task.start_task()
    print(task.title)

@ app.command()
def stop(title: str):
    task.end_task()
    print(task.duration)

def main(title):
    x = Task(title)
    x.start_task()
    time.sleep(1)
    x.end_task()

if __name__ == "__main__":  
    app()
