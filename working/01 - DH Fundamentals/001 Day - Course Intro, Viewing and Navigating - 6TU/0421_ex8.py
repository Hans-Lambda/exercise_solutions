import sys

g = {"Vegetables": 2.80, "Fruits": 3.60, "Herbs": 5.50}
m = {"Yoghurt": 1.50, "Cheese": 4.10, "Eggs": 2.75}
c = {"Chocolate": 2.10, "Chips": 0.75, "Schnapspralinen": 4.50}
h = {"Toothpaste": 2.25, "Aspirin": 7.00, "Bandages": 9.90}
d = {"Beer": 1.60, "Wine": 4.90, "Liquor": 9.50}
s = {"Groceries": g, "Milk Products": m, "Candies": c, "Health": h, "Drinks": d, "Exit": 1}


def menu():

    global shopping_cart
    print("Which section would you like to visit?")
    for k, v in s.items():
        print(str((list(s.keys()).index(k)) + 1) + " ", k)
    choice = int(input("Please type the corresponding number: "))

    if choice not in [1, 2, 3, 4, 5, 6]:
        print("You have to type a number between 1 and 6")
        menu()

    if 1 <= choice <= 5:
        item = buy(choice)
        print(f"{item[2]} {item[0]} added to your shopping cart")
        shopping_cart = check_if_present(item, shopping_cart)
        print(shopping_cart)
        menu()

    else:
        total = 0
        for item in shopping_cart:
            total += item[1] * item[2]
            print("\n***** BILL *****")
            print(f"{item[0]}, Price {item[1]} EUR, Amount: {item[2]}")
        print(f"Total: {'{:.2f}'.format(round(total, 2))} EUR")
        sys.exit()


def buy(choice):

    print(f"Welcome to the {(list(s)[choice - 1])} section. The following products are available:")
    for k, v in (list(s.values())[choice - 1]).items():
        print(str((list((list(s.values())[choice - 1]).keys()).index(k)) + 1) + " ", k + ", Price:", v, "EUR")

    prod = int(input("Please type the product number: "))
    if prod not in [1, 2, 3]:
        print("You have to type a number between 1 and 3")
        buy(choice)
    else:
        amount = int(input("Please type the amount: "))
        item = [(list(list(s.values())[choice - 1])[prod - 1]), (list((list(s.values())[choice - 1]).values())[prod - 1]), amount]
        return item


def check_if_present(item, cart):

    for i in cart:
        if i[0] == item[0]:
            i[2] = i[2] + item[2]
            break
    else:
        cart.append(item)
    return cart


if __name__ == '__main__':
    shopping_cart = []
    print("Welcome to the super strange store!")
    menu()

# To Do: insert error management for section and item choice, for example number out of range
