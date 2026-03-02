import json
size=3
    #  file Openinng with Exception Hanlding
try:
    with open('mini.json','r') as f:
        user=json.load(f)
except FileNotFoundError:
    user=[]
    print("File not found error generated here")
except json.JSONDecodeError:
    user=[]
    # Input handling 
name=input("Enter Your Name here :")
marks=[]
for i in range(size):
    while True:
       try:
         mark=int(input(f'Enter Your {i+1} Book makrs :'))
         marks.append(mark)
         break
       except ValueError:
          print("Value must be in string formate!")
average=sum(marks)/len(marks)
user.append({"Name":name,
             "Marks":marks,
             "Average":average})
print("Student added successfully!\n")
print("All Students:")
for student in user:
    print(student)
    #  Search Handling
Search_name=str(input("Search By name :"))
found=False
for student in user:
    if student["Name"].lower()==Search_name.lower():
      print("Student Founded")
      print(student)
    elif not found:
         print("Student is not found")
#  -------------- Save File-----------------
try:
    with open('mini.json','w') as file:
        json.dump(user,file, indent=4)
        print("Data saved successfully !")
except Exception as e:
    print("Error",e)