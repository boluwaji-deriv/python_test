import random           # import random module

def ask_user_and_check_number():
    user_number = int(input("Enter a number between 0 and 9: "))
    if user_number in magic_numbers:
        return "You got the number right!"
    if user_number not in magic_numbers:
        return "You didn't quite get it."
magic_numbers = [random.randint(0,9), random.randint(0,9)] # create a list with two random numbers
# Path: magic_number.py
# magic_numbers = [3,9]

def run_program_x_times(chances):
    for attempt in range(chances): # range(chances) is [0,1,2]
        print("This is attempt {}".format(attempt))
        print(ask_user_and_check_number())
run_program_x_times(6)

    