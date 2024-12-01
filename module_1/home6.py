#Task 1

# The greatest number

# Write a Python program to get the largest number from a list of random numbers with the length of 10

# Constraints: use only while loop and random module to generate numbers
import random 
my_list1=[] 
while len(my_list1)<10:
  my_list1.append(random.randint(1,100))

largest_number=max(my_list1)
print(largest_number)
    #Task2

# Generate 2 lists with the length of 10 with random integers from 1 to 10, and make a third list containing the common integers between the 2 initial lists without any duplicates.

# Constraints: use only while loop and random module to generate numbers
# import random


# my_list1=[]
# my_list2=[]
# my_list3=[]
# while len(my_list1)<10:
#   my_list1.append(random.randint(1,10))
#   my_list2.append(random.randint(1,10))
# for num in my_list1:
#   if num in my_list2 not in my_list3:
#     my_list3.append(num)
# print(my_list3)

#Task3
# Make a list that contains all integers from 1 to 100, then find all integers from the list that are divisible by 7 but not a multiple of 5, and store them in a separate list. Finally, print the list.

# Constraint: use only while loop for iteration

# numbers_list=[]
# i=0
# for i in range (1,101):
#   if i % 7==0 and i%5!=0 :
#     numbers_list.append(i)
#     print(numbers_list)
#   else:
#     continue

# print(numbers_list)