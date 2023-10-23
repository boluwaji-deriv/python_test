def compare_numbers(a, b):
    if a > b:
        return f"{a} is greater than {b}"
    elif a < b:
        return f"{a} is less than {b}"
    else:
        return f"{a} is equal to {b}"

# Calling the function
comparison_result = compare_numbers(5, 9)

# Printing the result
print(comparison_result)
