def count_frequency(number):
    frequency = {}
    for item in number:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    print(frequency)
list=input_list=[1,2,3,4,5,6,7,8,9,9,10]
count_frequency(list)