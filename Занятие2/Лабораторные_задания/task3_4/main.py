def make_string_upper(fn):
    def wrapper():
        # TODO перевести результат исходной функции в верхний регистр
        return fn().upper()
        # обязательно ли создавать переменную (как сделано в решении)
        # и к ней уже применять ".upper()",
        # если можно применить метод к самой функции (в данном случае)?
    return wrapper


@make_string_upper
def get_text() -> str:
    return "Hello, World!!!"


if __name__ == "__main__":
    print(get_text())
