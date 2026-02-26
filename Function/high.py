def greet(name):
    return f"Hello, {name}"

def process_user(func, name):
    return func(name)

print(process_user(greet, "Alice"))