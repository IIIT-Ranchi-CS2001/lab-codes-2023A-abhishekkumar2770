# Write a python script to find the squares of first n natural numbers. Display both the number and the square as shown below. Use while loop

n = int(input("Enter a positive integer n: "))

count = 1

print("Number\tSquare")
while count <= n:
    square = count ** 2
    print(f"{count}\t{square}")
    count += 1
