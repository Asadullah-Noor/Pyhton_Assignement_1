#High order function that will take another function function as an argument
def greet(name):
    print(f"Hello, {name}!")
def process_user(func,name):
    return func(name)
send=process_user(greet,"Asadullah Noor")
