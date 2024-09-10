# Write a python script to print the multiplication table of a given number up to the specified limit using a for loop.

def print_multiplication_table(number, limit):
    print(f"Multiplication table for {number} up to {limit}:")
    for i in range(1, limit + 1):
        result = number * i
        print(f"{number} x {i} = {result}")


try:
    number = int(input("Enter the number for which you want the multiplication table: "))
    limit = int(input("Enter the limit up to which you want the table: "))
    
    
    print_multiplication_table(number, limit)
except ValueError:
    print("Please enter valid integers for number and limit.")
