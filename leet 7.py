import random
def HelloWorld():
    correct = ["H", "e", "l", "l", "o", " ", "W", "o", "r", "l", "d"]
    lst = []
    num = random.randint(32, 127)
    print(chr(num))
    for i in correct:
        while chr(num) != i:
            num = random.randint(32, 127)
            print(chr(num))
        lst.append(chr(num))
        print("".join(lst))

    return "".join(lst)


HelloWorld()
