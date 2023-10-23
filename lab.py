import random
how = int(input("How many time will you like to try this? ")) 
def ask_user_and_check_number():
    magic_numbers = [random.randint(0,9), random.randint(0,9)] # create a list with two random numbers
    user_number = int(input("Enter a number between 0 and 9: "))
    if user_number in magic_numbers:
        return("You have won!")
    else:
        return("You have lost!")


def run_program_x_times(chances):
    for i in range(chances): # range(chances) is [0,1,2]
        print("This is attempt {}".format(i+1))
        print(ask_user_and_check_number())  
run_program_x_times(how)

