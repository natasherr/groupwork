def max_value(num1, num2, num3, num4, num5):
    numbers = []
    for x in range(5):
        while True:
            try :
                # Prompts the user to enter a number.
                num = float(input(f"Enter number {x}:"))
                numbers.append(num)
                break
            except ValueError:
                print ("Invalid Input. Please enter a numeric value.")
                # Handle invalid input (non-numeric values.)
                print (f"The maximum value is : {max(numbers)}")

max_value(1,2,3,4,5)