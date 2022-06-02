def sum_lists(list1, list2):
    total = []
    for index in range(5):
        total.append(list1[index] + list2[index])
    return total


if __name__ == '__main__':
    l1 = [1, 2, 3, 4, 5]
    l2 = [9, 3, 4, 6, 4]

    result = sum_lists(l1, l2)
    print(result)

    l3 = [4, 2, 3, 4, 5]
    l4 = [9, 2, 5, 6, 4]

    result2 = sum_lists(l3, l4)
    print(result2)
