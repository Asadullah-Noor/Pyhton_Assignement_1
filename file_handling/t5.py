import json
try:
    with open('Json_file.json', 'r') as f:
        file=json.load(f)
        print(file)
except FileNotFoundError:
    print("File does Not Exist!")
except json.JSONDecodeError:
    print("File is not in vlaid JSON formate")
except Exception as e:
    print("Error is :",e)