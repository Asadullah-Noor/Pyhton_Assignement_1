def calculator(func,a,b):
    return func(a,b)
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b!=0:
        return a/b
    else:
        return "Cannot divide by zero"
print(calculator(add,10,5))
print(calculator(subtract,10,9))
print(calculator(multiply,10,5))
print(calculator(divide,10,5))
print(calculator(divide,10,0))