<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Improving the "Super Car Store" System (Extra Assignment)](#improving-the-super-car-store-system-extra-assignment)
  - [Inserting new cars into the list](#inserting-new-cars-into-the-list)
  - [Updating a car](#updating-a-car)
  - [Main Menu](#main-menu)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# Improving the "Super Car Store" System (Extra Assignment)

## Inserting new cars into the list

Write a function that receives a dictionary with information about a new car
and inserts it in the car's list. Read from the user the data of the new car. You will have to:
- Read from the user about the new car.
- Store the data as a dictionary similar to those found in the list in `car.py`
- Insert this new data in the car's list

## Updating a car

Sometimes we need to change the data of a specific record, create a function that receives
the car’s ID, retrieves the record from the car's list, and updates the data. The new data
is given by the user:

- Ask the user for the ID of the car he wants to change.
- find this car's record in the list.
- Using `input` lets the user change the fields of this record.
    - Make sure that the new data is in the list. You can try to retrieve it
      again and check if the data is updated.

## Main Menu

Create the main menu so that the user can choose the operations available:
    
1. Get a car by name
2. Get cars by the number of gears
2. Get cars by Manufacturer
3. Get a car by average consumption
4. Get a car by the year
5. Insert new car
6. Update a car
0. Exit

You have to read the option given by the user and use a sequence of `if...elif`
execute the related function. The menu can be inside a while loop that runs until
the users type 0 to exit; that way, you allow the user to do multiple operations
during the program’s execution.
