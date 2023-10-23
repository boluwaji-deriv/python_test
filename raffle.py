import random
def menu():
    # Ask player for numbers
    user_numbers = get_user_numbers()
    # Calculate lottery numbers
    raffle_numbers = create_raffle_numbers()
    # Print out the winnings
    matched_numbers = user_numbers.intersection(raffle_numbers)
    print("You matched {}. You won ${}!".format(matched_numbers, 100 ** len(matched_numbers)))
    # print(lottery_numbers)
    # print(user_numbers)
    # print(matched_numbers)

# User can pick 6 numbers
def get_user_numbers():
    number_csv = input("Enter your 6 numbers, separated by commas: ")
    # Now I want to create a set of integers from this number_csv
    number_list = number_csv.split(",")
    integer_set = {int(number) for number in number_list}
    return integer_set

# Calculate 6 random numbers (1-20)
def create_raffle_numbers():
    values = set() # Cannot initialise like so: {}
    while len(values) < 6:
        values.add(random.randint(1,20))
    return values
# Then we match the user numbers to the computer numbers
# Calculate the winnings based on how many numbers the user matched
print(get_user_numbers())
    
menu()