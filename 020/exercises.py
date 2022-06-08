import math
import random
import sys

# https://github.com/mathiasbrito-dci/python-course-2022/blob/main/02%20-%20Python/021%20Day%20-%20Wrap-up:%20Python%20Basics/EXERCISE.md

# Task 1 - calculate sum
# Your task is to write a Python program to calculate the sum of three integers given (prompted) by user.
# If the values are equal then calculate triple value of their sum.

def calculate_sum():
    xyz = []
    for number in range(3):
        numb = int(input("Type number: "))
        xyz.append(numb)

    print(3 * sum(xyz)) if xyz[0] == xyz[1] == xyz[2] else print(sum(xyz))


# Task 2 - get the difference
# Your task is to write a Python program to get the difference between a two given numbers (prompted by user).
# If the first number is greater than second then calculate double difference between numbers.
# Otherwise calculate the absolute difference between numbers.

def difference():
    xyz = []
    for number in range(2):
        numb = int(input("Type number: "))
        xyz.append(numb)

    print(2 * abs(xyz[0] - xyz[1])) if xyz[0] > xyz[1] else print(abs(xyz[0] - xyz[1]))

# Task 3 - odd or even number
# Your task is to write a Python program to find whether a given number (prompted from the user) is even or odd.

def odd_even():
    numb = int(input("Type number: "))
    print("Even number") if numb % 2 == 0 else print("Odd number")

# Task 4 - circle area
# Your task is to write a Python program which accepts (prompts) the float radius of a
# circle from the user and compute its area.
# Round the result to two decimals!

def radius():
    numb = float(input("Type number: "))
    print(f"The are of a circle with the radius {numb} is {'{:.2f}'.format(math.pi * numb ** 2)}")

# Task 5 - guess a number
# Your task is to write a Python program to guess a number between 1 to 9.

def guess():
    print("correct number!") if int(input("Type number between 1 and 9 to guess: ")) == (round(random.random() * 10)) else print(f"wrong, try again"), guess()

# Task 6 - Celsius to Fahrenheit conversion
# Your task is to write a Python program to convert temperatures to and from Celsius, Fahrenheit.
# In the centigrade scale, which is also called the Celsius scale, water freezes at 0 degrees and boils at 100 degrees.
# In the Fahrenheit scale, water freezes at 32 degrees and boils at 212 degrees.
# Note : User should be prompted twice:
# to enter a temperature,
# to enter a shortcut for given scale (C for Celsius, F for Fahrenheit).

def conversion():
    temp = float(input("Please type temperature: "))
    scale = input("Please type C for Celsius or F for Fahrenheit to convert: ")
    print(f"The temperature in Celsius is: {(temp * (9/5)) + 32} °F") if scale == "C" else print(f"The temperature in Fahrenheit is: {(temp - 32) * 5/9} °C")

# Task 7 - pattern
# Your task is to write a Python program to construct the following pattern. Upper part should be done in one
# line of code without using a loop.

def pattern():
    for i in range(1, 5):
        print(i * "*")
    for j in range(5, 0, -1):
        print(j * "*")

# Task 8 - Fibonacci series
# Your task is to write a Python program to get the Fibonacci series between 0 to 50.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55

def fibonacci():
    fibo = [0, 1]
    [print(i) for i in [fibo.append(fibo[-1] + fibo[-2]) or x for x in fibo if x <= 50]]

if __name__ == '__main__':

    #calculate_sum()
    #difference()
    #odd_even()
    #radius()
    #guess()
    #conversion()
    #pattern()
    #fibonacci()

