import os
import pathlib


def main():
    cur_path: str = os.getcwd()
    p = pathlib.Path(cur_path)
    root : str = p.parents[1]
    rpath : str = f"{root}\\requirements.txt"
    try:
        os.system(f"pip install -r {rpath}")
        print("Success!")
    finally:
        input("Done")


if __name__ == "__main__":
    main()
