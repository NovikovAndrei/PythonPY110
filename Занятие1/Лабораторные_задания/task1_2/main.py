def task() -> int:
    list_words = [
        "Goldenrod",
        "Purple",
        "Salmon",
        "Turquoise",
        "Cyan"
    ]
    return max(map(len, list_words))
    # return len(max(list_words))   Не понимаю, почему нельзя обойтись без "map"?


if __name__ == "__main__":
    print(task())
