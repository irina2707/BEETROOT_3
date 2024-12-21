# Task 1

# Write a Python program to detect the number of local variables declared in a function.

 

# Task 2

# Write a Python program to access a function inside a function (Tips: use function, which returns another function)


# Task 3

# Write a function called "choose_func" which takes a list of nums and 2 callback functions. If all nums inside the list are positive, execute the first function on that list and return the result of it. Otherwise, return the result of the second one

 

# def choose_func(nums: list, func1, func2):

#     pass

 

# # Assertions

# nums1 = [1, 2, 3, 4, 5]

# nums2 = [1, -2, 3, -4, 5]

 

# def square_nums(nums):

#     return [num ** 2 for num in nums]

 

# def remove_negatives(nums):

#     return [num for num in nums if num > 0]

 

# assert choose_func(nums1, square_nums, remove_negatives) == [1, 4, 9, 16, 25]

# assert choose_func(nums2, square_nums, remove_negatives) == [1, 3, 5]
#Task 2

# def double(n):
#   return 2*n
#   print (2*n)
  
# def sq(n):
#   return n*n
#   print(n*n)
  
# def call_func(n,func):
#     print(func(n))
    
# call_func(5,sq) 
# call_func(7,double)  
#Task3
# def choose_func(nums: list, func1, func2):
  
#     if all(num > 0 for num in nums):
#         return [func1(num) for num in nums]
#     else:
#         return [func2(num) for num in nums]

# def double(num):
#     return 2 * num

# def sq(num):
#     return num * num

# numbers = [1, 2, 3, 4, 5]
# result = choose_func(numbers, double, sq)
# print(result)

# numbers = [-1, 2, -3, 4]
# result = choose_func(numbers, double, sq)
# print(result)

# def sample_function():
#     x = 10
#     y = 20
#     z = x + y
#     message = " "
#     return message

# def count_local_variables(func):
#     return func.__code__.co_nlocals


# num_locals = count_local_variables(sample_function)
# print(f"Кількість локальних змінних: {num_locals}")
# Завдання 1: Знижки у магазині
# Уявіть, що ви програмуєте систему для обчислення знижок у магазині. У цій системі функції використовуються як аргументи інших функцій. Напишіть програму, яка:
# Містить дві функції знижок:
# discount_10: повертає нову ціну з 10% знижкою.
# : повертає нову ціну з 20% знижкою.
# Головна функція apply_discount(price, discount_func) приймає ціну та функцію знижки і повертає ціну зі знижкою.
# Вхідні дані: Ціна товару: 100.
# Використайте дві функції знижок (discount_10 і discount_20) як аргументи.
# Очікуваний результат:
# Ціна зі знижкою 10%: 90.0
# Ціна зі знижкою 20%: 80.0


# def discount_10(price):
#    return price*0.9
 
# def discount_20(price):
#      return price*0.8
   
# def apply_discount(price, discount_func):
#         return discount_func(price)
    
# price=100

# price_10_discount=apply_discount(price,discount_10)
# price_20_discount= apply_discount(price,discount_20)
  
    
# print(f"Ціна зі знижкою 10%:{price_10_discount}") 
# print(f"Ціна зі знижкою 20%:{price_20_discount}")


# Завдання 2: Перевірка даних для виставлення рахунку
# Уявіть, що ви програмуєте систему для обчислення рахунку в магазині. Перед створенням рахунку потрібно перевірити правильність даних замовлення. Напишіть програму, яка:
# Використовує дві перевірки:
# Ціна товару повинна бути більшою за 0.
# Кількість одиниць товару повинна бути цілим числом і більшою за 0.
# Функція calculate_invoice(price_per_item, quantity) перевіряє умови за допомогою assert і обчислює загальну суму замовлення.
# Реалізація програми: Програма містить функцію calculate_invoice, яка:
# Отримує два параметри: price_per_item (ціна за одиницю товару) і quantity (кількість одиниць товару).
# Використовує твердження assert для перевірки відповідності вищезазначених умов.
# Якщо всі перевірки проходять успішно, обчислюється і повертається загальна сума замовлення як добуток ціни та кількості.

def calculate_invoice(price_per_item, quantity):
  assert quantity>0 
  assert quantity %1==0
  assert price_per_item>0
  return  price_per_item*quantity

print(calculate_invoice(0.1,5))