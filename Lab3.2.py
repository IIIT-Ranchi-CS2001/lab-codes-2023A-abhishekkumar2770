#Write a python script to find the sum of the digits of the given number using a while loop. Display the number.
number = int(input("Enter a number: "))

sum_of_digits = 0
original_number = number 

while number > 0:
    digit = number % 10
    sum_of_digits += digit 
    number //= 10  


print(f"The number is: {original_number}")
print(f"The sum of its digit is: {sum_of_digits}")

