def is_sorted_ascending(numbers):
    return numbers == sorted(numbers)

numbers = [2,5,1,3,6,9,7,10]
print(is_sorted_ascending(numbers))
# Output : False
numbers = [1,2,3,5,6,7,9,10]
print(is_sorted_ascending(numbers))
# Output : True