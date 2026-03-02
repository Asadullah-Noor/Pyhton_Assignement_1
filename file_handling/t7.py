import json
try:
    with open('new_json.json','r')as f:
        users=json.load(f)
except FileNotFoundError:
    users=[]
except json.JSONDecodeError:
    users=[]
name=input("Enter your name here :")
age=input("Enter the age here:")
users.append({"Name":name,"Age":age})
try:
    with open('new_json.json','w') as f:
        json.dump(users,f,indent=4)
        print("Data Succesfully Printed!")
except Exception as e:
    print("Data is not wrote")

    