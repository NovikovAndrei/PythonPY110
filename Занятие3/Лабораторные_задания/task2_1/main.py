import json


def task() -> str:
    dict_numbers = {k: k ** 2 for k in range(1,11)}  # TODO c помощью dict comprehension сформировать словарь
    return json.dumps(dict_numbers, indent=4)  # TODO сеализовать словарь в JSON строку


if __name__ == "__main__":
    print(task())
