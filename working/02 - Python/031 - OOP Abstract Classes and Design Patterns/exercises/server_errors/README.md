<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Server Error](#server-error)
  - [Task](#task)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# Server Error

Topic: **Class Polymorphism**

## Task
Create 3 classes:
* **OK**: Represents OK code error 200.
* **NotFound**: Represents Not Found code error 404.
* **ServerError**: Represents Server Error code 500.

- [ ] In each of the class, add attributes for the error code and the error message.


- [ ] Create a function **status(error_object)** That displays the error code and the error message of an object of any of the three classes above.


-[ ] Write a **main.py** to test your code: Create an object of each class, and run the function **status(error_object)** on them.


> The idea of this exercise is to see polymorphism in action:
> 
> The function **status(error_object)** changes its behaviour depending on the type (class) of the object it runs on.