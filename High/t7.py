def myFilter(func, myList):
    count=0
    result=[]
    for item in myList:
        if func(item):
            count+=1
            result.append(item)
    return count, result
def isEven(num): return num%2==0
numbers=[1,2,4,5,3,5,3,4,3,4,2,45,2]
count, result = myFilter(isEven,numbers)
print(f"Even numbers count: {count}, Even numbers list: {result}")
