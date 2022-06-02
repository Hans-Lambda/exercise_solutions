from termcolor import colored
import time


def colored_text(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)


def get_random():
    clk_id1 = time.CLOCK_REALTIME
    t1 = time.clock_gettime_ns(clk_id1)
    return int(str(t1)[-1])


def guess_loop(random_value):
    random_value = get_random()
    users_guess = int(input("Guess a number between " + colored("1 ", "blue") + "and " + colored("10 ", "blue") + colored_text(255, 128, 0, "until ") + "you get it right : "))
    while users_guess is not random_value:
        users_guess = int(input("Wrong!Guess a number between " + colored("1 ", "blue") + "and " + colored("10 ", "blue") + colored_text(255, 128, 0, "until ") + "you get it right : "))
    print("Well guessed!")


if __name__ == '__main__':

    # Task 5
    guess_loop(get_random())
    ask_to_go_on = input((colored("Do you want to try it again?", "blue") + colored("(Yes", "green") + colored("/no) ", "red")))
    if ask_to_go_on in ["Yes", "yes", "y", "Y"]:
        guess_loop(get_random())
    else:
        print(colored_text(0, 255, 255, " Okay! See you again soon!"))
