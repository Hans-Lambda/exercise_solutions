# password = "abcd"
password = input("What is your password")
# version 1
our_secret_password = "123445" # global 
second_password = "111"
# comparing 
# is the password the user typed the same as our secret password
is_correct_password = password == our_secret_password or password == second_password # system password!
if not is_correct_password:
    print("Hey, try again!")
else:
    print("Thank you!")

# version 2
if not password == our_secret_password:
    print("Hey, try again!")
else:
    print("Thank you!")

# version 3
if password == our_secret_password:
    print("Thank you!")
else:
    print("Hey, try again!")
