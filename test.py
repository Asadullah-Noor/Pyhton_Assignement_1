print("I m making the Hope to skill assignment#1")
input_string=input("Enter the string here:__________________")
reversed_string=""
vowevls="aeiouAEIOU"
count_vowles=0
for i in range(len(input_string)-1,-1,-1):
      if input_string[i] in vowevls:
            count_vowles+=1
      reversed_string+=input_string[i]
print("Reversed string is:",reversed_string)
print("Number of vowels in the reversed string is:",count_vowles)