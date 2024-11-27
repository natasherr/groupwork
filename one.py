def unique_numbers(numbers):
# Using set to remove duplicates.
    return list(set(numbers))

numbers = [1,2,2,3,4,4,5,6,7,8,9,10]
print(unique_numbers(numbers))