import json

try:
    with open("users.json", "r") as file:
        users = json.load(file)

except FileNotFoundError:
    users = []

except json.JSONDecodeError:
    users = []

name = input("Enter name: ")
age = int(input("Enter age: "))

users.append({"name": name, "age": age})

try:
    with open("users.json", "w") as file:
        json.dump(users, file, indent=4)
    print("User added successfully!")

except Exception as e:
    print("Error saving data:", e)