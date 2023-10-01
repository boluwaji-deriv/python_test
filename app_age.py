age = input('Enter your age here: ')
name = input('Enter your name here: ')
message = 'You have lived for '
age_in_secs = int(age) * 365 * 24 * 60 * 60 
output = "You have lived for {} seconds. This correspond to {} years. This code was writing by {}".format(age_in_secs, age, name)
print(output)

