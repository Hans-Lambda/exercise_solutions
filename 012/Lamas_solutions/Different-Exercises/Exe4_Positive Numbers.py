if __name__ == '__main__':
    print("this code counts the number of the positive values which you give.\n"
          "Please enter either positive or negative integer but no null")
    count = 1
    total = 0

    while count <= 6:
        a = int(input(f"Enter the {count}. integer = "))
        if a > 0:
            total = total + 1
        count = count + 1
    print(f"{total} positive values")


