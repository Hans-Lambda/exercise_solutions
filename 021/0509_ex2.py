
# Write a program that declares two lists, e.g.
# l1 = [2, 3, 4, 5, 8, 10]
# l2 = [9, 4, 3, 9, 3, 1]
# and creates a new list containing the sum from elements, of both lists, with the same index.

def merge():

    l1 = [2, 3, 4, 5, 8, 10]
    l2 = [9, 4, 3, 9, 3, 1]
    l3 = [x + l2[l1.index(x)] for x in l1]
    print(l3)
    return l3


posts = [
    {
        'author': 'Mathias',
        'title': 'Learn Python',
        'date': '2022-03-22 08:28:47.177870',
        'text': 'This article is about learning Python... bla bla bla....'
    },
    {
        'author': 'John Doe',
        'title': 'Inexistente\'s Drama',
        'date': '1982-12-24 08:28:47.177870',
        'text': 'This text is about the drama of a person that doesn\'t exists'
    },
    {
        'author': 'J. J. Nobody',
        'title': 'I\'m everywhere',
        'date': '1982-12-24 08:28:47.177870',
        'text': 'This text is about how I\'m used as an example in a programming class'
    },
    {
        'author': 'Mathias',
        'title': 'Controlling the Flow of your program!',
        'date': '2022-01-05 08:28:47.177870',
        'text': 'This article is about learning Python... bla bla bla....'
    },
    {
        'author': 'Mathias',
        'title': 'Python Comprehensions',
        'date': '2022-03-22 08:28:47.177870',
        'text': 'This article is about learning Python... bla bla bla....'
    },
]

# Base on the list in file the_blo_db, create a program that asks the user to type a name,
# after that list all the posts written by the author whose name matches the typed name.


def get_posts():
    author = input("Please type the author you wish to research: ")
    print("The posts from Mathias are:")
    [print(f"- {poster['text']}") for poster in posts if poster['author'] == author]
    return [poster["text"] for poster in posts if poster["author"] == author]

# Create a program that declares a list, then asks the user to type an integer value,
# remove from the list all occurrences of this value. Let's say you declare the following list in your program:


def rem_int():
    l_int = [2, 3, 3, 4, 3, 2, 1, 3]
    rem = int(input("Type integer to remove: "))
    print([i for i in l_int if i != rem])
    return [i for i in l_int if i != rem]


products = [
    {
        "name": "apple",
        "category": "fruit",
        "price": 4.3,
    },
    {
        "name": "Croissant",
        "category": "bakery",
        "price": 1.3,
    },
    {
        "name": "Salmon",
        "category": "fish",
        "price": 15.00
    },
    {
        "name": "Soda Max",
        "category": "beverages",
        "price": 0.8
    },
    {
        "name": "Beer",
        "category": "beverages",
        "price": 1
    }
]

# Based on the list of products in file the_supermarket, create a programa that reads from the user a product category,
# after read the discount to apply to the products of a specific category. Then list the name of the products followed
# by the new price


def give_discount():
    cat = input("Please type the product category you would like to adjust: ")
    discount = input("Please type the desired discount: ")
    [print(f"{prod['name']}: {((prod['price'] / 100) * (100 - int(discount)))}") for prod in products if prod['category'] == cat]


if __name__ == '__main__':

    #merge()
    #rem_int()
    #get_posts()
    give_discount()
