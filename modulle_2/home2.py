# Завдання 1: Декоратор для вимірювання часу виконання функції
# Напишіть декоратор, який вимірюватиме час виконання будь-якої функції, до якої він застосовується, і виводитиме цей час на екран.
# (тут можна використати таку штуку, як time.sleep(кількість секунд) щоб сповільнити виконання функції, бібліотеку time треба буде імпортувати додатково)
# Завдання 2: Декоратор для перевірки вхідних параметрів
# Напишіть декоратор, який перевірятиме, чи всі аргументи функції є цілими числами. Якщо хоча б один з аргументів не ціле число, функція повинна вивести повідомлення про помилку.


# Task1
# import time

# def time_function(f):
#   def wrapper(*args,**kwargs):
#     start=time.time()
#     result=f(*args,**kwargs)
#     end=time.time()
#     print(f.__name__ +" "+ "took"+" " +str((end-start)*1000) +"ms")
#     return result
#   return wrapper

# @time_function
# def multiplication(a,b):
#   return  a*b


# print(multiplication(7,9))


# Task2
def integer_(f):
    def wrapper(*args):
        for arg in args:
            if not isinstance(arg,int):
             raise ValueError("Аргумент функції не  є цілим числом")
            
        result = f(*args)  
        return result
    
    return wrapper

@integer_
def multiplication(a, b, c):
    return a * b * c

try:
 print(multiplication(7, 0.6, 10)) 
except :
  print("Аргумент функції не  є цілим числом")
  
try:
 print(multiplication(7,- 7, -10))
except :
  print("Аргумент функції не  є цілим числом")