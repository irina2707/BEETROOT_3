
# Завдання 2. Ознайомлення із модулем math.
# Створіть простий калькулятор, який:
# 1. Запитує у користувача число.
# 2. Дозволяє вибрати одну з функцій: квадратний корінь, синус, косинус, піднесення до степеня.
# 3. Використовує відповідні функції з модуля math для виконання обчислень.

# Завдання 3. Ознайомлення з модулями calendar та datetime.
# Напишіть програму, яка:
# 1. Виводить дні тижня для поточного місяця у зручному форматі.
# 2. Показує користувачеві, який сьогодні день тижня.

# * Модулі calendar, datetime і math є частиною стандартної бібліотеки Python і йдуть разом із самим інтерпретатором. Тобто їх не потрібно встановлювати окремо — вони готові до використання одразу після встановлення Python, проте вам треба буде їх додатково імпортувати у власних скриптах.

#Task2
# import math

# def my_calculation():
#     try:
#         number = float(input("Write number: ")) 
#     except ValueError:
#         print("Please enter a valid number.")
#         return

#     print("If you want to calculate square root enter '1'")
#     print("If you want to calculate cos enter '2'")
#     print("If you want to calculate sin enter '3'")
#     print("If you want to calculate pow enter '4'")

#     try:
#         math_method = int(input("Choose method: ")) 
#     except ValueError:
#         print("Please enter a valid choice.")
#         return

#     if math_method == 1:
#         if number < 0:
#             print("It is impossible to calculate the square root of a negative number.")
#         else:
#             result = math.sqrt(number)
#             print(result)
#     elif math_method == 2:
#         result = math.cos(math.radians(number))
#         print(result)
#     elif math_method == 3:
#         result = math.sin(math.radians(number))
#         print(result)
#     elif math_method == 4:
        
#             power = float(input("Write number to raise to the power of: "))
#             result = math.pow(number, power)
#             print(result)
    
#     else:
#         print("Choose the right method!")


# my_calculation()
#Task3 
import datetime
import calendar


x=datetime.datetime.now()
print(x)
print(x.strftime("%A"))
t=calendar.TextCalendar()
t.prmonth(x.year,x.month) 


