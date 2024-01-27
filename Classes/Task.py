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
import datetime
import sys
from Classes.Database import Database as db


class Task():
    duration = 0
    start_time = 0
    end_time = 0
    is_tracking = False
    database = db()

    def __init__(self, title):
        self.title = title
        print(f"Creating task: {self.title}")
        self.database.insert_task(self.title, "0", "0", "0", 0)

        # print("Unexpected error:", sys.exc_info()[0])

    def start_task(self):
        print(f'Start {self.title} at:')
        if self.is_tracking is False:
            self.start_time = datetime.datetime.now()
            self.is_tracking = True
            print(self.start_time)
        else:
            print('Task is already tracking')

    def end_task(self):
        print(f'Stop {self.title} at:')
        if self.is_tracking is True:
            self.end_time = datetime.datetime.now()
            self.is_tracking = False
            print(self.end_time)
            duration = self.end_time - self.start_time
            print(f"Duration: {str(duration)}")
        else:
            print('Task is not tracking')

#    def __check_if_task_exists(self):


if __name__ == "__main__":
    Task('**args')
