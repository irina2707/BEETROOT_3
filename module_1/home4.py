# Task 1

# String manipulation

# Write a Python program to get a string made of the first 2 and the last 2 chars from a given string. If the string length is less than 2, return instead of the empty string.

# Sample String: 'helloworld'

# Expected Result : 'held'

# Sample String: 'my'

# Expected Result : 'mymy'

# Sample String: 'x'

# Expected Result: Empty String

# Tips:

# Use built-in function len() on an input string
# Use positive indexing to get the first characters of a string and negative indexing to get the last characters
#
# Task 2

# The valid phone number program.

# Make a program that checks if a string is in the right format for a phone number. The program should check that the string contains only numerical characters and is only 10 characters long. Print a suitable message depending on the outcome of the string evaluation.

 

# Task 3

# The math quiz program.

# Write a program that asks the answer for a mathematical expression, checks whether the user is right or wrong, and then responds with a message accordingly.

 

# Task 4

# The name check.

# Write a program that has a variable with your name stored (in lowercase) and then asks for your name as input. The program should check if your input is equal to the stored name even if the given name has another case, e.g., if your input is “Anton” and the stored name is “anton”, it should return True.


# Task 1
# text="ca"
# if (len(text)>=2):
#     print(f"{text[0]}{text[1]}{text[-2]}{text[-1]}")
# else:
#   print("The string is empty.")


#Task 2

# phone_number ="0964222143g"
# chr={0,1,2,3,4,5,6,7,8,9}
# if len(phone_number)== 10 and phone_number.isdigit():
#     print("it is valid number")
# else:
#      print("it is invalid number")
  

# Task 3
# right_answere = '45'
# user_answere = '468'
# if right_answere == user_answere:
#   print("You are right!")
# else:
#   print("You are wrong!")

# Task 4 
storebleName ="iryna"
# a = storebleName.lower()

# inputName ="Iryna"

# b = inputName.lower()

# if(a == b):
#   print("True")
# else:
#   print("False") 
  
  