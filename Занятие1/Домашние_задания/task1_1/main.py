from itertools import count
def enumerate_(elements, start=0):
    return zip(count(start, 1), elements)
    # или лучше так? return zip(range(start, len(elements) + start), elements)



if __name__ == "__main__":
    for i, val in enumerate_(range(10), 4):
        print(i, val)

