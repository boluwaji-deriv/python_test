magic_numbers = [3,9]
chances = 3
for i in range(chances): # range(chances) is [0,1,2]
    print("This is an attemp {}".format(i))
    user_number = input("Enter your magic number: ")
    if int(user_number) in magic_numbers:
        print("You got the number right!")
    if not int(user_number) in magic_numbers:
        print("You didn't get it, please try again later.")