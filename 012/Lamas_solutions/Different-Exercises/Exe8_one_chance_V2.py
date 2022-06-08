# The "One Chance supermarket" is very strange. You go through a corridor divided in sections, and you have only one
# opportunity to pick up one single product in each section. It has 5 sections, grocery, milk products, candies,
# health, and drinks. Write a program that will ask the client what the client wants to take in each section. Each
# section show a menu, then te user select one product, and the menu for the next section is presented to the user,
# until the last menu. Print on the screen the price of the selected product, each time the user selects one product.
# Create one function per section, example def grocery(), def milk_products(), etc.
def grocery():
    return ['tomato', '2.50 €', 'Apples', '2.00 €', 'bread', '1.99 €', 'meat', '4.99 €', 'pasta', '1.69 €',
            'Oil', '4:99 €', 'frozen_food', '1.99 €']


def milk_products():
    return ['Cheese', '2.34 €', 'milk', '1.29 €', 'cream', '1.50 €', 'butter', '1.49 €',  'yogurt', '0.70 €']


def candies():
    candies_menu = ['Haribo', '0.99 €', 'Bonbons', '0.80 €',  'Mars', '0.90 €']
    return candies_menu


def health():
    return ['soap', '1.09 €',  'toothpaste', '1.99 €', 'shampoo', '2 €',  'vitamins', '1.89 €',
            'Toilet paper', '2.69 €']


def drinks():
    return ['Cola', '0.90  €',  'sprite', '0.89  €',  'icetea', '0.79  €',
            'juice', '1.39  €',  'alcohol FREE bear', '2.90 €']


if __name__ == '__main__':
    sections = ['grocery', 'milk_products', 'candies', 'health', 'drinks']
    sections_menus = [grocery(), milk_products(), candies(), health(), drinks()]
    help_sections = ['grocery', 'milk_products', 'candies', 'health', 'drinks']
    for i in (1, 2, 3, 4, 5):

        print(f'select a section of the menu (selected items can not be considered again) : {sections} ')
        selected_section = input(': ')
        while selected_section not in sections:
            print("Error: section dos not exist..")
            print(f'select an existing section of the menu: {sections} ')
            selected_section = input()

        if selected_section == sections[i-1]:
            help_sections_menus = sections_menus[i-1]
            help_items_menu = help_sections_menus[0::2]
            help_price_menu = help_sections_menus[1::2]

            print(f"help_sections_menus +{help_sections_menus}")
            print(f"help_items_menu + {help_items_menu}")
            print("help_price_menu", help_price_menu)

            print(f'select an item of the menu: {help_items_menu}')
            item = input(' : ')
            ind = help_items_menu.index(item)
            item_price = help_price_menu[ind]
            print(ind)
            print("item_price = ", item_price)

