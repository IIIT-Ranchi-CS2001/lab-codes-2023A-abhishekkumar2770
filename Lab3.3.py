# Write a python script to print the first n terms of the Fibonacci series using while loop.

def fibonacci_series(n):

    a, b = 0, 1
    count = 0  
    while count < n:
        print(a, end=' ')
       
        a, b = b, a + b
        count += 1  

n = int(input("Enter the number of terms in the Fibonacci series: "))
fibonacci_series(n)
