def second_largest(num):
    for i in range(0,len(num)):
        for j in range(i+1, len(num)):
            if num[i]< num[j]:
                second_lrgest=num[i]
                num[i]=num[j]
        return second_lrgest     
       
print(second_largest([1,2,3,4,5,6,7,8,9]))
