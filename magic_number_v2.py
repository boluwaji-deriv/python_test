import random           # import random module
minimum = 100
for i in range(10):
    magic_numbers = random.randint(0,100)
    print("The number generated is  {}".format(magic_numbers))
    if magic_numbers <= minimum:
        minimum = magic_numbers
print("The minimum number is {}".format(minimum))