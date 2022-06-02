<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [DH - Fundamentals: Programming - Introduction with Python (8TU)](#dh---fundamentals-programming---introduction-with-python-8tu)
  - [Objectives](#objectives)
  - [Python Basic Concepts](#python-basic-concepts)
      - [Topics](#topics)
  - [Programming with Python](#programming-with-python)
      - [Topics](#topics-1)
  - [Exercise](#exercise)
    - [Part 1 - Transform Diagrams into Python Code](#part-1---transform-diagrams-into-python-code)
    - [Part 2 - Programing](#part-2---programing)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# DH - Fundamentals: Programming - Introduction with Python (8TU)

## Objectives

- Python basic concepts and a first simple program.
- Creating, programing and inspecting a program.

## Python Basic Concepts

- Type: Lecture + Exercises 
- Time Units: 4 TU

#### Topics

- Python basic aspects. 
- How to write a simple program with python.


## Programming with Python 

- Type: Exercises (2TU)
- Time Planned: 4 TU

#### Topics

- Create and implement multiple programs in Python
- Debugger

## Exercise

- Solutions
  - [Part 1 - Transform Diagrams into Python Code](https://github.com/mathiasbrito-dci/python-course-2022/tree/main/01%20-%20DH%20Fundamentals/011%20Day%20-%20Programming%20-%20Introduction%20to%20Programming%20with%20Python/class_examples_part1)
  - [Part 2 - Programing](https://github.com/mathiasbrito-dci/python-course-2022/tree/main/01%20-%20DH%20Fundamentals/011%20Day%20-%20Programming%20-%20Introduction%20to%20Programming%20with%20Python/class_examples_part2)

### Part 1 - Transform Diagrams into Python Code

1. Try to create a python program out of the diagrams you created last class, important concepts to use are:
   - create and initialize variables with values
   - use of functions `print()` and `input()`
   - use of arithmetical and relational operators
   - use of `if` to take decisions.
   
### Part 2 - Programing 

1. Create a function called `hello` that receives a `name` as an argument and prints the string `Hello <name>` in the screen.
   - The name must be read with `input` outside the function.
   - The name must be stored in a variable called `name`.
   - Call the function with different values and check the result.
2. Create a function called `sum3` that receives three numbers as arguments and returns the sum.
   - Invoke the function by passing literal values.
   - Invoke the function passing variables (initialize the variables first).
   - Invoke the functions with both variables and literals.
3. Create a function `is_first_greater` that receives two numbers and checks if the first is greater than the second.
   - Function must return `True` if the first is greater `False` otherwise.
4. Create a function that do not receive any argument and returns the current date and time.
   - import the as `from datetime import datetime`, than you can get the current date and time by doing
     `datetime.now()`.
   - If you print the result you will get something like `2022-04-18 16:43:40.290323`