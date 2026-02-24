def remove_duplicate(numbers):
    result = []
    for num in numbers:
        if num not in result:
            result.append(num)
    return result
def main_function():
    print("I m removing the duplicate numbers from a list ")
    input_List=[1,2,3,4,2,5,6,7,8,9]
    print("The list with duplicates is:", input_List)
    print("The list after the removing duplicates is:",remove_duplicate(input_List))

main_function()