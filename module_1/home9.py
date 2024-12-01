# Write a function called oops that explicitly raises an IndexError exception when called. Then write another function that calls oops inside a try/except state­ment to catch the error. What happens if you change oops to raise KeyError instead of IndexError?
#Task1
# Write a function called oops that explicitly raises an IndexError exception when called
# def oops( x):


#  if x <0:
          
#       raise IndexError("This is an IndexError raised by oops.")
#  else:
#     print(x)
# # print(oops(-5)) 
    
# # Function that calls oops and handles the exception
# def my_oops(x):
#     try:
#         oops(x)
#     except IndexError :
#         print("Exception:IndexError ")
#     finally:("Program is finished")
# print(my_oops(-7))   
#change oops to raise KeyError instead of IndexError
# def oops1(dict):
#  dict ={
#   'Marina':30,
#   'Petro':23,
#   'Luda':18,
#   'Gena':43}
# person=input("Get age for: ")
# if 'Name'==('Marina','Petro','Luda','Gena'):
#       print(f'{person} is {ages[person]}years old')    

# else:
#    raise KeyError("This is an KeyError raised by oops.")
#Task2
# Write a function that takes in two numbers from the user via input(), call the numbers a and b, and then returns the value of squared a divided by b, construct a try-except block which catches an exception if the two values given by the input function were not numbers, and if value b was zero (cannot divide by zero).
def calculate_number():
    try:
        a=float(input("Write first number(a): "))
        b=float(input("Write second number(b): "))
        result=(a**2)/b
        print(result)
      
    except ValueError:
       print("Error:It is not number")
    #  if b==0:
    except  ZeroDivisionError:
       print("Error:cannot divide by zero")
    finally:
      print("Program is finished")
print(calculate_number())