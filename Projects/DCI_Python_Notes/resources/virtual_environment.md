# How to set up a Virtual Environment in Ubuntu

## 1. Create Folder

* which python3 : shows folder
* python3 --version : shows version
* ls /bin - shows everything in bin

## 2. Set up Virtual Environment

* python3 -m venv .venv : m for module, venv for virtual environment : set up venv
* . venv makes it hidden, can be named in other way : .venv_shapes for example
 -> correct path!!

## 3. Activate/Deactivate

* sh .venv/bin/activate : activate venv
* source .venv/bin/activate : activate venv
* deactivate : deactivate venv

## 4. Project and VE Folder separated

* mkdir /SOME_FOLDER/VirtualEnvironment
* python -m venv /SOME_FOLDER/VirtualEvns/YOUR_PROJECT-venv : VirtualEvns : folder name for VE's
* . /SOME_FOLDER/VirtualEvns/YOUR_PROJECT/bin/activate

## 5. Delete VE

* deactivate, then delete folders recursively
* rm -rf

## 6. Additional Info

* .venv/bin/activate : open file to edit paths etc
* keep VE's locally

## 7. Git and VE

* git init in folder
* .gitignore : files/folders Git shall ignore : set up in beginning
* initialize Git with first commit

## 8. Setup.py

* import setuptools
