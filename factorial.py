def factorial(n):
    if n==0 or n==1:
        return 1

    else:
        return n *factorial(n-1)


data=5
result =factorial(data)


print(f"The factorial of {data} is:{result} ")