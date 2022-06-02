def grocery():
    return ['tomato', '2.50 €', 'Apples', '2.00 €', 'bread', '1.99 €', 'meat', '4.99 €', 'pasta', '1.69 €',
            'Oil', '4:99 €', 'frozen_food', '1.99 €']


def milk_products():
    return ['Cheese', '2.34 €', 'milk', '1.29 €', 'cream', '1.50 €', 'butter', '1.49 €', 'yogurt', '0.70 €']


def candies():
    candies_menu = ['Haribo', '0.99 €', 'Bonbons', '0.80 €', 'Mars', '0.90 €']
    return candies_menu


def health():
    return ['soap', '1.09 €', 'toothpaste', '1.99 €', 'shampoo', '2 €', 'vitamins', '1.89 €',
            'Toilet paper', '2.69 €']


def drinks():
    return ['Cola', '0.90  €', 'sprite', '0.89  €', 'icetea', '0.79  €',
            'juice', '1.39  €', 'alcohol FREE bear', '2.90 €']


if __name__ == '__main__':
    sections = ['grocery', 'milk_products', 'candies', 'health', 'drinks']
    sections_menus = [grocery(), milk_products(), candies(), health(), drinks()]
    help_sections = ['grocery', 'milk_products', 'candies', 'health', 'drinks']
    print(f'select a section of the menu (selected items can not be considered again) : {sections} ')
    selected_section = input(': ')

    while selected_section not in sections:
        print("Error: section dos not exist..")
        print(f'select an existing section of the menu: {sections} ')
        selected_section = input()

    ind = sections.index(selected_section)
    print("ind =", ind)
    help_sections_menus = sections_menus[ind]
    items_menu = help_sections_menus[0::2]
    price_menu = help_sections_menus[1::2]

    print(f"help_sections_menus +{help_sections_menus}")
    print(f"help_items_menu + {items_menu}")
    print("help_price_menu", price_menu)

    print(f'select an item of the menu: {items_menu}')
    item = input(' : ')
    ind_1 = items_menu.index(item)
    item_price = price_menu[ind_1]
    print("ind_1 = ", ind_1)
    print("item_price = ", item_price)

    for i in range(5):
        if i != ind:

            if selected_section == sections[i]:
                help_sections_menus = sections_menus[i]
                items_menu = help_sections_menus[0::2]
                price_menu = help_sections_menus[1::2]

                print(f"help_sections_menus +{help_sections_menus}")
                print(f"help_items_menu + {items_menu}")
                print("help_price_menu", price_menu)

                print(f'select an item of the menu: {items_menu}')
                item = input(' : ')
                ind_1 = items_menu.index(item)
                item_price = price_menu[ind_1]
                print("ind_1 NEW= ", ind_1)
                print("item_price NEW= ", item_price)
        # i += 1
