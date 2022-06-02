

nope = "Hey, try again!"
yea = "Thank you!"
password = input("What is your password: ")
# version 1
our_secret_password = "123445"  # global
second_password = "111"
third_password = "slow"
# comparing
# is the password the user typed the same as our secret password
is_correct_password = password == our_secret_password or password == second_password or password == third_password  # system password!

if not is_correct_password:
    print(nope)
else:
    print(yea)

# # version 2
# if not password == our_secret_password:
#     print(nope)
# else:
#     print(yea)
#
# # version 3
# if password == our_secret_password:
#     print(yea)
# else:
#     print(nope)
