<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Python logical expressions](#python-logical-expressions)
  - [Description](#description)
    - [](#)
    - [Task](#task)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# Python logical expressions

## Description

In this exercise, we will look into a common feature of most web applications (users, roles and permissions) to practice some more on even more complex logical expressions.

###

### Task

Consider the following set of dictionaries:

```
roles = {
    "ST": "Student",
    "REST": "Registered student",
    "AL": "Alumni",
    "AN": "Anonymous",
    "TE": "Teacher",
    "AD": "Admin"
}

users = [
    {
        "name": "Holly",
        "role": roles["ST"]
    },
    {
        "name": "Peter",
        "role": roles["ST"]
    },
    {
        "name": "Luke",
        "role": roles["ST"]
    },
    {
        "name": "Janis",
        "role": roles["TE"]
    },
    {
        "name": "Aretha",
        "role": roles["TE"]
    },
    {
        "name": "Ringo",
        "role": roles["AD"]
    }
]

modules = [
    {
        "title": "Computer basics",
        "teacher": "Janis",
        "registered": ["Peter"],
        "alumni": ["Luke", "Holly"]
    },
    {
        "title": "Python basics",
        "teacher": "Janis",
        "registered": ["Holly"],
        "alumni": [],
        "requirement": "Computer basics"
    },
    {
        "title": "Django basics",
        "teacher": "Aretha",
        "registered": [],
        "alumni": [],
        "requirement": "Python basics"
    }
]

module_permissions = {
    roles["AN"]: ["describe"],
    roles["ST"]: ["describe"],
    roles["REST"]: ["describe", "read", "comment"],
    roles["AL"]: ["describe", "read"],
    roles["TE"]: ["describe", "read"],
    roles["AD"]: ["describe", "read", "write", "comment"]
}
```

> **Data**

> Most of the data may be self-explanatory, but some additional clarification on `roles` and `module_permissions` may be of help.

> We have identified 6 different roles: Anonymous, Student, Registered student, Alumni, Teacher and Admin.

> 3 of these roles are actually present in our `users` dictionary: Student, Teacher and Admin. The other 3 are virtual roles that will be defined in our code when some conditions are met.

> Anonymous is any user who is not in our list.

> Registered student is a user with the role Student who is registered to the module being queried.

> Alumni is a user with the role Student who was registered to this module in the past and now is part of the alumni of this module.

> According to the module_permissions dictionary, everyone should be able to see a description of all modules, even the anonymous user.

> Teachers (TE) can also read all modules.

> The only students who can see a particular module are the registered students (REST) and alumni (AL).

> The only students who can publish comments on the module are the students registered on that module.

> The admin can perform any operation on any module.

On this exercise you will define a function named `has_permission` that will require 3 parameters:

- **user_name**: a `String` with the name of a user (Holly, Peter, Luke, Janis, Aretha, Ringo).
- **module_name**: a `String` with the name of a module (Computer basics, Python basics, Django basics).
- **permission**: a `String` with the name of the permission (describe, read, write, comment).

The function will return `True` if the user has the requested type of permission on the module indicated. If not, it will return `False`.

Follow this general rules:

- Each user dictionary has a `role` key.
- The dictionary `module_permissions` has the name of these roles as keys and a list of permissions as values. This dictionary indicates the basic access of each role to any module.
- You can use it to check if a user (actually, the role of the given user) has the given permission as default to every module.

You will have to consider the following exceptions:

- The anonymous user is not actually a user, so you may have to write a logical expression to catch this particular case.
- The students who are registered (or alumni) in a module will actually need to be checked for permissions taking the REST or AL roles instead of ST. You may have to write another logical expression to catch these particular cases.
- Teachers have read access to every module, but they should also have Admin access (describe, read, write, comment) to the module they are teaching. We do not have a specific role for this case, use the AD permissions instead. Again, you may have to add another logical expression to catch this particular case.

> You are only allowed to use `if` conditional statements when getting the user and module from their list.

> The `has_permission` function should have a first couple of instructions to get the user and module objects and then it should immediately return a logical expression that needs to be fairly simple to read.

> Use functions as predicates the make the main logical expression more readable.

Use the following test case:

```
for permission in module_permissions["Admin"]:
    for module in modules:
        print(f"Can {permission.upper()} on {module['title'].upper()}?")
        print("Anonymous",
              has_permission("Somebody", module["title"], permission))
        for user in users:
            print(user["name"],
                  has_permission(user["name"], module["title"], permission))
```
- Your result should look like this:

```
Can DESCRIBE on COMPUTER BASICS?
Anonymous True
Holly True
Peter True
Luke True
Janis True
Aretha True
Ringo True
Can DESCRIBE on PYTHON BASICS?
Anonymous True
Holly True
Peter True
Luke True
Janis True
Aretha True
Ringo True
Can DESCRIBE on DJANGO BASICS?
Anonymous True
Holly True
Peter True
Luke True
Janis True
Aretha True
Ringo True
Can READ on COMPUTER BASICS?
Anonymous False
Holly True
Peter True
Luke True
Janis True
Aretha True
Ringo True
Can READ on PYTHON BASICS?
Anonymous False
Holly True
Peter False
Luke False
Janis True
Aretha True
Ringo True
Can READ on DJANGO BASICS?
Anonymous False
Holly False
Peter False
Luke False
Janis True
Aretha True
Ringo True
Can WRITE on COMPUTER BASICS?
Anonymous False
Holly False
Peter False
Luke False
Janis True
Aretha False
Ringo True
Can WRITE on PYTHON BASICS?
Anonymous False
Holly False
Peter False
Luke False
Janis True
Aretha False
Ringo True
Can WRITE on DJANGO BASICS?
Anonymous False
Holly False
Peter False
Luke False
Janis False
Aretha True
Ringo True
Can COMMENT on COMPUTER BASICS?
Anonymous False
Holly False
Peter True
Luke False
Janis True
Aretha False
Ringo True
Can COMMENT on PYTHON BASICS?
Anonymous False
Holly True
Peter False
Luke False
Janis True
Aretha False
Ringo True
Can COMMENT on DJANGO BASICS?
Anonymous False
Holly False
Peter False
Luke False
Janis False
Aretha True
Ringo True
```
