from rent import RentManagement, Bike
from crap import BullshitGenerator


def main_menu():
    print("1. Rent a Bike")
    print("2. Return a Bike")
    print("3. List Bikes")
    print("4. List Bills")
    print("5. Incoming Report")
    print("6. Add Bike")
    print("0. Exit")
    opt = int(input("Type an option >> "))
    return opt


if __name__ == '__main__':

    bullshit_generator = BullshitGenerator()
    bullshit_generator.populate()
    rent_management = RentManagement()
    bike = Bike()

    option = -1
    while option != 0:

        option = main_menu()

        if option == 1:
            rent_management.rent()
        elif option == 2:
            rent_management.return_bycicle()
        elif option == 3:
            print(rent_management.print_bycycle_list())
        elif option == 4:
            print(rent_management.bills_list())
        elif option == 5:
            print(rent_management.report())
        elif option == 6:
            user = None
            user = rent_management.manage()
            if user is True:
                bike.add_bike(user)
