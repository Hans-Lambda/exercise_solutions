<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [DH - Python: Collections (8TU)](#dh---python-collections-8tu)
  - [Objectives](#objectives)
  - [Content](#content)
    - [Review on Python Basics Content](#review-on-python-basics-content)
      - [Topics](#topics)
  - [Learning Material](#learning-material)
    - [Additional/External Learning Material](#additionalexternal-learning-material)
  - [Exercises](#exercises)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# DH - Python: Collections (8TU)


## Objectives

- Teach the main concept of collections in a program.
- Introduce the basic python collections Lists and Dictionaries.

## Content

### Review on Python Basics Content

- Type: (Lecture, live-coding, exercises)
- Time Units: 8 TU

#### Topics

- Collections what it is and its different types.
- Python Lists
- Python Dictionaries

## Learning Material

- [Slides - Collections](https://drive.google.com/file/d/1sR12Pyh6aCp-14HZULIqIayBXLPJHezm/view?usp=sharing)

### Additional/External Learning Material

- **Book** - Automate the Boring Stuff with Python
  - [Chapter 4: Lists](https://automatetheboringstuff.com/2e/chapter4/)
  - [Chapter 5: Dictionaries and structuring data](https://automatetheboringstuff.com/2e/chapter5/)
- **Book** - Automate the Boring Stuff with Python
  - [Chapter 5: Lists](https://openbookproject.net/thinkcs/python/english3e/lists.html)
  - [Chapter 20: Dictionaries](https://openbookproject.net/thinkcs/python/english3e/dictionaries.html)

## Exercises

1. Write a program that declares two lists, e.g.
    ```python
    l1 = [2, 3, 4, 5, 8, 10]
    l2 = [9, 4, 3, 9, 3, 1]
    ```
    and creates a new list containing the sum 
    from elements, of both lists, with the same index. 
    The result of the sum of the lists above are:

    ```python
    [11, 7, 7, 14, 11, 11]
    ```
   
2. Create a program that declares a list, then asks the user to type 
   an integer value, remove from the list all occurrences of this value.
   Let's say you declare the following list in your program:
   ```python
   l = [2, 3, 3, 4, 3, 2, 1, 3]
   ```
   If the user types 3, the resulting list will be:
   ```python
   [2, 4, 2, 1]
   ```
   
3. Base on the list in file `the_blo_db`, create a program
   that asks the user to type a name, after that list all
   the posts written by the author whose name matchs the typed 
   name.

   For example, if the user type `Mathias` the result must be:

   ```
   Mathias' Posts
   - Learn Python
   - Controlling the Flow of your program!
   - Python Comprehensions
   ```
   
4. Based on the list of products in file the_supermarket, create
   a programa that reads from the user a product category, after read
   the discount to apply to the products of a specific category.
   Then list the name of the products followed by the new price, e.g.
   if the user type `beverage` and `10`, the result will be: 

   ```
   Soda Max: 0.72 Euros
   Beer: 9 Euros
   ```