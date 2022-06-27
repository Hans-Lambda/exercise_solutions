# Test Driven Development

Suitable libraries: Unittest or Pytest

Most disastrous software errors in history:
https://www.youtube.com/watch?v=AGI371ht1N8

- missing overbar instead of missing hyphen
- calculate safe position in retard units instead of metric units
- obsolete function lowered company stocks
- floating point number bug
- miscalculation of radiation because faulty instruction and limited input parameters
- unexpectedly large values
- coverage module

# Setup

from setuptools import setup, find_packages

this will automatically detect required packages - package=find_packages()

Start application with main:

        entry_points={
                    'console_scripts': ['class-social=class_social.main:main']
                }

## 1. General Setup

    from setuptools import setup, find_packages

    setup(
        version='0.1',
        name='class_social',
        author='DCI Python 2022 Class',
        author_email='franz.bandelin@dci.education',
        description='Class Social is a social network for students',
        url='https://github.com/dci-python-backend-assignments/tdd-class-social',
        license='MIT',
        keywords=['social networks', 'education'],
        requires=[
            'fastapi',
            'uvicorn'
        ],
        package=find_packages(),
        entry_points={
            'console_scripts': ['class-social=class_social.main:main']
        }
    )

## 2. Setup Tests

tox : test execution tool

command: tox

tox.ini

    [envlists]
    test = py38, py39
    
    [testenv]
    minversion = 6.0
    addopts =
    # list of dependencies
    deps =
        pytest
        setuptools
        requests
        coverage
        fastapi
    testpaths =
        tests
    command =
    # -m : run module
        python -m pytest
