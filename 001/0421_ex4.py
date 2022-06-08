def pos_val(l):
    res = [element for element in l if element > 0]
    print(res)
    print(f"{len(res)} positive values")


if __name__ == '__main__':
    lst = []
    for i in range(0, 6):
        ele = int(input("Type number: "))
        lst.append(ele)
    pos_val(lst)
