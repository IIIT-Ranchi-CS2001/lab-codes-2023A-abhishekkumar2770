
input_string = input("Enter a string: ")
character_to_count = input("Enter a character to count: ")

count = 0

for char in input_string:
    
    if char == character_to_count:
        count += 1
print(f"The character '{character_to_count}' appears {count} times in the string.")
