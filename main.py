import stack
from stack import *


def append():
    length = int(input("Enter length of list: "))

    array = []

    for i in range(length):
        a = int(input(f"Enter {i + 1} element: "))
        stacks.append(a)

    stack.main()


if __name__ == "__main__":
    append()
