import json
data={
    "name":"Asadullah",
    "age":30,
    "Class":"BSSE"
}
try:
  with open('Json_file.json','w') as f:
   json.dump(data,f,indent=4)
except Exception as e:
  print("Error with file handling :",e)