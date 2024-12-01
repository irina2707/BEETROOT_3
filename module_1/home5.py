#Task1
# import random
# random_number = random.randint(1,10)

# while random_number!=None: 
#  user_number = int(input("Guess number: "))
#  if random_number > user_number:
   
#     print("Your number is smaller")
#  elif random_number < user_number:
#     print("Your number is bigger")
#  elif random_number == user_number:
#    print("You are winner!")   
# else:
 
#     print("Don't follow rules")
 
 
 #Task 2
# user_name=str(input("Write your name: "))
# user_age =int(input ("Write your age: "))
# greeting_message = f"Hello {user_name} ,on your next birthday you’ll be {user_age+1} years "
# print(greeting_message)


#Timport random
# import random
# user_string = input("Write your string: ")

# count = 0
# while count < 5:
#     random_string = ''.join(random.choice(user_string) for _ in range(len(user_string)))  
#     print(random_string)
#     count += 1
 
import random
input_string = input("Enter a string: ")
  
    
characters = list(input_string)
    
random_combinations = set() 
count = 0

while count < 5:
       
        random.shuffle(characters)
       
        random_string = ''.join(characters)
        
       
        if random_string not in random_combinations:
            random_combinations.add(random_string)
            print(random_string)  
            count += 1

