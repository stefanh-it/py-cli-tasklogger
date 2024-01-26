import datetime
import time
import typer

# from datetime import timedelta
# delta = timedelta(
#     days=50,
#     seconds=27,
#     microseconds=10,
#     milliseconds=29000,
#     minutes=5,
#     hours=8,
#     weeks=2
# )

class Task():
    duration = 0
    start_time = 0
    end_time = 0
    def __init__(self, title):
        self.title = title
        print(self.title)

    def start_task(self):
        print(f'Start {self.title} at:')
        self.start_time = datetime.datetime.now()
        print(self.start_time)

    def end_task(self):
        print(f'Stop {self.title} at:')
        self.end_time = datetime.datetime.now()
        print(self.end_time)
        if self.end_time != self.start_time:
            duration = self.end_time - self.start_time

def main(title):
    x = Task(title)
    x.start_task()
    time.sleep(1)
    x.end_task()

if __name__ == "__main__":  
    typer.run(main)
