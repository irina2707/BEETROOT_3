# Завдання на практику по функціям:
# Напишіть функцію, яка виводить повідомлення “Hello, world!“. Викличте її.
# Напишіть функцію, яка приймає два числа і повертає їхню суму.
# Напишіть функцію, яка приймає два числа і повертає більше з них.
# Напишіть функцію, яка приймає одне число і повертає його квадрат.
# Напишіть функцію, яка приймає одне число і повертає True, якщо число парне, і False, якщо непарне.
# 6. Напишіть функцію, яка приймає список і повертає кількість елементів у ньому.
# 7. Напишіть функцію, яка приймає список чисел і повертає найбільше число.
# 8. Напишіть функцію, яка приймає список чисел і повертає їхню суму.
# 9. Напишіть функцію, яка приймає список і повертає новий список, що містить лише унікальні елементи (без повторів).
# 10. Напишіть функцію, яка приймає список слів та число n, і повертає список, що містить лише ті слова, які довші за n символів.

#Task1
# def greetings(_greetings="Hello"):
#  print(_greetings)
#  return(_greetings)

# greetings("Hello,world!")

#Task2
# def sum(a,b):
#   sum = a+b
#   print(sum)
#   return(sum)
# sum(8,6)

#Task3
# def max_number(d,e):
#  if d> e:
#    print("Max is d")
#    return(d)
#  else:
#    print("Max is e")
#    return(e)
 
#  max_number(7,45)
#Task4 

# def square_number(c):
#   result= c*c
#   print(result)
#   return(result)
# square_number(7)


#Task5
# def even_number(g):
#   if g%2==0:
#    print("It is even number")
#    return("True")
#   else:
#    print("It is odd number")
#    return("False")
 
 
# even_number(15)


#Task6
# def count_elements_of_list(my_list):
#   len_of_my_list=len(my_list)
#   return len_of_my_list

# input_list=[5,6,9,8,7]
# print(count_elements_of_list(input_list))

#Task7


### Використання вбудованої функції `max`:

# def find_max_number(numbers):
  
#     return max(numbers)

# # Приклад використання:
# numbers_list = [7,8,4,9,10, 5]
# result = find_max_number(numbers_list)
# print(f"Найбільше число у списку: {result}")


### Реалізація без використання `max`:
# def find_max_number(numbers):
#     if len(numbers) is 0:  # Перевірка на порожній список
#         return None

#     max_number = numbers[0]
#     for number in numbers:
#         if number > max_number:
#             max_number = number
#     return max_number


# numbers_list = [6,7,4,8,23]
# result = find_max_number(numbers_list)
# print(f"Найбільше число у списку: {result}")



# def sum_of_numbers(numbers):
#   return sum(numbers)

# numbers_list=[5,66,7,8,9]
# result=sum_of_numbers(numbers_list) 
# print(f"Sum of numbers is:{result} ")






#Task8 
# def sum_of_list_number (numbers):
#   sum=0
#   i=0
#   for number in numbers:
#    sum+= number
 
#    return (sum)
 
# number_list2=[5,66,4,75,86]
# print(sum_of_list_number (number_list2)) 


# def sum_of_number (numbers):   
#  total=0
#  for number in numbers:
#    total+=number
#    return total
 
 
#  numbers_list=[4,7,88,6]
#  result=sum_of_number(numbers_list)
#  print(f"Sum of numbers is:{result}")
 
 
#  Task10
# def get_unique_elements(elements):
#   return list(set(elements))

# list_of_elements=[2,4,7,9,6,6,7,4]
# result = get_unique_elements(list_of_elements)
# print(f"Unique elements are:{result}")

# def get_unique_list(elements):
#   unique_list=[]
#   for element in elements:
#     if element not in unique_list:
#       unique_list.append(element)
#   return unique_list
     
          
# my_list =[3,5,6,7,3,4,5,7,8] 
# unique_list=get_unique_list(my_list) 
# print(f"Unique elements are:{unique_list}")         

# Додаткові завдання по *args і **kwargs:
# Напишіть функцію, яка приймає через *args довільну кількість чисел і просто друкує їх.
# Напишіть функцію, яка приймає через *args довільну кількість слів і друкує тільки перше слово.
# Напишіть функцію, яка приймає через **kwargs довільну кількість параметрів і друкує їх у вигляді ключ: значення.

# def print_my_number(*args):
#  for number in args:
#    print(number)

  
# result=print_my_number(4,5,6,8,1)
# print(f"My_data is:{number}")



# def print_my_words(*args):
#   if len(args) != 0 :
#     print(args[0])
#   else:
#     print("It is empty.")
  
# print_my_words("cherry","banana","mango")


# def print_my_dict(**kwargs):
#   for key,value in kwargs.items():
#     print(f"{key}:{value}")
    
# print_my_dict(name='Iryna',city='Kharkiv',score=75,department='Python')    