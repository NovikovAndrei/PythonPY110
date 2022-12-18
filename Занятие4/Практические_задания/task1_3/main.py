import re


def task():
    emails = "abc.test@gmail.com, xyz@test.in, test.first@analyticsvidhya.com, first.test@rest.biz"

    #email_pattern = re.compile(r"(?P<domen>(?<=@)\w+\.\w+)")  # TODO используйте запоминающие группы
    #email_pattern = re.compile(r"(?<=@)\w+\.\w+")
    email_pattern = re.compile(r"@(?:\w+)\.(?:\w+)")
    print(email_pattern.findall(emails))


if __name__ == "__main__":
    task()
