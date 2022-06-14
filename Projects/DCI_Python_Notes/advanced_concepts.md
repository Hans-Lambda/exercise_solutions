# Decorators

Using a function as variable

        def greeting0():
            print("Hi")

        def greeting(greeting_fun, name):
            greeting_fun(f"Hi {name}")
        
        def greeting1(basic_greeting):
            print(f"{basic_greeting} - This is greeting 1 !")
        
        def greeting2(basic_greeting):
            print(f"{basic_greeting} - This is greeting 2 !")
        
        
        if __name__ == '__main__':
            greeting(greeting1, "Franz")
            greeting(greeting2, "Hans Lambda")

            greeting0()
            nice_greeting = greeting0
            nice_greeting()

# Exceptions - Handling unexpected behaviour

An exception disrupts the normal flow of the program

exception is an event/object that represents an error (derived from base exception class)

Error: action that is incorrect or inaccurate

## General

Exception objects contain:

* Error type /Exception name
* state of the program when the error occurred
* error message - holds information on the error

## Additional info

* ConfigParser

### Terminology

Call Stack

## Throw Exceptions

Error Exceptions can be grouped:

        try:
            condition
        except (ValueError, TypeError):
            print("error")

## Catch Exceptions

## Custom Exceptions

## Built-In Exceptions