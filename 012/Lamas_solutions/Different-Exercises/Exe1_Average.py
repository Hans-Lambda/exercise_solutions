def weighted_average(a, b, c):
    # return "{: .5f}".format((a * 3.5 + b * 7.5 + c * 8) / 19)
    return (a * 3.5 + b * 7.5 + c * 8) / 19


if __name__ == '__main__':
    A = round(float(input("Enter the first Grade: A= ")), 1)
    while A < 0 or A > 10:
        print("this is not valid value of a grade..it should be between 0 and 10")
        A = round(float(input("Enter the first Grade again A= ")), 1)
    B = round(float(input("Enter the second Grade: B= ")), 1)
    while B < 0 or B > 10:
        print("this is not valid value of a grade.....it should be between 0 and 10")
        B = round(float(input("Enter the second Grade again B= ")), 1)

    C = round(float(input("Enter the third Grade: C= ")), 1)
    while C < 0 or C > 10:
        print("this is not valid value of a grade.....it should be between 0 and 10")
        C = round(float(input("Enter the third Grade again C= ")), 1)

    # print("AVERAGE = ", weighted_average(A, B, C))
    print(f"AVERAGE = {weighted_average(A, B, C): .5f}")
