def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
    
print("I m calculating the factorial of a number")
print(factorial(5))