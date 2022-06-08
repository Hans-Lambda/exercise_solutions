<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Python logical expressions](#python-logical-expressions)
  - [Description](#description)
  - [](#)
  - [Tasks](#tasks)
    - [](#-1)
    - [Task 1](#task-1)
    - [](#-2)
    - [Task 2](#task-2)
    - [](#-3)
    - [Task 3](#task-3)
    - [](#-4)
    - [Task 4](#task-4)
    - [](#-5)
    - [Task 5](#task-5)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# Python logical expressions

## Description

In this exercises, we will focus on the usage of simple logical expressions.

##

## Tasks

###

### Task 1

Validate the input credentials of a user. You should print the message `Welcome, {username}!` if the credentials are valid and the message `Credentials are invalid` if they are not.

Use the following code:

```
username = input("What is your username? ")
password = input(f"Type the password for username {user}: ")
valid = {"username": "admin", "password": "admin"}
# Your code here
```
- Your result should look like this:

```
What is your username? admin
Type the password for username admin: admin
Welcome, admin!
```
```
What is your username? Luke
Type the password for username Luke: Skywalker
Credentials are invalid
```
```
What is your username? Luke
Type the password for username Luke: admin
Credentials are invalid
```
```
What is your username? admin
Type the password for username admin: password
Credentials are invalid
```
###

### Task 2

Define a function named `isweekend` that accepts a parameter named `date` of type `Datetime` (with a default value of `datetime.datetime.now()`).

This function will serve as a logical expression and will return `True` if the day of the week in the `date` is either Saturday or Sunday. It will return `False` in any other case.

> You can actually do this in many ways, but in this exercise **you are required to use the OR operator**.

Use the following test cases:

```
print(isweekend(datetime.date(2021, 8, 6)))
print(isweekend(datetime.date(2021, 8, 7)))
print(isweekend(datetime.date(2021, 8, 8)))
print(isweekend(datetime.date(2021, 8, 9)))
```
- Your result should look like this:

```
False
True
True
False
```
###

### Task 3

We now want a version of the first task, that will implement an "open doors" policy on the weekends. So, if the user credentials are valid, or the date is on the weekend, the conditional should evaluate to `True` and greet the user.

> Use a single logical expression.

> Reuse the `isweekend(<Datetime>)` function from before.

Use the following code:

```
username = input("What is your username? ")
password = input(f"Type the password for username {username}: ")
valid = {"username": "admin", "password": "admin"}
today = datetime.date(2021, 8, 7)
# Your code here
```

Use the following date objects to do the different tests:

```
today = datetime.date(2021, 8, 7)
today = datetime.date(2021, 8, 6)
```

- Your result should look like this:

**today = datetime.date(2021, 8, 7)**

```
What is your username? admin
Type the password for username admin: admin
Welcome, admin!
```
```
What is your username? Anonymous
Type the password for username admin: 1234
Welcome, Anonymous!
```
**today = datetime.date(2021, 8, 6)**

```
What is your username? admin
Type the password for username admin: admin
Welcome, admin!
```
```
What is your username? Anonymous
Type the password for username admin: 1234
Credentials are invalid
```

###

### Task 4

Now define a function named `get_user` with the input arguments `username` and `password`, both as a `String`.

There is a global variable named `users` as a list of dictionaries:

```
users = [
    {
        "name": "Holly",
        "password": "hunter"
    },
    {
        "name": "Peter",
        "password": "pan"
    },
    {
        "name": "Janis",
        "password": "joplin"
    }
]
```

The function should return the first dictionary in the list `users` matching the `username` and `password` provided. If no user matches, it should return `None`.

When the user provided is invalid (when `get_user` returned None) the function should show the message `An error occurred. You are not authorized.`.

> Do nothing if the user is valid.

> Use the "truthy" and "falsy" nature of the Non-boolean values returned by `get_user`.

Use the following code:

```
username = input("What is your username? ")
password = input(f"Type the password for username {username}: ")
user = get_user(username, password)
# Rest of your code here
```
- Your result should look like this:

```
What is your username? admin
Type the password for username admin: admin
An error occurred. You are not authorized.
```
```
What is your username? Janis
Type the password for username Janis: joplin
```
```
What is your username? Janis
Type the password for username Janis: hunter
An error occurred. You are not authorized.
```

###

### Task 5

Replace the previous list of users with the following one:

```
users = [
    {
        "name": "Holly",
        "type": "Student",
        "password": "hunter"
    },
    {
        "name": "Peter",
        "type": "Student",
        "password": "pan"
    },
    {
        "name": "Janis",
        "type": "Teacher",
        "password": "joplin"
    }
]
```

Now define a function named `show_offers` that accepts, again, a `username` and `password` as `Strings`.

This function will print a message if the user is a Student or anonymous (the `get_user` function returned None) saying `We have great courses to offer you!`. If the user is a Teacher it should do nothing.

> Reuse the `get_user` function from before.

> Use a single conditional (use functions to simplify it or make it more readable).

> Use short-circuiting to avoid errors.

Use the following code:

```
username = input("What is your username? ")
password = input(f"Type the password for username {username}: ")
show_offers(username, password)
```
- Your result should look like this:

```
What is your username? Holly
Type the password for username Holly: hunter
We have great courses to offer you!
```
```
What is your username? Janis
Type the password for username Janis: joplin
```
```
What is your username? Anonymous123
Type the password for username Anonymous123: password
We have great courses to offer you!
```
