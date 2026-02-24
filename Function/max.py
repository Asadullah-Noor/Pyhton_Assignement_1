def function_max(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c
def max(a,b,c):
    return function_max(a,b,c)
print("The maximum number is ",max(5,10,15))
