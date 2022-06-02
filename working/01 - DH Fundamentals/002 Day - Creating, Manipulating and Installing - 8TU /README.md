<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [DH Fundamentals: Creating, Manipulating, Editing and Installing (8TU)](#dh-fundamentals-creating-manipulating-editing-and-installing-8tu)
  - [Objectives](#objectives)
  - [Content](#content)
    - [Creating and Manipulating Files](#creating-and-manipulating-files)
      - [Topics](#topics)
    - [Installing packages](#installing-packages)
      - [Topics](#topics-1)
    - [Markdown Basics](#markdown-basics)
      - [Topics](#topics-2)
  - [Exercises Exercises](#exercises-exercises)
    - [Exercises](#exercises)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# DH Fundamentals: Creating, Manipulating, Editing and Installing (8TU)

## Objectives

-  In this submodule, learners will be introduced to various methods to create or manipulate files through the terminal and basic markdown authoring.


## Content

### Creating and Manipulating Files

- Methodology: Lecture + Exercises
- Time Units: 2 TU

#### Topics

- Creating directories wiht the command `mkdir
   - `mkdir <folder_name>`
   - `mkdir -p <folder_path>`
- Creating new files with `touch` command
- Editing files with `nano`
   - `nano <filename>`

### Installing packages

- Methodology: Lecture + Exercises
- Time Units: 2 TU

#### Topics

- Installing packages with `apt`
  - `apt search`
  - `apt install`
  - `apt remove`

### Markdown Basics

- Methodology: Lecture + Exercises
- Time Units: 4 TU

#### Topics
  - Basic Authoring (Markdown):
    - Text (bold, italic)
    - Quotes
    - Headlines
    - Lists
    - Pre-formatted text
    - Markdown documentation
  - Converting Markdown to PDF with `pandoc`

## Exercises Exercises

### Exercises

1. **My first programming Project Skeleton**
    - Create a folder with the name of your project (e.g. my_nice_project)
    - Inside this folder create the following folders:
      - "doc": for your project documentation
      - "src": for your project source code
      - "build": for your project build
      - "conf": for the project configurations
    - Inside the "src" directory, create a file "my_app.py"
    - Edit the file and add the following line to it:
      - `print("This is my nice app")`
    - Save and quit the file
    - Execute the following command:
      - `python3 my_app.py`
    - Write the documentation of the project using Markdown
      describing the project.
      - my_nice_project/README.md
2. **Plan your project with Markdown**
    - Create a folder with the name of your final project (e.g. my_nice_project)
    - Inside this project create a README.md to describe your project, you must include:
        - Introduction
        - Related Work and Apps
        - Unique Features
    - Try to use every markdown feature, lists, titles, tables, etc.
    - Build a PDF file out of your Markdown file
    - Create a package of the project folder with tar and send to mathias.brito@digitalcareerinstitute.org
3. **[Creating, Manipulating and Installing (Official Repo Exercises)](https://github.com/dci-python-course/content-materials/tree/9e00f5dfae07c6ebe0c877c61a44771e654f3094/exercises/1_Fundamentals/1.3_Creating-Manipulating-and-Installing)**
