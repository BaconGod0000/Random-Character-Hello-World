import random as r
import time as t

def run():

    # initialises variables
    text,i = input("give text: "),0
    n = len(text)

    # main loop
    while i < n:
        j = chr(r.randint(32, 127))
        print(text[:i] + j)
        if j == text[i]: i += 1
        t.sleep(1/100)

run() # driver code