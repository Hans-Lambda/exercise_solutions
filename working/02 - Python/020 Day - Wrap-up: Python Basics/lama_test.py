# import sys
# from termcolor import cprint, colored
# from colorama import Fore, Back, Style
# import rhinoscript
# from color_constants import colors,RGB  # https://www.webucator.com/article/python-color-constants-module/
#  https://realpython.com/python-ordereddict/
# from colorama import init
from termcolor import colored
def colored_text(r, g, b, text):  # https://www.codegrepper.com/code-examples/python/print+orange+colour+text+python
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)
# Task 1
def Sum(x, y, z):
    return x + y + z
# Task 5
# import time
"""
def random_number(max_of_range):
    for n in range(max_of_range):
        for i in range(max_of_range):
            n = i
    return n
"""
# Task 6
def celsius_to_fahrenheit(celsius):
    return 9/5 * celsius + 32
def fahrenheit_to_celsius(fahrenheit):
    return 5/9 * (fahrenheit - 32)
# Task 8
def fibonacci_ser(n):
    if(n <= 1):
        return n
    else:
        return(fibonacci_ser(n-1) + fibonacci_ser(n-2))
def fibo(num):
  a,b = 0, 1
  for i in range(0, num):
    yield "{}: {}".format(i,a)
    a, b = b, a + b
if __name__ == '__main__':
    # Task 1
    number1 = int(input("Enter the first number >> "))
    number2 = int(input("Enter the second number >> "))
    number3 = int(input("Enter the third number >> "))
    if number1 != number2 != number3:
        print("The sum is ", Sum(number1, number2, number3))
    else:
        print("The triple sum is ", Sum(number1, number2, number3))
    # Task 2
    Number1 = int(input("Enter the first number >> "))
    Number2 = int(input("Enter the second number >> "))
    if Number1 > Number2:
        print("The result of calculation is ", 2 * (Number1 - Number2))
    else:
        print("The result of calculation is ", abs(Number1 - Number2))
    # Task 3
    # have done it before
    #  Task 4
    # done before
    # Task 5 (see the extra code)
    # # set_color = RGB(ORANGE)
    # # print(colored("text", RGB(255, 128, 0)))
    # # print(colored_text(255, 128, 0, 'Hello, World'))
    #
    # # i = random_number((1, 5))
    # # print(i)
    # # random_number((1, 5))
    # # print(i)
    #
    # i = 2
    #
    # # while i in range(1, 4):
    # users_guess = int(input(
    #     "Guess a number between " + colored("1 ", "blue") + "and " + colored("10 ", "blue") + colored_text(255, 128, 0,
    #                                                                                                        "until ") + "you get it right : "))
    # while users_guess is not i:
    #     users_guess = int(input(
    #         "Wrong!Guess a number between " + colored("1 ", "blue") + "and " + colored("10 ", "blue") + colored_text(
    #             255, 128, 0, "until ") + "you get it right : "))
    # print("Well guessed!")
    # ask_to_go_on = input(
    #     (colored("Do you want to try it again?", "blue") + colored("(yes", "green") + colored("/no) ", "red")))
    # if ask_to_go_on == "Yes":  # or "yes" or "y" or "Y":
    #     users_guess = int(input(
    #         "Guess a number between " + colored("1 ", "blue") + "and " + colored("10 ", "blue") + colored_text(255, 128,
    #                                                                                                            0,
    #                                                                                                            "until ") + "you get it right : "))
    #
    # else:
    #     print(colored_text(0, 255, 255, " Okay! See you again soon!"))
    #
    # i += 1
    #
    # for n in range(1, 11):
    #     i = n
    #  Task 6
    scale = input("Enter the scale shortcut you'd like to convert (F - Fahrenheit, C - Celsius: ")
    temp = float(input("Input the value of temperature you'd like to convert "))
    if scale == "C" or scale == "c":
        print("The temperature " + colored_text(255, 128, 0,
                                                "in ") + "Fahrenheit is " + colored(celsius_to_fahrenheit(temp), "blue") + " degrees.")
    else:
        print("The temperature " + colored_text(255, 128, 0,
                                                "in ") + "Fahrenheit is " + colored(fahrenheit_to_celsius(temp), "blue") + " degrees.")
    #  Task 7
    for i in range(5):
        print(colored(i * "* ", "red"))
    for i in range(5, 0, -1):
        print(colored(i * "* ", "red"))
    #  Task 8
    n =int(input("Enter the items number: "))
    print("Fibonacci sequence:")
    # Version 1 A
    i = 0
    print(i)
    j = 1
    print(j)
    while i in range(34):
        i = i + j
        print(i)
        j = j + i
        print(j)
     # Version 1 B
    # i = 0
    # count =0
    # print(count, i)
    # j = 1
    # count = 1
    # print(count, j)
    # if n%2 ==0:
    #     for count in range(2,n,2):
    #         i = i + j
    #         print(count, i)
    #         j = j + i
    #         print(count +1,j)
    # else:
    #     for count in range(n,2,-2):
    #         i = i + j
    #         print(n+2-count, i)
    #         j = j + i
    #         print(n+3-count,j)
    # Version 2
    i, j = 0,1
    for count in range(n):
        print(i)
        i, j = j, i +j
    # Version 3
    n = int(input("Enter number of terms:"))
    print("Fibonacci sequence:")
    for i in range(n):
        print(fibonacci_ser(i))
    # Version 4
    for item in fibo(10):
        print (item)