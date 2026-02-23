   #Question 1: Write a Python program that takes a string as input and reverses 

#Get input from user
print("I m making the Hope to skill assignment#1")
input_string=input("Enter the string here:__________________")
reversed_string=input_string[::-1]
vowevls="aeiouAEIOU"
count_vowles=0

for char in input_string:
      if char in vowevls:
            count_vowles+=1
print("Reversed string is:",reversed_string)
print("Number of vowels:",count_vowles)