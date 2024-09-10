import math

def find_roots(a, b, c):
    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        print("The roots are:", root1, "and", root2)

    elif discriminant == 0:
        root = -b / (2*a)
        print("The root is:", root)

    else:
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(-discriminant) / (2*a)
        print("The roots are:", str(real_part) + " + i" + str(imaginary_part), "and", str(real_part) + " - i" + str(imaginary_part))

a = int(input("Enter coefficient a: "))
b = int(input("Enter coefficient b: "))
c = int(input("Enter coefficient c: "))

find_roots(a, b, c)
