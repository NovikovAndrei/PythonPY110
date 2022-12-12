import json


def task():
    filename = "input.json"
    # TODO считать содержимое JSON файла
    with open(filename) as f:
        python_obj = json.load(f)
    return max(python_obj, key=lambda x: x["score"])   # TODO найти максимальный элемент по ключу score


if __name__ == "__main__":
    print(task())
