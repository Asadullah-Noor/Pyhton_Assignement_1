def even_function(num):
    return f"{num} is even"

def odd_function(num):
    return f"{num} is odd"

def main_function(num):
    if num % 2 == 0:
        return even_function(num)
    elif num % 2 != 0:
        return odd_function(num)
    else:
        return "Invalid input"
print("I m checking the even and odd numbers")
print(main_function(4))
print(main_function(7))