<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [DH - Python: Handling Text Files (8TU)](#dh---python-handling-text-files-8tu)
  - [Objectives](#objectives)
  - [Content](#content)
    - [Basics of Text File handling](#basics-of-text-file-handling)
      - [Topics](#topics)
    - [Writing and Reading Json From a File](#writing-and-reading-json-from-a-file)
  - [Learning Material](#learning-material)
    - [Additional/External Learning Material](#additionalexternal-learning-material)
  - [Exercises](#exercises)
    - [File I/O](#file-io)
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
        - [](#-6)
        - [Task 6](#task-6)
        - [](#-7)
        - [Disclaimer](#disclaimer)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# DH - Python: Handling Text Files (8TU)


## Objectives

- Introduce the basics of file manipulation.
- Open, read and write text files.
- How to write and read JSON to a file

## Content

### Basics of Text File handling

- Type: (Lecture, live-coding, exercises)
- Time Units: 5 TU

#### Topics

- Opening a text file.
- Reading data from a file. The entire file or line-by-line.
- Writing data to a file and appending data.

### Writing and Reading Json From a File

- Type: (Self.Studying)
- Time Units: 3 TU

## Learning Material

- [Slides - Input/Output](https://drive.google.com/file/d/10GIZ0Wp6d_n6Fl_dVxk1sxypB8Mmiv8K/view?usp=sharing)

### Additional/External Learning Material

- **Book** - Automate the Boring Stuff with Python
  - [Chapter 9: Reading and Writing Files](https://automatetheboringstuff.com/2e/chapter9/)
- **Book** - Automate the Boring Stuff with Python
  - [Chapter 13: Files](https://openbookproject.net/thinkcs/python/english3e/files.html)

## Exercises

### File I/O

#### Description

In this exercise, we will focus on opening files for reading and practicing the use of the position.

####

#### Tasks

#####

###### Task 1

Open the file [src/data/task1.txt](src/data/task1.txt) and print its entire content with the least amount of instructions possible.

> Make sure the file is closed before the script finishes.

- Your result should look like this:

```
CHAPTER I

JONATHAN HARKER'S JOURNAL

(_Kept in shorthand._)
```

######

##### Task 2

Output the amount of ToDos written in the file [src/data/task2.txt](src/data/task2.txt).

> Consider the following:
> - There will always be two lines at the beginning of the list (one with the header and the other empty).
> - Every ToDo in the list will be written in a single line.
> - Every line in the list will contain a single ToDo.
> - There will be nothing after the list.

- Your result should look like this:

```
5
```

#####

##### Task 3

Open the file [src/data/task3.txt](src/data/task3.txt) and print its entire content as you did on **Task 1**. You will see a text that seems mixed up:

```
_3 May. Bistritz._--Left Munich at 8:35 P. M., on 1st May, arriving at
late and would start as near the correct time as possible. The
Vienna early next morning; should have arrived at 6:46, but train was an
impression I had was that we were leaving the West and entering the
hour late. Buda-Pesth seems a wonderful place, from the glimpse which I
East; the most western of splendid bridges over the Danube, which is
got of it from the train and the little I could walk through the
here of noble width and depth, took us among the traditions of Turkish
streets. I feared to go very far from the station, as we had arrived
rule.
```

This text has been manipulated so that it only reads well if we print the `odd` lines first and then the `even` lines. Write some Python code that opens this file and prints first the `odd` lines and then the `even` lines.

- Your result should look like this:

```
_3 May. Bistritz._--Left Munich at 8:35 P. M., on 1st May, arriving at
Vienna early next morning; should have arrived at 6:46, but train was an
hour late. Buda-Pesth seems a wonderful place, from the glimpse which I
got of it from the train and the little I could walk through the
streets. I feared to go very far from the station, as we had arrived
late and would start as near the correct time as possible. The
impression I had was that we were leaving the West and entering the
East; the most western of splendid bridges over the Danube, which is
here of noble width and depth, took us among the traditions of Turkish
rule.
```

#####

##### Task 4

Open the file [src/data/task4.txt](src/data/task4.txt) and print the text found between the positions 1622 and 1634 (both included).

- Your result should look like this:

```
the dark side
```

#####

##### Task 5

Open the file [src/data/task5.txt](src/data/task5.txt) and print the first line and the amount of characters in this line (the line break does not count).

> You are not allowed to use the `len()` function, use the reading position instead.

- Your result should look like this:

```
We left in pretty good time, and came after nightfall to Klausenburgh.

70
```

#####

##### Task 6

Now open the file [src/data/task6.txt](src/data/task6.txt) and print a list of integers representing the amount of characters per line. The order in the list will be the order of the lines.

> Again, you are not allowed to use the `len()` function.

- Your result should look like this:

```
[69, 72, 72, 68, 70, 66, 68, 72, 70, 71, 71, 73, 73, 19]
```

#####

##### Disclaimer

The contents are fragments from the book Dracula, *by Bram Stoker*.
