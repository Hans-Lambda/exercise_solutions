<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Apex Cheatsheet Python](#apex-cheatsheet-python)
- [Generally useful](#generally-useful)
  - [Logical Operators Precedence](#logical-operators-precedence)
  - [Comments](#comments)
  - [Key combos](#key-combos)
- [Variables](#variables)
  - [Global, local, nonlocal Variables](#global-local-nonlocal-variables)
    - [Print Global and Local Variables](#print-global-and-local-variables)
    - [Global and local variable with same name](#global-and-local-variable-with-same-name)
    - [Declaring Variable global](#declaring-variable-global)
    - [Declaring Variable nonlocal](#declaring-variable-nonlocal)
  - [Formatting Variables](#formatting-variables)
  - [Assignment Expressions](#assignment-expressions)
  - [Booleans](#booleans)
    - [Non-Boolean Values](#non-boolean-values)
  - [Strings](#strings)
    - [Replacing in Strings](#replacing-in-strings)
    - [String Slicing](#string-slicing)
- [Data Structures](#data-structures)
  - [Dictionaries](#dictionaries)
    - [Print Key](#print-key)
    - [Print Value](#print-value)
    - [Print Key_Value_Pair](#print-key_value_pair)
    - [Get Index from Key](#get-index-from-key)
    - [Add item to Dictionary](#add-item-to-dictionary)
  - [Lists](#lists)
    - [Printing list items](#printing-list-items)
    - [Check for Sublists](#check-for-sublists)
    - [List Slicing](#list-slicing)
    - [List Comprehension](#list-comprehension)
    - [Mapping Lists](#mapping-lists)
- [User Input](#user-input)
  - [Click Module](#click-module)
  - [Holy Grail of Input on StackOverFlow](#holy-grail-of-input-on-stackoverflow)
- [Timing and Memory](#timing-and-memory)
- [Awesome methods you could forget about](#awesome-methods-you-could-forget-about)
- [OOP Design Patterns](#oop-design-patterns)
  - [Factory Pattern](#factory-pattern)
    - [Objective](#objective)
    - [Classification](#classification)
    - [Code Example](#code-example)
    - [Polymorphism or Abstract Class required?](#polymorphism-or-abstract-class-required)
  - [Singleton](#singleton)
    - [Objective](#objective-1)
    - [Classification](#classification-1)
    - [Code Example](#code-example-1)
    - [Polymorphism or Abstract Class required?](#polymorphism-or-abstract-class-required-1)
  - [Observer](#observer)
    - [Objective](#objective-2)
    - [Classification](#classification-2)
    - [Code Example](#code-example-2)
    - [Polymorphism or Abstract Class required?](#polymorphism-or-abstract-class-required-2)
  - [Strategy](#strategy)
    - [Objective](#objective-3)
    - [Classification](#classification-3)
    - [Code Example](#code-example-3)
    - [Polymorphism or Abstract Class required?](#polymorphism-or-abstract-class-required-3)
  - [Adapter](#adapter)
    - [Objective](#objective-4)
    - [Classification](#classification-4)
    - [Code Example](#code-example-4)
    - [Polymorphism or Abstract Class required?](#polymorphism-or-abstract-class-required-4)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# Apex Cheatsheet Python

# Generally useful

[Regex for English Words](url="https://stackoverflow.com/questions/60271576/how-to-select-words-with-apostrophe-using-regular-expression")

[Zetcode library](url="https://zetcode.com/all/#python")

[Stackoverflow - Iterate stuff](url="https://stackoverflow.com/questions/33077274/lambda-in-python-can-iterate-dict")

Input prompt in same line:

    print("Please type: >>> ", end='')
    y = input()

Better Debugger:

    import pdb; pdb.set_trace()

## Logical Operators Precedence

    1. not
    2. and
    3. or

## Comments

"""
multi line
comment
"""

ordinary comment by #

## Key combos

CTRL + Shift + C            -> copy absolute path to file

CTRL + Shift + V            -> paste (to Terminal)

dir(OBJECT_OF_INTEREST)     -> shows possible methods in module

help(OBJECT.METHOD)         -> gives short rundown on object.method      

CTRL + Num /                -> comment/uncomment code (above Num 8)

ALT + Shift + n7            -> show all references everywhere for the word at the caret

# Variables

## Global, local, nonlocal Variables

### Print Global and Local Variables

[Print Global and Local Variables](url="https://www.delftstack.com/howto/python/python-print-variable-name/")

Example 1 - Print Global Variables - if Variable is on Top Level

    city = "Berlin"
    population = 9000000
    variable_names = [name for name in globals() if globals()[name] is city or population]
    print(variable_names)
    print(locals().items())

    Output:
    ['city', 'population']
    dict_items([('city', 'Berlin'), ('population', 9000000), ('variable_names', ['city', 'population'])])

Example 1 - Print Local Variables - if Variable is in Function

    city = "Berlin"
    population = 9000000
    variable_names = [name for name in locals() if locals()[name] is city or population]
    print(variable_names)
    print(locals().items())
    [print(f"{k.capitalize()}: {v.capitalize() if (type(v) == str) else v} {f'({type(v) == str})' if type(v) == str else ''}") for k, v in locals().items()]

    Output:
    Output:
    ['city', 'population']
    dict_items([('city', 'Berlin'), ('population', 9000000), ('variable_names', ['city', 'population'])])
    City: Berlin (True)
    Population: 9000000 

### Global and local variable with same name

both x keep their values

    x = 5

    def foo():
        x = 10
        print("local x:", x)


    foo()
    print("global x:", x)
    
    Output:
    local x: 10
    global x: 5

### Declaring Variable global

do this to make a variable from outside the function(global var) accessible 
and manipulable in the function

    x = "global "

    def foo():
        global x
        y = "local"
        x = x * 2
        print(x)
        print(y)

    foo()

    Output:
    global global 
    local

### Declaring Variable nonlocal

change the value of a nonlocal variable, to change the local variable

    def outer():
        x = "local"

        def inner():
            nonlocal x
            x = "nonlocal"
            print("inner:", x)

        inner()
        print("outer:", x)

    outer()
    
    Output:
    inner: nonlocal
    outer: nonlocal

## Formatting Variables

[Formatting in general](url="https://www.askpython.com/python/string/python-format-function")

[Python String (and numbers) Format Cookbook](url="https://mkaz.blog/code/python-string-format-cookbook/")

Via format() function

    "{}".format(value)

    "{{0}}".format(value)
    prints: {0}


Example 0 - numbers

    print("FORMAT".format(NUMBER))

    shorting to two decimals

    print("{:.2f}".format(6.12345))
    
    Output:
    6.12

Example 1

    s1 = 'Python'
    s2 = 'with'
    s4 = 'JournalDev'
 
    s3 = "{} {} {}".format(s1, s2, s4)
    print(s3)

    Output:
    Python with JournalDev

Example 2 - index formatting

    s1 = 'Python'
    s2 = 'with'
    s4 = 'Data Science'
 
    res = "{2} {1} {0}".format(s1, s2, s4)
    print(res)

    Output:
    Data Science with Python

Example 3 - passing values

    "{var1}".format(var1='value')

    res = "{s4} {s2} {s1}".format(s1 = 'Python',s2 = 'with',s4 = 'Data Science')
    print(res)

    Output:
    Data Science with Python

Example 4 - passing dict as parameter

    "{key}".format(**dict)

Since, we are passing the dict keys as arguments, in order to replace the 
keys with their values we need to unpack the dictionary.
Thus, Python "**" operator is used to unpack the dictionary.

    dict1 = {"Python":"A","Java":"B","Cpp":"D"}
    res = "{Python} {Cpp}".format(**dict1)
    print(res)

    Output:
    A D

## Assignment Expressions

Possibility to assign Value to Variable in an Expression

[Tutorial Assignment Expressions](url="https://www.digitalocean.com/community/tutorials/how-to-use-assignment-expressions-in-python")
[Less useful Explanation](url="https://peps.python.org/pep-0572/")
[More about the Walrus operator](url="https://realpython.com/python-walrus-operator/")

Example 1 - Using Assignment Expressions in if Statements

    some_list = [1, 2, 3]
    if (list_length := len(some_list)) > 2:
        print("List length of", list_length, "is too long")
    
    Output:
    List length of 3 is too long

Example 2 - Using Assignment Expressions in while Loops

    while (directive := input("Enter text: ")) != "stop":
        print("Received directive", directive)

    Output Example:

    Enter text: hello
    Received directive hello
    Enter text: example
    Received directive example
    Enter text: stop

Example 3 - Using Assignment Expressions in List Comprehensions


**** Assignment Expression ****

    def slow_calculation(x):
        print("Multiplying", x, "*", x)
        return x * x
    
    [result for i in range(3) if (result := slow_calculation(i)) > 0]
    
    Output:
    
    Multiplying 0 * 0
    Multiplying 1 * 1
    Multiplying 2 * 2
    [1, 4]

**** Oldschool ****

    def slow_calculation(x):
        print("Multiplying", x, "*", x)
        return x * x
    
    [slow_calculation(i) for i in range(3) if slow_calculation(i) > 0]
    
    Output:
    
    Multiplying 0 * 0
    Multiplying 1 * 1
    Multiplying 1 * 1
    Multiplying 2 * 2
    Multiplying 2 * 2
    [1, 4]

## Booleans

If value != zero it is True
x = 1 is True

### Non-Boolean Values

Example 1 - and

    True and 1000
    Output:
    1000

    1000 and True
    Output:
    True

## Strings

### Replacing in Strings

[ ] add method for using replace() and maketrans()/translate() from dictionary
[ ] add sub() method

Example 1  - replace() for single adjustments

    sentence.replace("WORD", "REPLACEMENT")

Example 2 - maketrans() and translate() for multiple adjustments

[maketrans - translate - method](url="https://www.delftstack.com/howto/python/python-replace-multiple-characters/")

    txt = "Hi, my name is Mary. I like zebras and xylophones."

    transTable = txt.maketrans("aeiou", "AEIOU", "xyz")
    txt = txt.translate(transTable)
    print(txt)

    print(txt.translate(txt.maketrans("aeiou", "AEIOU", "xyz")))

### String Slicing

Example 1 - Split at Delimiter

    s = "wolfdo65gtornado!salmontiger223"
    m = s.index('!')
    l = s[:m]

# Data Structures

## Dictionaries

[deleting from dictionaries](url="https://www.askpython.com/python/dictionary/delete-a-dictionary-in-python")

    DICT = {"Key": Value, "Key2": Value2, ... }

### Print Key
    
    print(list(DICT)[Index_of_pair])

### Print Value

    print(list(DICT.values())[Index_of_pair])

### Print Key_Value_Pair

Print an object containing the whole dictionary

    print(list(DICT.items()))

    Output:
    [('Key', 'Value'), ('Key2', 'Value2')]

Print full pairs

    for k, v in DICT.items():
        print(k, v)

    Output:
    Key Value
    Key2 Value2

Look if EXAMPLE is Value

    if EXAMPLE == DICT[Key]:

Delete Key_Value_Pair

    DICT.pop(Key)

Create new dictionary by filtering via DICT.items()

    DICT = {"Key": Value, "Key2": Value2, "Key3": Value3, ... }

Example 1 - new dictionary without key2

    new_DICT = {key:value for key, value in DICT.items() if key != "Key2"} 

Example 2 - new dictionary of tuples with only values > 0

    new_DICT = [(key, value) for key, value in DICT.items() if value > 0]

    Outout:
    new_DICT = {"Key": Value, "Key3": Value3, ... }

Modification by loop

    for KEY in list(DICT): 
    if KEY =="Key":  
        del DICT[KEY] 

    Outout:
    new_DICT = {"Key2": Value2, "Key3": Value3, ... }

### Get Index from Key

    list(DICT.keys()).index("Key2")

    Output:
    1

### Add item to Dictionary
    
    DICT[NEW_ITEM] = KEY

## Lists

    LIST = ["This", "is", "a", "list"]

### Printing list items

[Printing Lists](url="https://www.geeksforgeeks.org/print-lists-in-python-4-different-ways/")

Example 1 - Using the ‘*’ symbol

    print(*LIST, sep="\n")

    Output:
    This
    is
    a
    list

    print(*LIST, sep=", ")
    
    Output:
    This, is, a, list

### Check for Sublists

[Sublists](url="https://stackoverflow.com/questions/35964155/checking-if-list-is-a-sublist")

Example 1 - see if all items from list1 are in list2

    list1 = ['1','2']
    list2 = ['1','2',3]

    all(i in list2 for i in list1)

Example 2 - b = sublist and a = list then search b by splitting a in lengths of b

-> xrange is for generators - no idea until now

    a = [2,4,3,5,7] , b = [4,3]
    b in [a[i:len(b)+i] for i in range(len(a))]

    Output:
    True

    a = [2,4,3,5,7] , b = [4,10]
    b in [a[i:len(b)+i] for i in xrange(len(a))]

    Output:
    False

### List Slicing

[Stackoverflow](url="https://stackoverflow.com/questions/509211/understanding-slicing")

### List Comprehension

Example 1 - Convert Strings in List to Int

    test_list = ['1', '4', '3', '6', '7']
    test_list = [int(i) for i in test_list]
    Output:
    [1, 4, 3, 6, 7]

Example 2 - Convert Strings in List of Lists to Int

    # split matrix_string @ \n into list of lists, split sublist @ ' ', convert sublist items to int
    # self. indicates the example is taken from a functrion in a class

    self.matrix_string = "1 2 3 4\n5 6 7 8\n9 8 7 6"
    
    self.m_split = [[int(j) for j in i.split(" ")] for i in (self.matrix_string.split("\n"))]
    
    Output:
    [[1, 2, 3], [4, 5, 6], [7, 8, 9], [8, 7, 6]]

Example 3 - Alternative to Example 2

    row = matrix_string.split('\n')
    self.matrix = [[int(col) for col in row.split()] for row in row]

Example 4 - From loop to list of dictionaries

    # evens = [i for i in list if i % 2 == 0]
    # odds = [i for i in list if i % 2 == 1]

    def odd_even():
        nlist = [*range(25)]
        evens = [{"even_value": i} for i in nlist if i % 2 == 0]
        odds = [{"odd_value": i} for i in nlist if i % 2 != 0]
        print(evens)
        print(odds)

Example 5 - another example

    def author_is_popular(author):
    author = get_author(author)
    return bool(
        author
        and author["items"]
        and (sum([article["reads"] for article in author["items"]
                  if "reads" in article and article["status"] == "Published"]) / len(author["items"]) > 1000)
    )

Example 6 - Looping over list of dictionaries comparing input with value in dict, changing it and returning sum

    scores = {("A", "E", "I", "O", "U", "L", "N", "R", "S", "T"): 1, ("D", "G"): 2, ("B", "C", "M", "P"): 3, 
              ("F", "H", "V", "W", "Y"): 4, ("K"): 5, ("J", "X"): 8, ("Q", "Z"): 10}
    next(scores[score] for score in scores.keys() if char.upper() in score)]
    sum([result for [result] in [[next(scores[score] for score in scores.keys() if char.upper() in score)] 
              for char in word]])

Example 7 - Appending in List Comprehension

[Appending in List Comprehension](url="https://stackoverflow.com/questions/2505529/appending-item-to-lists-within-a-list-comprehension")

    fibo = [0, 1]
    [print(i) for i in [fibo.append(fibo[-1] + fibo[-2]) or x for x in fibo if x <= 50]]

Example 8 - Get info from different Dictionaries of LIST of DICT_1 of DICT_2

    [print(DICT_1[DICT_2][ITEM]) for DICT_1 in LIST for DICT_1_OTHER_TERM in DICT_1[DICT_2] if DICT_1[DICT_2][ITEM_2] == INPUT]

### Mapping Lists

    test_list = ['1', '4', '3', '6', '7']
    Output:
    [1, 4, 3, 6, 7]

Example 1 - split the string with delimiter '\n'

    a = ("1 2 3\n4 5 6\n7 8 9\n8 7 6")
    b = a.split("\n")

    Output: 
    ['1 2 3', '4 5 6', '7 8 9', '8 7 6']

# User Input

## Click Module

Python package for creating beautiful command line interfaces in a composable way
Also works for User Input

[General Docs](urls="https://click.palletsprojects.com/en/7.x/")
[Input Parameters](urls="https://click.palletsprojects.com/en/7.x/parameters/#parameter-types")

## Holy Grail of Input on StackOverFlow

[Holy_Grail.exe](url="https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response")
[Guide on Towardsdatascience](url="https://towardsdatascience.com/a-complete-guide-to-user-input-in-python-727561fc16e1")

# Timing and Memory

@timeit tu measure time to execute code

# Awesome methods you could forget about

    random.random() generates a random number between 0 and 1

https://www.geeksforgeeks.org/dunder-magic-methods-python/

https://docs.python.org/3/reference/datamodel.html

https://docs.python.org/3/library/stdtypes.html#object.__dict__


# OOP Design Patterns

When we architect a system and analyze its requirements and features, we have to think about how to organize the classes
and the relationship between them. After working on different projects, we start to identify some patterns that appear 
in various projects.

Some patterns used to occur so often that they were cataloged and classified. The book Design Patterns. 
Elements of Reusable Object-Oriented Software, Erich Gama et al. was one of the first attempts to catalog 
these patterns and provide recipes to those trying to apply them.

Patterns are then divided into three categories, creational, behavioral, and structural. Polymorphism and 
Abstract Classes (and Interfaces, a concept not present in Python) are essential tools for implementing these patterns.

## Factory Pattern

Factory Method is a creational design pattern used to create concrete implementations of a common interface.

It separates the process of creating an object from the code that depends on the interface of the object.

### Objective

* used to create concrete implementations of a common interface

* interface is like hub for classes and functions instead of putting everything together

* the central idea in Factory Method is to provide a separate component with the responsibility to decide which concrete 
implementation should be used based on some specified parameter

### Classification

creational

### Code Example

### Polymorphism or Abstract Class required?



## Singleton

* Singleton pattern is a design pattern in Python that restricts the instantiation of a class to one object

* it can limit concurrent access to a shared resource, and also it helps to create a global point of access for a resource

### Objective

* to create just one instance of a class, throughout the lifetime of a program

* limit concurrent access to a shared resource

* create a global point of access for a resource

### Classification

creational

### Code Example

https://www.geeksforgeeks.org/singleton-pattern-in-python-a-complete-guide/#:~:text=Singleton%20pattern%20is%20a%20design,of%20access%20for%20a%20resource.

Singleton pattern can be implemented in three different ways. They are as follows:

* Module-level Singleton

        all modules are singleton, by definition
        for example a variable stored in another file
        singleton.py
        shared_variable = "Shared Variable"

* Classic Singleton

        creates an instance only if there is no instance created so far
        otherwise, it will return the instance that is already created

* Borg Singleton

        design pattern in Python that allows state sharing for different instances. Let’s look into the following code

### Polymorphism or Abstract Class required?



## Observer

### Objective

* define or create a subscription mechanism to send the notification to the multiple objects about any new event 
that happens to the object that they are observing

* the subject is basically observed by multiple objects

* the subject needs to be monitored and whenever there is a change in the subject, the observers are being notified about the change

### Classification

behavioral

### Code Example

https://www.geeksforgeeks.org/observer-method-python-design-patterns/

### Polymorphism or Abstract Class required?



## Strategy

### Objective

* the main goal of strategy pattern is to enable client to choose from different algorithms or procedures to complete the specified task

* different algorithms can be swapped in and out without any complications for the mentioned task

* it provides a list of strategies from the functions, which execute the output

### Classification

behavioral

### Code Example

https://www.tutorialspoint.com/python_design_patterns/python_design_patterns_strategy.htm

### Polymorphism or Abstract Class required?



## Adapter

### Objective

* making the incompatible objects adaptable to each other

* create a bridge between two incompatible interfaces

### Classification

structural

### Code Example

https://www.geeksforgeeks.org/adapter-method-python-design-patterns/

### Polymorphism or Abstract Class required?

# Polymorphism

[Polymorphism](url="https://www.geeksforgeeks.org/polymorphism-in-python/")

[Lama on Singleton and Factory Pattern](url="https://docs.google.com/presentation/d/1L5i77jXS_ULGZjNAj8w-DoQqm9NGkKx7Kc35ItU2DQk/edit#slide=id.p")