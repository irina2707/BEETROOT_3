# Create a simple function called favorite_movie, which takes a string containing the name of your favorite movie. The function should then print "My favorite movie is named {name}".
# def favorite_movie(my_film):
#   print(f"My favorite movie is named {my_film}")
  
# film1="Corona"

# print(favorite_movie(film1))

# Create a function called make_country, which takes in a country’s name and capital as parameters. Then create a dictionary from those two, with ‘name’ as a key and ‘capital’ as a parameter. Make the function print out the values of the dictionary to make sure that it works as intended.


# def make_country( name,capital):
#  country_dict={"name":name,"capital":capital}
#  print(country_dict)
#  return country_dict


# make_country("Ukraine","Kyiv")
# make_country("Germany","Berlin")
    
# Create a function called make_operation, which takes in a simple arithmetic operator as a first parameter (to keep things simple let it only be '+', '-' or '*') and an arbitrary number of arguments (only numbers) as the second parameter. Then return the sum or product of all the numbers in the arbitrary parameter. For example:

# the call make_operation('+', 7, 7, 2) should return 16
# the call make_operation('-', 5, 5, -10, -20) should return 30
# the call make_operation('*', 7, 6) should return 42      
def make_operation(operator,*args):
  if operator not in("+","-","*"):
       print("Choose right operator.")               

  if operator=="+":
      result=sum(args)
    
  elif operator=="-" : 
       result=args[0]
       for number in args[1:]:
         result-=number
  elif operator == "*":
    result=1   
    for number in args:
    
        result*=number
  return result      
# print(make_operation("+",4,5,7))
# print(make_operation("*",4,5))  
print(make_operation("-",5,5,-10,-20))            