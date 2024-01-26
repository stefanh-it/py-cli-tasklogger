import time
import typer

def main(name: str):
    print(f"Hi {name}")

if __name__ == "__main__":
    typer.run(main)
