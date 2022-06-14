# Python basics - Exceptions III

## Coding a calculator

### Context

import re


# In this exercise, your are given code for a program that is a basic calculator. User input is assumed to be a
# mathematical formula that consist of a number, an operator (at least + and -), and another number, **separated by
# white space** (e.g. 1 + 1). Here is the basic code for the calculator:

# ```python
# create a new exception class called "MathematicalError" from BaseException class
class MathematicalError(Exception):
    pass

# write a function called parse_input that parses all the user input according to rules list defined in the exercise text
def parse_input(user_input):
  result = re.findall("\d+\s[*+\/-]\s\d+", user_input)
  if result is False:
    raise MathematicalError
  else:
    return True


# function calculate takes 2 integers and an operation type as an argument
def calculate(n1, op, n2):

  if op == '+':
    return n1 + n2
  if op == '-':
    return n1 - n2
  if op == '*':
    return n1 * n2
  if op == '/':
    return n1 / n2

if __name__ == '__main__':

  while True:
    try:
      user_input = input('>>> ')
      if user_input == 'quit':
        break
      elif parse_input(user_input) is True:
        user_input_sep = user_input.split(" ")
        n1 = float(user_input_sep[0])
        op = user_input_sep[1]
        n2 = float(user_input_sep[2])
        result = calculate(n1, op, n2)
        print(result)

    except:
      raise MathematicalError("Not a valid equation")


# An interaction could look like this (easiest if you run this on Idle):
#
# ```python
# >>> 1 + 1
# 2.0
# >>> 3.2 - 1.5
# 1.7000000000000002
# >>> quit
# ```

### Task

# Your task is to right a function called `parse_input`,that splits user input using `str.split()`, and checks
# (using exceptions) whether the following list of things are valid (using try and except):
#
# 1. If the input does not consist of 3 elements, raise a `MathematicalError`, which is a **custom Exception**.
# **_(Hint: create a custom exception class)_**
# 2. Try to convert the first and third input to a float type(like so: float_value = float(str_value)).
# Catch any `ValueError`(built-in exception) that occurs, and instead raise a `MathematicalError` (custom exception).
# 3. If the second input is not '+' or '-' (or any other operator that you use), again raise a `MathematicalError`.
#
# If the input is valid, perform the calculation and print out the result (as in the code above). The user is then
# prompted to provide new input, and so on, until the user types "quit".

### ```unittest```

# In order to test your solution:
#
# 1. *Name* your solution file as **solution_calc.py** .Run the test_calc.py
# 2. *Copy* **test_calc.py** file (provided in this repo) to the same folder
# 2. *Run* the **test_calc.py** script.
