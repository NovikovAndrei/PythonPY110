import json


def task():
    filename = "input.json"
    # TODO считать содержимое JSON файла
    with open(filename) as f:
        obj = json.load(f)

    gen_exr = (i["contains_improvement_appeals"] for i in obj)  # TODO записать выражение-генератор возвращающее значение по ключу contains_improvement_appeals
    return sum(gen_exr)


if __name__ == "__main__":
    print(task())
