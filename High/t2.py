def calculator(operation, a, b):
    return operation(a,b)
def add(a,b):return a+b
def multiply(a,b):return a*b
def subtract(a,b):return a-b
print(calculator(add,10,5))
print(calculator(multiply,10,5))
print(calculator(subtract,10,5))