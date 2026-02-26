def Reducer(func, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        value = next(it)
        print("No initializer provided, using first element:", value)
    else:
        value = initializer
        print("Initializer provided:", value)
    for element in it:
        value = func(value, element)
    return value
def add(x, y):
    return x + y
numbers = [5, 2, 3, 4, 5]
result = Reducer(add, numbers)
print("Result of reduction:", result)