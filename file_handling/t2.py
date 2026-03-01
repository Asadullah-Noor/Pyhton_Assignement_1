def read_file():
    with open('open.txt','r') as f:
     return f.readlines()

file=read_file()
print(file)