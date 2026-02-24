def voiwel_counter(string):
    vowel="aeiouAEIOU"
    count=0
    for char in string:
        if char in vowel:
            count+=1
        return count


def main_function():
    print("I m counting the vowels in a string")
    input_string="Hello World"
    print("Number of vowels in the string is:", voiwel_counter(input_string))
main_function()