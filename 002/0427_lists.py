import sys
import random


students = ["Alex", "Peter", "Bilel", "Hugo", "Ikoro"]

for fuck in students:
    print(fuck)

index = 0
while index < len(students):
    print(students[index])
    index += 1


indexx = 0
while indexx < 3:
    print(students[2])
    indexx += 1


def is_odd(n):
    if n % 2 == 0:
        return False
    else:
        return True


a = 0
b = 0


# random.random() generates a random number between 0 and 1
while a < 0.9 and b < 10:
    b += 1
    a = random.random()
print(b)


username = input("Input username: ")
password = input("Input password: ")
count = 0
while password != "pw" and username != "admin":
    print("Try again!")
    username = input("Input username: ")
    password = input("Input password: ")
    count += 1

    if count > 3:
        print("Three times wrong password. Try again later")
        sys.exit()
