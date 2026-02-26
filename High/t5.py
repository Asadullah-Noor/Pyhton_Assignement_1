def func1():
    return "Hello, World!"
def high_order_function(func):
    return func()
print(high_order_function(func1))