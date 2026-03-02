import json

try:
    with open('Json_file.json','r') as f:
        file=json.load(f)
        print("Data successFully Read ")
        print(file)
except FileNotFoundError:
    print("File is Not found")
except json.JSONDecodeError:
    print("File is not VALID json")
except Exception as e:
    print("File reading error genrated :",e)