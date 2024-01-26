import datetime
import time
import typer

class Task():
    duration = 0
    start_time = 0
    end_time = 0
    def __init__(self, title):
        self.title = title

    def start_task(self):
        self.start_time = datetime.datetime.now()
        print(self.start_time)

    def end_task(self):
        self.end_time = datetime.date.now()
        print(self.end_time)
        if self.end_time != self.start_time:
            duration = self.end_time - self.start_time
            print(duration)

def main():        
    x = Task('Erste Aufgabe')
    x.start_task()
    time.sleep(5)
    x.end_task()

typer.run(main)
