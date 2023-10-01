age = input('Enter your age here: ')
name = input('Enter your name here: ')
message = 'You have lived for '
# print(age)
# print(message)
age_in_secs = int(age) * 365 * 24 * 60 * 60 
# output = message  + str(age_in_secs) + ' secs' + '. This is equivalent to ' + str(age) + ' years'  
# output = "You have lived for {} seconds".format(str(age_in_secs))
output = "You have lived for {} seconds. This correspond to {} years. This code was writing by {}".format(age_in_secs, age, name)
print(output)

