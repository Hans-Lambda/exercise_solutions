<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [DCI_Python_Notes - Rules for Collaboration](#dci_python_notes---rules-for-collaboration)
- [To Do](#to-do)
- [1. Resources](#1-resources)
  - [1.1 Cheat Sheets](#11-cheat-sheets)
  - [1.2 Mathias Repos](#12-mathias-repos)
  - [1.3 Week 1 Review - Git basics](#13-week-1-review---git-basics)
  - [1.4 Week 2 Review](#14-week-2-review)
- [2.  Linux](#2--linux)
  - [2.1 General Info](#21-general-info)
    - [2.1.1 Files and Directories](#211-files-and-directories)
    - [2.1.2 File types](#212-file-types)
  - [2.2 Linux Bash](#22-linux-bash)
    - [2.2.1 Maintenance](#221-maintenance)
    - [2.2.2 General](#222-general)
    - [2.2.3 Navigation](#223-navigation)
    - [2.2.4 Attributes](#224-attributes)
    - [2.2.5 Working with Files](#225-working-with-files)
    - [2.2.6 File Compression](#226-file-compression)
- [3. Documentation](#3-documentation)
  - [3.1 Markdown Files](#31-markdown-files)
  - [3.2 README](#32-readme)
- [4. Tools](#4-tools)
  - [4.1 Pandoc](#41-pandoc)
  - [4.2 Doctoc](#42-doctoc)
  - [4.3 Wireshark](#43-wireshark)
  - [4.4 Traceroute](#44-traceroute)
- [5. Github](#5-github)
  - [5.1 General](#51-general)
  - [5.2 Security](#52-security)
  - [5.3 Setup Repo](#53-setup-repo)
  - [5.4 Work on Repo](#54-work-on-repo)
  - [5.5 Collaborate on Repo](#55-collaborate-on-repo)
  - [5.6 Merging](#56-merging)
  - [5.7 IN CASE OF FUCK UP](#57-in-case-of-fuck-up)
    - [5.7.1 Example of Conflict](#571-example-of-conflict)
- [6. HTML](#6-html)
  - [6.1 General Information](#61-general-information)
  - [6.2 Example of Code](#62-example-of-code)
- [h1 to h6 allows for different headings](#h1-to-h6-allows-for-different-headings)
  - [6.3 Output of Code](#63-output-of-code)
- [7. CSS](#7-css)
  - [7.1 General Information](#71-general-information)
  - [7.2 Code Examples](#72-code-examples)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# DCI_Python_Notes - Rules for Collaboration

* make your own branch
* just push additions
* pull request for major changes

# To Do

- [ ] Wireshark
- [ ] Traceroute
- [x] HTML 
- [x] CSS

# 1. Resources

## 1.1 Cheat Sheets

[Bash Cheatsheet](/resources/Linux_bash_cheat_sheet-1.pdf)

[Linux Command line Cheatsheet](/resources/linux_command_line.pdf)

[Markdown Cheatsheet](/resources/markdown-cheatsheet.pdf)

[Git Cheatsheet](/resources/git-cheat-sheet-education.pdf)

[HTML Cheatsheet](/resources/HTML-Cheat-Sheet.pdf)

[CSS Cheatsheet](/resources/css_cheat_sheet.pdf)

## 1.2 Mathias Repos

[Exercise Repo](https://github.com/fbw-p22-e01/exercises)

[Fundamentals Recap ](https://github.com/mathiasbrito-dci/python-course-2022)

[Versioning and Collaboration Cheatsheet](/resources/Versioning_and_Collaboration.pdf)

[The Internet & HTML](/resources/Internet_&_HTML.pdf)

[CSS Basics](/resources/CSS_Basics.pdf)

## 1.3 Week 1 Review - Git basics

[Part 1](https://www.youtube.com/watch?v=pMsvKdrX8Bg)

[Part 2](https://www.youtube.com/watch?v=aDCBwRo8uyI)

## 1.4 Week 2 Review

[Part 1](https://drive.google.com/file/d/1FOWMWnJ00-5Ksuh3cV3ctRutfIoQUlJJ/view)

# 2.  Linux 

## 2.1 General Info

Term|Effect
-------------------------|-------------------------
Bash|basic shell
Editors|Vim, Emacs, Nano

### 2.1.1 Files and Directories

Color|Effect
-------------------------|-------------------------
blue|directory
green|executables
red|packages
white|regular text files

files and directories are case sensitive

### 2.1.2 File types

Ending|File type
-------------------------|-------------------------
.md|Markdown File

## 2.2 Linux Bash

TAB for autocompletion, case sensitive

/* is Wildcard

/^ is STRG

### 2.2.1 Maintenance

Command|Effect
-------------------------|-------------------------
sudo|super user do
sudo apt|
sudo apt search APPLICATION|search for app to install
sudo apt install APPLICATION|install application
sudo apt update|update every application and package
sudo apt list upgradable|list upgradable packages
sudo apt upgrade|upgrade every package
sudo apt autoremove|automatically remove unnecessary package parts

### 2.2.2 General

Command|Effect
-------------------------|-------------------------
--help|get help concerning command
man CMD|open manual for the command
help CMD|show help if available
clear|clear terminal
/search term|search help, manuals, etc
/search term|press n for next occurence of search term

### 2.2.3 Navigation

Command|Effect
-------------------------|-------------------------
pwd|print working directory
cd /FOLDER/|change directory
cd ..|go to parent directory
cd -|got to previously opened directory
cd /|go to /root/
cd ~|got to /home/
arrow up, arrow down|cycle through used commands
ls|show files and folders in directory
ls -la|files and folders with details and hidden files
../|refers to parent directory

### 2.2.4 Attributes

Command|Effect
-------------------------|-------------------------
-i|require confirmation
-r|recursive, affecting all sub folders and files
-f|force command
--help|open help for command
man COMMAND|show the manual

### 2.2.5 Working with Files

Command|Effect
-------------------------|-------------------------
rm|remove files and directories
mkdir|make directory
mkdir -p|make directory with parent folders
touch|create file
cat|show file content directly
less|read file one page at a time
echo "...">FILE|write to file
echo "...">>FILE|apprehend to file
cp file ..|copy file to parent directory
nano FILE|open file in Nano

### 2.2.6 File Compression

Command|Effect
-------------------------|-------------------------
tar -cvf ARCHIVE_NAME.tar FOLDER/|create TAR archive
tar -zcvf ARCHIVE_NAME.tar.gz FOLDER/|create compressed TAR archive
tar xf ARCHIVE|unzip

# 3. Documentation

## 3.1 Markdown Files

Command|Effect
-------------------------|-------------------------
#|main heading
##|2nd level heading
###|3rd level heading
**bold**|bold
*italic*|italic
'highlited'|highlited
[title](link)|show link with title

To include code from different programming languages indent the code by 4 spaces and markdown will recognize it

To display raw code without rendering use:

~~~
"~~~"
put code here.

No citation marks.

They are just there because otherwise Markdown converts them and the example doesn't work. 
"~~~"
~~~

## 3.2 README

* How to use it
* Purpose of Code
* Version
* Features
* To Do

# 4. Tools

## 4.1 Pandoc

Command|Effect
-------------------------|-------------------------
pandoc TEST.txt -o TEST_2.pdf|make a pdf Test_2 of TEST

## 4.2 Doctoc

[Doctoc](https://github.com/thlorenz/doctoc)

Absolutely awesome. Autogenerates table of contents for markdown files.

## 4.3 Wireshark

todo

## 4.4 Traceroute

todo

# 5. Github

## 5.1 General

Command|Effect
-------------------------|-------------------------
.gitignore file in folder|filenames ignored by git
git config –global user.email “email”|set email
git config –global user.name “name”|set name
git config --list|show git config

## 5.2 Security

**ALWAYS SSH SECURITY IN GIT; NOT HTTPS**

Command|Effect
-------------------------|-------------------------
ssh-keygen -t rsa -b 4096 -C "YOUR@EMAIL.COM"|set up RSA key
/home/user/.ssh/id_rsa|where RSA key is saved
id_rsa.pub|public part of key to insert in github

## 5.3 Setup Repo

**ALWAYS GIT INIT FIRST IN FOLDER**

Command|Effect
-------------------------|-------------------------
git init|start tracking folder with git
git branch -M main|rename master branch to main branch
git push -u origin main|push main branch to online repo
git checkout -b NEW_BRANCH|set up new branch
git push -u origin NEW_BRANCH|start tracking online for NEW_BRANCH
git checkout NEW_BRANCH|switch to branch


## 5.4 Work on Repo

Command|Effect
-------------------------|-------------------------
git branch|show branches and the branch currently in
git branch -v|show differences between branches
git branch -d BRANCH|delete branch
rm -rf REPO_FOLDER|remove local copy of repo
git status|show status
git log|show log
git log --graph|show log with graph of branches
git add FILE_or_FOLDER|add tracking
git add .|add everything in folder
git commit|commit added changes to next push
git commit -m “MESSAGE”|commit with message in one line

## 5.5 Collaborate on Repo

* in online repo use settings/collaborators to invite others

Command|Effect
-------------------------|-------------------------
git log -> copy REFERENCE_NUMBER|copy reference number of the version you want to checkout or set back to
git checkout REFERENCE_NUMBER|checkout old version
git clone|make a local clone of repo
git clone git@github.com:mathiasbrito-dci/lets_collaborate.git|git repo address under “code” in repo
git diff OTHER_BRANCH|compare the branch you're in to OTHER_BRANCH
git push -u origin OTHER_BRANCH|push local OTHER_BRANCH to online repo

## 5.6 Merging

Command|Effect
-------------------------|-------------------------
git push -u origin NAME_OF_BRANCH|create a pull request on github to review, discuss and approve
pull request via github|make pull request online
git merge OTHER_BRANCH|when in BRANCH (for example MAIN) use to merge OTHER_BRANCH into BRANCH

## 5.7 IN CASE OF FUCK UP

Command|Effect
-------------------------|-------------------------
git restore|restore from some stage, see documentation
git merge --abort|abort merging, back to before push, possibly solve conflict before

### 5.7.1 Example of Conflict

open conflicting file, you'll see something like this

Example|
-------------------------|
<<< HEAD|
content in MAIN|
===|
content in OTHER_BRANCH|

* then open conflicting file in main
* solve conflict
* then git merge OTHER_BRANCH

# 6. HTML

## 6.1 General Information

* HyperText Markup Language
* developed in 1991 by Tim Berners-Lee
* rendered in browser
* in the beginning static, nowadays dynamic
* regularly accompanied by CSS for styling

[Link to HTML Tag References on w3schools.com](https://www.w3schools.com/tags/default.asp)

## 6.2 Example of Code

~~~
<!--This is a comment-->
<!--html tag introduces html doc-->
<html>
        <head>
                <title>This title is shown as the webpages name in browser tabs</title>
<!--this link adds the reference for CSS styling
href has to include the path to the folder for the CSS file or a valid link to the resource-->
                <link rel="stylesheet" href="style.css"></link>
        </head>
        <body>
<!--here starts the body-->
                <h1>h1 to h6 allows for different headings</h1>
                <p>p allows for paragraphs</p>
                <br>this will include an empty line</br>
<!--this will generate a link with the name-->
                <a href="https://www.reddit.com/">This will show up as name</a>
<!--this will generate a table-->
                <table>
<!--table header-->
                        <tr>
                                <th>header column 1</th>
                                <th>header column 2</th>
                                <th>header column 3</th>
                        </tr>
<!--this will generate table content-->
                        <tr>
                                <td>content column 1 row 1</td>
                                <td>content column 2 row 1</td>
                                <td>content column 3 row 1</td>
                        </tr>
                        <tr>
                                <td>content column 1 row 2</td>
                                <td>content column 2 row 2</td>
                                <td>content column 3 row 2</td>
                        </tr>
                </table>
<!--this will generate a form-->
<!--there are different possible actions to use the data from the form-->
                <form action="mailto:email@example.com">
                        <input type="text"></input>
<!--type=submit will generate a button to send  the data from the form to the destination specified in action=-->
<!--value="Submit" generates what is written on the button-->
                        <input type="submit" value="Submit"></input>
                </form>
        </body>
</html>
~~~

## 6.3 Output of Code

<!--This is a comment-->
<!--html tag introduces html doc-->
<html>
	<head>
		<title>This title is shown as the webpages name in browser tabs</title>
<!--this link adds the reference for CSS styling
href has to include the path to the folder for the CSS file or a valid link to the resource-->
		<link rel="stylesheet" href="style.css"></link>
	</head>
	<body>
<!--here starts the body-->
		<h1>h1 to h6 allows for different headings</h1>
		<p>p allows for paragraphs</p>
		<br>this will include an empty line</br>
<!--this will generate a link with the name-->
		<a href="https://www.reddit.com/">This will show up as name</a>
<!--this will generate a table-->
		<table>
<!--table header-->
			<tr>
				<th>header column 1</th>
				<th>header column 2</th>
				<th>header column 3</th>
			</tr>
<!--this will generate table content-->
			<tr>
				<td>content column 1 row 1</td>
				<td>content column 2 row 1</td>
				<td>content column 3 row 1</td>
			</tr>
			<tr>
				<td>content column 1 row 2</td>
				<td>content column 2 row 2</td>
				<td>content column 3 row 2</td>
			</tr>
		</table>
<!--this will generate a form-->
<!--there are different possible actions to use the data from the form-->
		<form action="mailto:email@example.com">
			<input type="text"></input>
<!--type=submit will generate a button to send  the data from the form to the destination specified in action=-->
<!--value="Submit" generates what is written on the button-->
			<input type="submit" value="Submit"></input>
		</form>
	</body>
</html>

# 7. CSS

## 7.1 General Information

CSS means Cascading StyleSheet. Cascading means, that there can be multiple levels of styling commands for all
kinds of HTML objects. The different CSS selectors have different priorities thus allowing for styling objects in a
general matter and specifying afterwards.

If for example all fonts shall be size 14px and green color in general, this can be overridden for single objects
as well as special commands like padding etc. being added.

The Priorities:

Inline Style > ID Selector > Class Selector > Tag Selector

[Link to CSS References on w3schools.com](https://www.w3schools.com/cssref/default.asp)

[Link to css-tricks.com](https://css-tricks.com/)

[Vertical Alignment techniques](https://www.outsystems.com/blog/posts/css-vertical-align/)

## 7.2 Code Examples

~~~
/*This is a comment*/


Inline Style


/*Inline style is the top priority and will override all style aspects mentioned in other
selectors*/

<body style="background-color: green; ADDITIONAL: STYLE_COMMAND; ANOTHER: STYLE_COMMAND;">


ID Selector


/*The ID selector allows for a unique styling for one element per ID*/

<body id="THIS_IS_AN_ID">

THIS_IS_AN_ID {
	background-color: green;
	ADDITIONAL: STYLE_COMMAND;
	ANOTHER: STYLE_COMMAND;
}


Class Selector


/*The class selector allows to assign the same class to multiple elements, thus styling all
of them in the same way*/

<body class="MY_CLASS">

<h3 class="MY_CLASS">

<table class="MY_CLASS">

/*all of the above elements will get their styling from the MY_CLASS, as long as parts
aren't overridden by higher priority stylings*/

MY_CLASS {
	background-color: green;
        ADDITIONAL: STYLE_COMMAND;
        ANOTHER: STYLE_COMMAND;
}


Tag Selector


/*The tag selector uses a list of HTML tags. All of those elements in the list will receive
the same styling, as long as they aren't overridden*/

h1, h2, p, table {
	background-color: green;
        ADDITIONAL: STYLE_COMMAND;
        ANOTHER: STYLE_COMMAND;
}

/*Every <h1> and <h2> heading, every <p> paragraph and every <table> will receive the same
styling expressed in the class*/

~~~
