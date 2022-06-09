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

[Setup.py / Setup.cfg](url="https://towardsdatascience.com/setuptools-python-571e7d5500f2#:~:text=be%20more%20appropriate.-,The%20setup.,as%20the%20command%20line%20interface")

[Python Docs](url="https://docs.python.org/3/distutils/setupscript.html")

* import setuptools
* STRG + Q : show all (required) attributes

* setup.cfg as alternative
* setup.py will then load setup.cfg

## 9. Templates

[Templates](url="https://github.com/JetBrains/python-skeletons")

* all packages need an __init__.py file

* python setup.py sdist : makes a package from the package named in setup.py?
* packages=find_packages()

* twine : twine upload -r testpypy dist/* : test package on twine
* mailinator
* https://truveris.github.io/articles/configuring-pypirc/
* https://packaging.python.org/en/latest/guides/using-testpypi/

* pip install -e . : pip will look in the current folder for a python package to install in the current virtual environment

* pip freeze : will show all packages installed in the current installation

* example : pip install -i https://test.pypi.org/simple/ Be-A-Man 
* upgrade : pip install -i https://test.pypi.org/simple/ Be-A-Man --upgrade
