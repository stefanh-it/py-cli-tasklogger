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
    task_id: int
    duration = 0
    start_time = 0
    end_time = 0
    is_tracking = False
    database = db()

    def __init__(self, title):
        self.title = title

        # print("Unexpected error:", sys.exc_info()[0])

    def create_task(self):
        print(f"Creating task: {self.title}")
        self.database.insert_task(self.title, "0", "0", "0", 0)

    def start_task(self, title):
        print(f'checking for {title}')
        self.database.read_task_by_title(title)
        print(f'Start {title} at:')
        self.database.update_task('Title1', '10', '10', '10', 0, 2)
        # if self.is_tracking is False:
        #     self.start_time = datetime.datetime.now()
        #     self.is_tracking = True
        #     print(self.start_time)
        # else:
        #     print('Task is already tracking')

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

    def getTask(self):
        self = self.database.create_task_from_db(self.title)
        print("from task class" + str(self))
        return self
#    def_check_if_task_exists(self):


if __name__ == "__main__":
    Task('**args')
