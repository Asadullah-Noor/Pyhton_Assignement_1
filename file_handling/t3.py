import json
data={
    "name":"Asadullah",
    "age":23,
    "Class":"Bsse"
}
try:
    with open("data.json", "w") as file:
        json_string = json.dumps(data, indent=4)
        print(json_string)
    #     json.dump(data, file, indent=4)
    # print("Data written successfully!")

except Exception as e:
    print("Error while writing file:", e)