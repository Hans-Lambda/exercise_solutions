# ( ) # parentheses
# { } # curly braces 
# [ ] # square brackets
students = ["Alex", "Petter", "Bilel", "Hugo", "Ikoro"]  # student IDs.
# get the first student out of this
# 1 million students
# print(students[0])
# print(students[1])
# print(students[2])
# print(students[3])
# print(students[4])
# for st in students:
#     print(st)

# While loop 
# index = 0
# 0 < 5 ==> true?? -- 5.
# while index < len(students):
#     print(students[index])
#     index = index + 1
#     # KEEP DOING THE CODE until CONDITION --> turns FALSE

# ############ PSEUDOCODE ######### (won't work!)
# while CONDITIONAL:
    # KEEP RUNNING THE CODE BELOW IT 

# import random
# a = 0
# b = 0

# def isOdd(n):
#     if n % 2 == 0:
#         return False
#     else:
#         return True
# # even numbers are multiples of 2
# # a number divisible by 2 / remainder
# # Modulo!!

# while a < 0.9 and b < 10:
#     b = b + 1
#     a = random.random()
# print(b)

# password = input("What is your password?")
# username = input("What is your user?")
# count = 1
# import sys
# while password != "xyza" and username != "admin":
#     print("Try again!")
#     password = input("What is your password?")
#     username = input("What is your user?")

#     if count < 2:
#         print("You have your limit!")
#         sys.exit() # break!!
#     else:
#         print(count, '@@@count')
#         count += 1

# # you never reach if you 46 is not "false!!"
# # THis is your "else"
# print("You have logged in")


password = input("What is your password?")
# NOT TRUE??? or NOT FALSE -> NOT FALSEY ? True
while not password:
    print("Try again, you cannot put an empty password", password)
    password = input("What is your password?")

while password == "1":
    print("Try again, you cannot put ", password)

if password == "abcd":    
    print("Welcome")
else:
    print("You are wrong! You cannot put ", password)


value = ""
if value:
    print("This is printed when TRUE")
else:
    print("This is printed when FALSE")
####
# 0, "", [], {}    