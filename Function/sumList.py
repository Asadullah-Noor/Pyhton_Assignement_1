def sumList(num):
    total=0
    if num>0:
        for i in range(1,num+1):
            total+=i
        return total
    else:
        return "Invalid input"
print("I m calculating the sum of numbers in a list")
print(sumList(3))