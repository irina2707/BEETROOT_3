#Task1.1
# list1 = [2,4,5,67,54,7,8]
# list1.append(54)
# print(list1)
#Task1.2 
# list1=[2, 4, 5, 67, 54, 7, 8, 54]
# index_to_remove =4
# list1.pop(index_to_remove)
# print("The list is:",list1)

  
#Task1.3
# list1=[2, 4, 5, 67, 54, 7, 8, 54]

# sum=0
# i = 0
# while i < len(list1):
#  sum+=list1[i]
#  i+=1
# print(sum) 
#Task1.4
# list1=[2, 4, 5, 67, 54, 7, 8, 54]
# max_element = max(list1)
# min_element = min(list1)
# print("The max element is:",max_element)
# print("The min element is:",min_element)
#Task2.1
# list2=["str","asd","dsu","cdr"]
# for i in list2:
#   print(i)
#Task2.2
# list1=[2, 4, 5, 67, 54, 7, 8, 54]
# for i in list1:
#   if list1[i]%2!=0:
#     continue
# print(i) 
#Task 2.3

# list1=[2, 4, 5, 67, 54, 7, 8, 54]

# sum=0
# i = 0
# while i < len(list1):
#  sum+=list1[i]
#  i+=1
#  avar_in_list1=sum/len(list1)
# print(avar_in_list1) 


#Task 2.4
# list3=["fdg","mouse","brain","beer"]
# for i in list3:
#   print(len(i))


#Task 3.1
# tuple1 = (4,5,76,65,44)
# tuple1.append(7)
# print(tuple1)

#Task 3.2
# tuple2= ("fdg","mouse","brain","beer","cat","rat")
# list_from_tuple = list(tuple2)
# list_from_tuple.append("fox")

# new_tuple2=tuple(list_from_tuple) 
# print("The tuple is:",new_tuple2)
# Створення кортежу з рядками
# my_tuple = ("apple", "banana", "cherry")

# # Перетворення кортежу на список
# my_list = list(my_tuple)

# # Додавання нового елемента до списку
# my_list.append("orange")

# # Перетворення списку назад на кортеж
# new_tuple = tuple(my_list)

# print("Оригінальний кортеж:", my_tuple)
# print("Новий кортеж:", new_tuple)

#Task 3.3
# my_tuple = ("apple", "banana", "cherry")
# for i in my_tuple:
#   print(i)

#Task 3.4
# tuple3 = (4,5,76,65,44,44,44)
# x = tuple3.count(44)
# print(x)


# Task 4.1
# set1 ={2,4,6,7,8,9,10}
# set1.add(77)
# print(set1)

# Task 4.2
# set1 ={2,4,6,7,8,9,10}
# item1_to_remove =4
# set1.remove(4)
# print(set1)
# item2_to_remove =16
# set1.remove(16)
# print(set1)


#Task 4.3 
# set2= {"apple", "banana", "cherry"}
# set3={"apple","mango","lemon"}
# z= set2.isdisjoint(set3)
# print(z)


# Task 4.4
# set2= {"apple", "banana", "cherry"}
# for i in set2:
#   if i == "banana":
#    print(True)
#   else:
#     print(False)


#Task 5.1
number_list =[2,4,6,77,8,9,15]
my_set=set()
for number in number_list:
   my_set.add(number)
print("The set is:",my_set)


#Task5.3

# set3=set(range(1,11))
# for number in list(set3):
#   if number % 2 == 0:
#     set3.remove(number)
# print("The set is:",set3)


# numbers_set = set(range(1, 11))

# # Видалення всіх парних чисел за допомогою циклу for
# for number in list(numbers_set):  # Перетворюємо на список, щоб уникнути зміни множини під час ітерації
#     if number % 2 == 0:
#         numbers_set.remove(number)

# print("Множина після видалення парних чисел:", numbers_set)