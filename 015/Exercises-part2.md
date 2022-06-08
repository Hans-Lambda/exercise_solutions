<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Python logical expressions](#python-logical-expressions)
  - [Description](#description)
  - [](#)
  - [Tasks](#tasks)
    - [](#-1)
    - [Task 1:](#task-1)
- [Task 2](#task-2)
- [Task 3](#task-3)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# Python logical expressions

## Description

In this exercise, we will practice on more complex logical expressions including
various predicates and operators.

##

## Tasks

###

### Task 1:

Let's consider the following list of users:

```
users = [
    {
        "name": "Holly",
        "type": "Student",
        "password": "hunter",
        "modules": [
            {
                "title": "Computer basics",
                "completed": True
            },
            {
                "title": "Python basics",
                "completed": False
            }
        ]
    },
    {
        "name": "Peter",
        "type": "Student",
        "password": "pan",
        "modules": [
            {
                "title": "Computer basics",
                "completed": False
            }
        ]
    },
    {
        "name": "Luke",
        "type": "Student",
        "password": "skywalker",
        "modules": [
            {
                "title": "Computer basics",
                "completed": True
            }
        ]
    },
    {
        "name": "Janis",
        "type": "Teacher",
        "password": "joplin"
    }
]
```

Using the concepts, and some code from the previous exercises, define a function named `show_registration` that checks if a user is registered to a specific module.

The function will accept three input arguments:

- **username**. `String`
- **password**. `String`
- **modulename**. `String`

The function may print any of the following messages:

- `You are registered to the module {modulename}`.
It will print this message if the user is a student and in his `modules` key has a module with a `title` equal to the argument `modulename`
- `You did not register to the module {modulename}`
It will print this message if the user is anonymous or is a student and in his `modules` key DOES NOT have a module with the given title.
- `You are a teacher`
It will print this message if the username is a teacher.

> You may use additional functions to filter or store logical expressions to use in your `show_registration` function.

> You may use more than one conditional.

Use the following code to test:

```
username = input("What is your username? ")
password = input(f"Type the password for username {username}: ")
modulename = input("What module do you want to check? ")
show_registration(username, password, modulename)
```
- Your result should look like this:

```
What is your username? Peter
Type the password for username Peter: pan
What module do you want to check? Computer basics
You are registered to the module Computer basics.
```
```
What is your username? Luke
Type the password for username Luke: skywalker
What module do you want to check? Python basics
You did not register to the module Python basics.
```
```
What is your username? Janis
Type the password for username Janis: joplin
What module do you want to check? Django
You are a teacher.
```
```
What is your username? Anonymous
Type the password for username Anonymous: empty
What module do you want to check? Computer basics
You did not register to the module Computer basics.
```

# Task 2

Now add another function named `has_completed_module` similar to `show_registration` with the same input arguments and the following differences:

- This time, the function will do nothing if the user is valid and a teacher.
- It will check if, besides having a particular module in the user's list, the module has the key `completed` set to `True`.

Use the following code to test:

```
username = input("What is your username? ")
password = input(f"Type the password for username {username}: ")
modulename = input("What module do you want to check? ")
show_registration(username, password, modulename)
has_completed_module(username, password, modulename)
```
- Your result should look like this:

```
What is your username? Peter
Type the password for username Peter: pan
What module do you want to check? Computer basics
You are registered to the module Computer basics.
You did not complete the module Computer basics.
```
```
What is your username? Luke
Type the password for username Luke: skywalker
What module do you want to check? Computer basics
You are registered to the module Computer basics.
You have completed the module Computer basics.
```
```
What is your username? Janis
Type the password for username Janis: joplin
What module do you want to check? Django
You are a teacher.
```
```
What is your username? Anonymous
Type the password for username Anonymous: password
What module do you want to check? Django
You did not register to the module Django.
You did not complete the module Django.
```

# Task 3

Now we are given this list of modules:

```
modules = [
    {
        "name": "Computer basics"
    },
    {
        "name": "Python basics",
        "requirement": "Computer basics"
    },
    {
        "name": "Django",
        "requirement": "Python basics"
    }
]
```

Add a new function named `may_enroll` with three input parameters:

- **username**. `String`
- **password**. `String`
- **modulename**. `String`

This function should return `True` in the following cases:

- The user is anonymous and the module has no requirement (they can always register).
- The user is a student and:
    - The user is not already registered to that module.
    - The module has no requirement or it has one and the user meets the requirement (is also registered to the requirement and its `completed` flag is set to `True`).

In any other case, the function should return `False`.

> Keep the code from previous exercises.

> A teacher cannot register to any module.

> An anonymous user will only be allowed to register if the module has no requirement. If that happens, the script should not execute any other logical expression.

> Use as many functions as needed to keep the logical expressions easy to read. Use semantic names for those functions to improve the readability. Example: is_anonymous(), has_no_requirement(), meets_requirement(), ...

> Use any concept learned on the slides: short-circuiting, grouping,...

Use the following code to test:

```
username = input("What is your username? ")
password = input(f"Type the password for username {username}: ")
modulename = input("What module do you want to check? ")
show_registration(username, password, modulename)
has_completed_module(username, password, modulename)
if may_enroll(username, password, modulename):
    print(f"You may register to the module {modulename}.")
else:
    print(f"You may not register to the module {modulename}.")
```
- Your result should look like this:

```
What is your username? Peter
Type the password for username Peter: pan
What module do you want to check? Computer basics
You are registered to the module Computer basics.
You did not complete the module Computer basics.
You may not register to the module Computer basics.
```

```
What is your username? Peter
Type the password for username Peter: pan
What module do you want to check? Python basics
You did not register to the module Python basics.
You did not complete the module Python basics.
You may not register to the module Python basics.
```

```
What is your username? Luke
Type the password for username Luke: skywalker
What module do you want to check? Python basics
You did not register to the module Python basics.
You did not complete the module Python basics.
You may register to the module Python basics.
```

```
What is your username? Janis
Type the password for username Janis: joplin
What module do you want to check? Django
You are a teacher.
You may not register to the module Django.
```

```
What is your username? Anonymous
Type the password for username Anonymous: password
What module do you want to check? Computer basics
You did not register to the module Computer basics.
You did not complete the module Computer basics.
You may register to the module Computer basics.
```

```
What is your username? Anonymous
Type the password for username Anonymous: password
What module do you want to check? Django
You did not register to the module Django.
You did not complete the module Django.
You may not register to the module Django.
```

```
What is your username? Peter
Type the password for username Peter: pan
What module do you want to check? PHP
You did not register to the module PHP.
You did not complete the module PHP.
You may not register to the module PHP.
```
