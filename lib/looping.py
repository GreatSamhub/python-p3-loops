#!/usr/bin/env python3

def happy_new_year():
    counter = 10
    while (counter > 0):
        counter -= 1
        print(counter)
    print("Happy New Year!")
    pass


def square_integers(int_list):
    int_list = [i**2 for i in int_list]
    print(int_list)
    pass

def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
    pass
