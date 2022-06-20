from view import MainMenu, SubMenu
from crap import BullshitGenerator


if __name__ == '__main__':

    main_menu = MainMenu()
    sub_menu = SubMenu()

    bullshit_generator = BullshitGenerator()
    bullshit_generator.populate()

    option = -1
    while option != 0:

        option = main_menu.main_menu()

        if option == 1:
            sub_menu.rent_bike_menu()
        elif option == 2:
            sub_menu.return_bike_menu()
        elif option == 3:
            sub_menu.list_bikes_menu()
        elif option == 4:
            sub_menu.report_menu("Pending")
        elif option == 5:
            sub_menu.report_menu("Closed")
        elif option == 6:
            sub_menu.add_bike_menu()
        elif option not in [0, 1, 2, 3, 4, 5, 6]:
            print("Please choose a valid option or exit!")
