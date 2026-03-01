# with open('open.txt','w') as file:
#     file.write("My name is Asadullah Today Ayatullah Khumnai Have been Died")
count=0
with open('open.txt','r')as f:
 
  for i in f:
   count+=1
print(f.readlines())
print("Total line is",count)
