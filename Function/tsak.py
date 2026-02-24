def my_name(name):
    return f"My Name is {name} and i am a python developer"

def get_name(name):
  return my_name(name)

def get_details(get_name, age, city):
    return f"{get_name} and i am {age} years old and i live in {city}"
print(get_details(get_name("Asadullah Noor"), 25, "New York"))