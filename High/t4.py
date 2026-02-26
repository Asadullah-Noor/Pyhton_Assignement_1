def myFilter(func,lit):
    result=[]
    for item in lit:
            result.append(func(item))
    return result
def isEven(num): return num*2
numbers=[1,2,3,4,5,6,7,8,9,10]
print(myFilter(isEven,numbers))