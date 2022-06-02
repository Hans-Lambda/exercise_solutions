# Task 1
# Open the file src / data / task1.txt and print its entire content with the least amount of instructions possible.
# Make sure the file is closed before the script finishes.
def task1():
    with open("task1.txt") as file:
        print(file.read())

# Task 2
# Output the amount of ToDos written in the file src/data/task2.txt.
def task2():
    with open("task2.txt") as file:
        print(len([x for x in file.readlines()][2:]))

# Task 3
# Open the file src/data/task3.txt and print its entire content as you did on Task 1.
# This text has been manipulated so that it only reads well if we print the odd lines first and then the even lines.
# Write some Python code that opens this file and prints first the odd lines and then the even lines.

def task3():
    with open("task3.txt") as file:
        file = file.readlines()

        print("".join(file[::2] + file[1::2]))

        print("".join([x for x in file if file.index(x) % 2 == 0]) + "".join([x for x in file if file.index(x) % 2 != 0]))

        # missing part2
        for number, line in enumerate(file, 1):
            if number % 2 != 0:
                print(line, end="")

    # Task 4
# Open the file src/data/task4.txt and print the text found between the positions 1622 and 1634 (both included).

def task4():
    with open("task4.txt") as file:
        print(file.read()[1622:1635])

# Task 5
# Open the file src/data/task5.txt and print the first line and the amount of
# characters in this line (the line break does not count).

def task5():
    with open("task5.txt") as file:
        file = file.readlines()[0]
        print(f"{file}\n{file.index(file[-1])}")

# Task 6
# Now open the file src/data/task6.txt and print a list of integers representing the amount of characters per line.
# The order in the list will be the order of the lines.

def task6():
    with open("task6.txt") as file:
        # lines = file.readlines()
        # print(len(lines[0]))
        # print(len("Having had some time at my disposal when in London, I had visited the"))
        # print([len(x) for x in lines])
        # print([x.index(x[-1]) + 1 for x in lines])

        lines = file.readline()
        result = []
        counter = 0
        for line in lines:
            if line != "\n":
                counter += 1
        result.append(counter)
        print(result)






if __name__ == '__main__':
    #task1()
    #task2()
    #task3()
    #task4()
    #task5()
    task6()
    pass
