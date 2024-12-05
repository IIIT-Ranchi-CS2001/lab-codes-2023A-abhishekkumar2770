user_input = input("Enter a string: ")
user_input = user_input.replace(" ", "").lower()

if user_input == user_input[::-1]:
    print("The input string is a palindrome")
else:
    print("The input string is not a palindrome")
