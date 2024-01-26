import datetime
import typer

class Task():
    duration = 0
    start_time = 0
    def __init__(self, title):
        self.title = title
        
        

def main(name: str):
    print(f"Hi {name}")

if __name__ == "__main__":
    typer.run(main)
