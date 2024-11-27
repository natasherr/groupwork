def print_numbers_skipping_sevens(start, end):
# Prints numbers between start and end, skipping multiples of seven.
    for num in range(start, end +1):
        if num % 7 != 0:
            print(num, end=" ")

start = int(input("Enter the starting integer: "))
end = int(input("Enter the ending integer: "))
print_numbers_skipping_sevens(start, end)