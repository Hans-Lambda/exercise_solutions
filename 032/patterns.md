<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

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

Patterns are then divided into three categories, creational (object creation), behavioral, and structural. Polymorphism and 
Abstract Classes (and Interfaces, a concept not present in Python) are essential tools for implementing these patterns.

Your task is to research at least two of the following patterns:

Factory Pattern
Singleton
Observer
Strategy
Adapter


## Factory Pattern

Factory Method is a creational design pattern used to create concrete implementations of a common interface.

It separates the process of creating an object from the code that depends on the interface of the object.

Reusable Solutions.

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

https://www.geeksforgeeks.org/singleton-pattern-in-python-a-complete-guide/

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