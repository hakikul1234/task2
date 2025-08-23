
import math

try:
    number=float(input("Enter any positive number:"))

    if number<=0:
        print("enter a positive number.")

    else:

        square_root=math.sqrt(number)
        natural_log=math.log(number)
        sine=math.sin(number)


        print(f" squre root of {number} is {square_root}:")
        print(f"natural log of {number} is {natural_log}:")
        print(f"sine of {number} is {sine}:")

except ValueError:
    print("Enter a valid number.")
