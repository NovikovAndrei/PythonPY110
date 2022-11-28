from itertools import repeat


def task(list_args: list, type:callable = int) -> bool:
    return all(map(isinstance, list_args, repeat(type)))


if __name__ == "__main__":
    print(task([1, 2, 3], int))
    print(task(["str", "2", "3"], str))
