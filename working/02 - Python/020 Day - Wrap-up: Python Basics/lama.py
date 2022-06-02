from termcolor import colored
# from color_constants import colors,RGB
import time
def colored_text(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)
def guess_loop(random_value):
    pass
if __name__ == '__main__':
    # Task 5
    # set_color = RGB(ORANGE)
    # print(colored("text", RGB(255, 128, 0)))
    # print(colored_text(255, 128, 0, 'Hello, World'))
    # i = random_number((1, 5))
    # print(i)
    # random_number((1, 5))
    # print(i)
    # creating real random number using the time in order for the computer to create a new number everytime the user runs the play again
    # clk_id for System-wide real-time clock
    clk_id1 = time.CLOCK_REALTIME
    # Get the time (in nanoseconds) of the above
    # specified clock clk_ids
    # using time.clock_gettime_ns() method
    t1 = time.clock_gettime_ns(clk_id1)
    print("System-wide real-time clock time: ", t1)
    cut_time = str(t1)[-1]
    print(cut_time)
    # new_number = t1 % 16
    # print(new_number)
    # i = 2
    i = int(cut_time)
    print(type(cut_time))
    print(type(i))
    # while i in range(1, 4):
    users_guess = int(input("Guess a number between " + colored("1 ", "blue")+"and "+ colored("10 ", "blue")+ colored_text(255, 128, 0, "until ") + "you get it right : "))
    while users_guess is not i:
        users_guess = int(input("Wrong!Guess a number between " + colored("1 ", "blue")+"and "+ colored("10 ", "blue")+ colored_text(255,128,0,"until ") + "you get it right : "))
    print("Well guessed!")
    ask_to_go_on = input((colored("Do you want to try it again?","blue") +colored("(Yes","green") + colored("/no) ", "red")))
    if ask_to_go_on == "Yes":  # or "yes" or "y" or "Y":
        i = int(cut_time)
        users_guess = int(input("Guess a number between " + colored("1 ", "blue")+"and "+ colored("10 ", "blue")+ colored_text(255,128,0,"until ") + "you get it right : "))
        # want him to go through the wile loop again
    else:
        print(colored_text(0, 255, 255, " Okay! See you again soon!"))