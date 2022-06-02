<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [The World as Objects](#the-world-as-objects)
  - [What is OOP?](#what-is-oop)
  - [Why do we need OOP?](#why-do-we-need-oop)
  - [Benefits of OOP](#benefits-of-oop)
  - [What is an Object, and what is a Class?](#what-is-an-object-and-what-is-a-class)
  - [Main Principles](#main-principles)
  - [How does a Class look like in Python?](#how-does-a-class-look-like-in-python)
  - [Tips for learning OOP.](#tips-for-learning-oop)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# The World as Objects

Object-Oriented Programming (OOP) is one of the essential techniques we have in software development. 
It allows us to structure our program by modeling real-world objects inside our programs. 
Soon we will be learning OOP. In this Self-Study session, you will investigate why we need OOP, 
the advantages of using it, and how it can improve the structure of our program. 
The following questions need to be answered:

## What is OOP?

- programming model that organizes software design around data, or objects, rather than functions and logic
- an object can be defined as a data field that has unique attributes and behavior

## Why do we need OOP?

- focuses on the objects that developers want to manipulate rather than the logic required to manipulate them
- well-suited for programs that are large, complex and actively updated or maintained

## Benefits of OOP

**Modularity**

- Encapsulation enables objects to be self-contained, making troubleshooting and collaborative development easier

**Reusability**

- Code can be reused through inheritance, meaning a team does not have to write the same code multiple times

**Productivity**

- Programmers can construct new programs quicker through the use of multiple libraries and reusable code

**Easily upgradable and scalable**

- Programmers can implement system functionalities independently

**Interface descriptions**

- Descriptions of external systems are simple, due to message passing techniques that are used for objects communication

**Security**

- Using encapsulation and abstraction, complex code is hidden, software maintenance is easier and internet protocols are protected

**Flexibility**

- Polymorphism enables a single function to adapt to the class it is placed in
- Different objects can also pass through the same interface

## What is an Object, and what is a Class?

**Classes** 

- are user-defined data types that act as the blueprint for individual objects,
attributes and methods.

**Objects**

- are instances of a class created with specifically defined data
- Objects can correspond to real-world objects or an abstract entity
- when class is defined initially, the description is the only object that is defined

**Methods**

- are functions that are defined inside a class that describe the behaviors of an object 
- each method contained in class definitions starts with a reference to an instance object
- additionally, the subroutines contained in an object are called instance methods 
- methods are used for reusability or keeping functionality encapsulated inside one object at a time

**Attributes**

- are defined in the class template and represent the state of an object
- Objects will have data stored in the attributes field
- Class attributes belong to the class itself.

## Main Principles

**Encapsulation** 

- This principle states that all important information is contained inside an object and only select information is exposed. 
- The implementation and state of each object are privately held inside a defined class. 
- Other objects do not have access to this class or the authority to make changes. 
- They are only able to call a list of public functions or methods. 
- This characteristic of data hiding provides greater program security and avoids unintended data corruption.

**Abstraction**

- Objects only reveal internal mechanisms that are relevant for the use of other objects, hiding any unnecessary implementation code
- The derived class can have its functionality extended. 
- This concept can help developers more easily make additional changes or additions over time.

**Inheritance**

- Classes can reuse code from other classes
- Relationships and subclasses between objects can be assigned, enabling developers to reuse common logic while still maintaining a unique hierarchy
- This property of OOP forces a more thorough data analysis, reduces development time and ensures a higher level of accuracy

**Polymorphism**

- Objects are designed to share behaviors and they can take on more than one form
- The program will determine which meaning or usage is necessary for each execution of that object from a parent class, reducing the need to duplicate code
- A child class is then created, which extends the functionality of the parent class
- Polymorphism allows different types of objects to pass through the same interface

## How does a Class look like in Python?

    class Dog:
         
        # A simple class
        # attribute
        attr1 = "mammal"
        attr2 = "dog"
     
        # A sample method 
        def fun(self):
            print("I'm a", self.attr1)
            print("I'm a", self.attr2)
 
    # Driver code
    # Object instantiation
    Rodger = Dog()
     
    # Accessing class attributes
    # and method through objects
    print(Rodger.attr1)
    Rodger.fun()

## Tips for learning OOP.

- Google
