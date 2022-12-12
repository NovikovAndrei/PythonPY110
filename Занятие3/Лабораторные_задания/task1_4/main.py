INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


def task():
    ...  # TODO перезаписать содержимое одного файла в другой
    with open(INPUT_FILE, "r") as in_f:
        with open(OUTPUT_FILE, "w") as o_f:
            for upper_line in map(str.upper, in_f):
                o_f.write(upper_line)
    # Возможен ли такой вариант решения задачи?
    #with open(OUTPUT_FILE, "w") as o_f:
        #with open(INPUT_FILE, "r") as in_f:
            #for line in in_f:
                #line = line.rstrip().upper() + '\n'
                #o_f.write(line)

if __name__ == "__main__":
    task()

    with open(OUTPUT_FILE) as file:
        for line in file:
            print(line, end="")
