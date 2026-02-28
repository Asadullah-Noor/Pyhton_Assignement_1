def decorator_function(hello_function_call):
    def wrapper():
        print("Print Before the Function Call")
        hello_function_call()
        print("Print After the Function Call")
    return wrapper
def say_hello():
    print("Hello, World!")
decorator=decorator_function(say_hello)
decorator()
