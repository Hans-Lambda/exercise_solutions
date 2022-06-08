<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [My Simple Canvas App](#my-simple-canvas-app)
  - [The Shapes Classes](#the-shapes-classes)
  - [The Canvas Class](#the-canvas-class)
  - [Run the main](#run-the-main)
  - [Extra](#extra)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# My Simple Canvas App

A Canvas is an area in an application where users can draw shapes and insert images
in drawing applications. Let’s write a program to implement the mechanics behind a
simple Canvas. 

## The Shapes Classes

This time, we are going to focus on the shapes. Every shape can be represented as a
class like Circle, Rectangle, Square, etc. They will have attributes; a rectangle
would need height and width attributes, while a circle a radius. Each shape has its
specificities, and they need to be considered when creating the class.

Forms also have operations (methods), and you will need to implement the following
methods for each shape class:

- One to calculate the area
- Another to calculate the perimeter
- One to print on the screen a summary of the shape, attributes, area, and perimeter.

## The Canvas Class

Write a class called Canvas. The class must have an attribute called Shapes which is
a list of shapes that starts empty. The class Canvas must have methods to do the following:

- Add a new shape to the canvas
- Remove a shape to the canvas
- Print the canvas, this means calling print from every shape object in the list of shapes.

## Run the main

You will find in the exercises folder a `main.py` file. It creates a Canvas and adds some 
shapes to it, and it also prints the canvas. In the end, you must be able to run this file using your classes, not that the file contains errors. It is importing files that do not exist, these files are the files you are going to create.

## Extra

After you finish earlier, implement a menu in the `main.py`, so that the user can do the following actions:

- Add a shape of his/her choice.
- Print the current state of the canvas, calling `canvas.print()`
- Reset the canvas (delete all the shapes)
