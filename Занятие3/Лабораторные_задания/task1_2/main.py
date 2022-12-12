OUTPUT_FILE = "output.txt"


def task():
    with open(OUTPUT_FILE, "w") as f:   # TODO записать лесенку в файл
        for _ in range(1,11):
            print(" " * (10 - _) + '*' * _)

if __name__ == "__main__":
    task()

    with open(OUTPUT_FILE) as file:
        for line in file:
            print(line, end="")
