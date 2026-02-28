def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print("Before the decorator")
        result=original_function(*args,**kwargs)
        print("After the Decorator")
        return result
    return wrapper_function
@decorator_function
def add(a,b):
    return a+b
print(add(10,3))