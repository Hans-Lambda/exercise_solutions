
# https://github.com/mathiasbrito-dci/python-course-2022/blob/main/02%20-%20Python/024%20Day%20-%20Strings%20in%20Depth/EXERCISE-4.md

# Task 1

# Functioninator 8000

def inator(string):
    print(((f"{string}inator") if string[-1].upper() in 'BCDFGHJKLMNPQRSTVWXYZ' else (f"{string}-inator")) + f"{len(string)}000")


if __name__ == '__main__':
    inator("FUCK")
