def myFilter(func,list):
    result=[]
    for item in list:
        if func(item):
            result.append(item)
    return result
def isEven(num): return num%2==0
numbers=[1,2,3,4,5,6,7,8,9,10]
print(myFilter(isEven,numbers))