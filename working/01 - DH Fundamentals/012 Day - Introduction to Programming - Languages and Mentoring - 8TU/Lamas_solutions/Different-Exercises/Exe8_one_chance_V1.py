def grocery():
    return ['tomato', '2.50 €', 'apples', '2.00 €', 'bread', '1.99 €', 'meat', '4.99 €', 'pasta', '1.69 €',
            'Oil', '4:99 €', 'frozen_food', '1.99 €']


def milk_products():
    return ['cheese', '2.34 €', 'milk', '1.29 €', 'cream', '1.50 €', 'butter', '1.49 €', 'yogurt', '0.70 €']


def candies():
    candies_menu = ['haribo', '0.99 €', 'bonbons', '0.80 €', 'mars', '0.90 €']
    return candies_menu


def health():
    return ['soap', '1.09 €', 'toothpaste', '1.99 €', 'shampoo', '2 €', 'vitamins', '1.89 €',
            'Toilet paper', '2.69 €']


def drinks():
    return ['cola', '0.90  €', 'sprite', '0.89  €', 'ice_tea', '0.79  €',
            'juice', '1.39  €', 'bear', '2.90 €']


if __name__ == '__main__':
    sections = ['grocery', 'milk_products', 'candies', 'health', 'drinks']
    sections_menus = [grocery(), milk_products(), candies(), health(), drinks()]  # List of lists
    # help_sections = ['grocery', 'milk_products', 'candies', 'health', 'drinks']
    print(f'select a section of the menu (selected items can not be considered again) : {sections} ')
    selected_section = input(': ')

    while selected_section not in sections:
        print("Error: section dos not exist..")
        print(f'select an existing section of the menu: {sections} ')
        selected_section = input()

    ind = sections.index(selected_section)  # index of the element which is identical with the selected_section
    # print("ind =", ind)
    help_sections_menus = sections_menus[ind]  # e.g. for ind= 0 it gives grocery()
    items_menu = help_sections_menus[0::2]   # takes every second element of the list starting by the first element
    price_menu = help_sections_menus[1::2]   # takes every second element of the list starting by the second element

    """
    print(f"help_sections_menus +{help_sections_menus}")
    print(f"help_items_menu + {items_menu}")
    print("help_price_menu", price_menu)
    """

    print(f'select an item of the menu: {items_menu}')
    item = input(' : ')
    ind_1 = items_menu.index(item)  # index of the element which is identical with 'item'
    item_price = price_menu[ind_1]
    # print("ind_1 = ", ind_1)
    print("ITEM PRICE= ", item_price)

    # separate the number of the string in item_price for the extra Exercise
    """
    s = [int(s) for s in str.split(item_price) if s.isdigit()]
    print(s)
    
    """
    s = []
    for t in item_price.split():
        try:
            s.append(float(t))
        except ValueError:
            pass
    # print(s)
    item_price_float = float(s[0])
    total_price = item_price_float
    for i in range(ind + 1, ind + 5):  # to show the content of the next section
        if i > 4:
            i = i - 5
        # print(i)  # if ind = 1 : i= 2, 3,4,0
        selected_section = sections[i]
        help_sections_menus = sections_menus[i]
        items_menu = help_sections_menus[0::2]
        price_menu = help_sections_menus[1::2]

        """
        print(f"help_sections_menus +{help_sections_menus}")
        print(f"help_items_menu + {items_menu}")
        print("help_price_menu", price_menu)
        """
        print(f'select an item of the menu: {items_menu}')
        item = input(' : ')
        ind_1 = items_menu.index(item)
        item_price = price_menu[ind_1]

        # print("ind_1 NEW= ", ind_1)
        print("ITEM PRICE= ", item_price)
    # extra Exercise
        """
        s = [int(s) for s in str.split(item_price) if s.isdigit()]
        
        """
        s = []
        for t in item_price.split():
            try:
                s.append(float(t))
            except ValueError:
                pass
        # print(s)
        item_price_float = float(s[0])
        total_price = total_price + item_price_float
    print(f"TOTAL PRICE = {total_price: .2f} €")
