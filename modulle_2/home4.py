# Завдання 1: “Співробітники компанії” (наслідування)
# Мета: Розробити ієрархію класів для управління інформацією про співробітників.
# Вимоги:
# Базовий клас Employee:
# Атрибути: name (ім‘я), position (посада), salary (зарплата).
# Метод: get_info(), який повертає інформацію про співробітника.
# Клас FullTimeEmployee (успадковує Employee):
# Додаткові атрибути: annual_bonus (річний бонус).
# Метод get_info() доповнюється інформацією про бонус.
# Клас PartTimeEmployee (успадковує Employee):
# Додаткові атрибути: hours_worked (кількість відпрацьованих годин), hourly_rate (ставка за годину).
# Метод calculate_pay() обчислює оплату на основі годин та ставки.
# Завдання:
# Створіть об‘єкт класу FullTimeEmployee (ім‘я: “Ольга“, посада: “Менеджер“, зарплата: 20000, бонус: 3000).
# Створіть об‘єкт класу PartTimeEmployee (ім‘я: “Петро“, посада: “Кур’єр“, ставка: 200 грн/год, відпрацьовано 120 годин).
# Викличте метод get_info() для обох співробітників та розрахуйте оплату для працівника з погодинною ставкою.
# Завдання 2: “Склад та продукти” (агрегація)
# Мета: Створити систему класів для управління продуктами на складі.
# Вимоги:
# Клас Product:
# Атрибути:
# name (назва продукту),
# price (ціна за одиницю),
# quantity (кількість у наявності).
# Клас Warehouse:
# Атрибути:
# location (розташування складу),
# products (список продуктів на складі).
# Методи:
# add_product(product) — додає продукт до складу.
# get_total_value() — повертає загальну вартість усіх продуктів на складі.
# Очікуваний результат:
# Створити кілька продуктів.
# Додати їх до складу за допомогою методу add_product.
# Обчислити загальну вартість продуктів за допомогою методу get_total_value.


# Task1
# class Employee:
#   def __init__(self,name,position,salary):
#    self.name=name
#    self.position=position
#    self.salary=salary

#   def get_info(self):
#     return f"Employeee:{self.name},Position: {self.position},Salary:{self.salary}"
  
# class FullTimeEmployee(Employee):
#   def __init__(self,name,position,salary,annual_bonus ):
#     super().__init__(name,position,salary)
#     self.annual_bonus=annual_bonus
    
#   def get_info(self):
#     return f"Employeee:{self.name},Position: {self.position},Salary:{self.salary},Bonus: {self.annual_bonus}"  
   
# class PartTimeEmployee(Employee):
 
#   def __init__(self,name,position,hourly_rate,hours_worked):
#     self.hourly_rate=float(hourly_rate)
#     self.hours_worked=int(hours_worked)

#     salary=self.hours_worked*self.hourly_rate
#     super().__init__(name,position,salary) 
    
    
#   def calculate_pay(self):

#     return self.hours_worked*self.hourly_rate
  
#   def get_info(self):
#     payment= self.calculate_pay()
#     return f"Employeee:{self.name},Position: {self.position},Rate: {self.hourly_rate}grn/hour,Hours: {self.hours_worked},Total Pay:{payment} grn" 
   
   
   
# # Створіть об‘єкт класу FullTimeEmployee (ім‘я: “Ольга“, посада: “Менеджер“, зарплата: 20000, бонус: 3000)   
# FullTimeEmployee1=FullTimeEmployee("Ольга","Менеджер","20000",3000)
# # Створіть об‘єкт класу PartTimeEmployee (ім‘я: “Петро“, посада: “Кур’єр“, ставка: 200 грн/год, відпрацьовано 120 годин)  
# PartTimeEmployee1=PartTimeEmployee("Петро","Кур’єр","200","120")
# print(FullTimeEmployee1.get_info())
# print(PartTimeEmployee1.get_info())


# Task2

class Product:
  def __init__(self,name,price,quantity):
    self.name=name
    self.price=price
    self.quantity=quantity
class Warehouse: 
  def __init__(self,location,products):
    self.location=location
    self.products=[]
    
  def add_product(self,product):
     return self.products.append(product)
   
  def get_total_value(self):
    total_value=0
    for product in self.products:
       product_value= product.price*product.quantity
       total_value+= product_value
    return total_value
  
product1 = Product(name="Orange", price=50, quantity=50)
product2 = Product(name="Apple", price=30, quantity=30)

warehouse=Warehouse(location="Kharkiv",products=[ ])
warehouse.products.append(product1)
warehouse.products.append(product2)

total_value=warehouse.get_total_value()
print (f"Total value of products in warehouse is:{total_value}")