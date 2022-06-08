import json
import random


def main():

    photos_file = open('photos.json', 'r')
    photo_list = json.load(photos_file)

    # Task 1
    list_of_10_photos = photo_list[0:10]
    list_of_100_photos = photo_list[0:100]

    # Task 2
    list_of_10_random_photos = random.choices(photo_list, k=10)
    list_of_100_random_photos = random.choices(photo_list, k=100)

    list_of_1_random_photos = random.choice(photo_list[0:10])
    print(type(random.choice(photo_list[0:10])))


# a = 2
# b = 3
# def add(a, b):
#     return a + b
# def divide(a, b):
#     # return b > 0 and a / b
#     return a / b
# def divide_function(a, b):
#     if b > 0 and a  < 100:
#         return divide(a, b)
# def operation_in_class():
#     # it can be any thing!
#     if divide_function(a, b) and a == 5:
#         print('Successfully divided')
#         # add a print statement that tells us it was successfully
#     else:
#         return add(a, b)
# operation_in_class()


if __name__ == "__main__":
    main()
