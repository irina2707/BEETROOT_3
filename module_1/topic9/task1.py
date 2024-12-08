from greet import greet

def print_greet(name):
  message=greet(name)
  return f"{message}.We are looking for you."

print(print_greet("Fiona"))
