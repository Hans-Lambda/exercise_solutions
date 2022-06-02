import random as rd

list1 = ["rock", "paper", "scissor"]
new_line = "\n"


def your_choice():
    chosen = input("choose ;): ")
    if chosen not in list1:
        chosen = input(f"learn how to write u you Dumbass {new_line} And now try Again : ")
    else:
        return chosen
    return chosen


def win(n, chosen):
    s = (chosen == "rock" and n == "scissor")
    k = (chosen == "paper" and n == "rock")
    f = (chosen == "scissor" and n == "paper")
    t = s or k
    return t or f


def game():
    n = rd.choice(list1)

    chosen = your_choice()

    while n == chosen:
        print(f"we pick the same {new_line}, lets Try Again! ")
        n = rd.choice(list1)

        chosen = your_choice()

    else:
        if win(n, chosen):
            print(" YOU WIN !!")
        else:
            print("YOU LOSE Dumbass!!!!!")


def start():
    while True:
        game()

        restart = input("Press any key to RESTART or X to Exit : ")
        if restart == "X" or restart == "x":
            print("goodbye")
            break
        else:
            continue


if __name__ == '__main__':
    start()
