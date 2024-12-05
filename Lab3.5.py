#Write a python script to check whether all the characters present in a string are alphanumeric (uppercase letters, lowercase letters or digits) using for  with else. Print True if all characters are alphanumeric. Otherwise print False.By taking user input
input_string = input("Enter a string: ")

is_alphanumeric = True

for char in input_string:
    
    if not char.isalnum():
        is_alphanumeric = False 
        break  

if is_alphanumeric:
    print(True)
else:
    print(False)
