import numpy as np
# input list of numbers
input_list = input("Enter a list of numbers (comma separated): ")
# convert to integers
input_list = [int(x) for x in input_list]
# sort using numpy
sort_list = np.sort(input_list).tolist()
print("Numpy version ",np.__version__)
print("Sorted list is:", sort_list)