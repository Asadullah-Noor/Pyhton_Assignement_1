def decorator_function(func):
    def wrapper():
        result=func()
        return result
    return wrapper
@decorator_function
def say_hello():
    print("Today AyatUllah Khamnae Shaheed")
say_hello()
