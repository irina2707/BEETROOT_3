# Завдання 1: Клас “Student”
# Умова:
# Створити клас Student, який має атрибути:
# name – публічний атрибут.
# _group – захищений атрибут.
# __average_score – приватний атрибут.
# Створити об’єкт Student, додай будь-які значення для атрибутів.
# Завдання:
# Перевірити доступ до атрибутів: публічного, захищеного і приватного.
# Пояснити різницю між доступом до атрибутів через код:
# student.name
# student._group
# student.__average_score
# class Student:
#   def __init__(self,name,group,average_score):
#     self.public_atr=name 
#     self._protected_atr= group
#     self.__private_atr= average_score
  # def display_info(self):
  #       print(f"Name: {self.public_atr}")
  #       print(f"Group: {self._protected_atr}")
  #       print(f"Average Score: {self.__private_atr}")
#   def show_public(self): 
#      print(f"Public attribute: {self.public_atr}")
     
#   def show_protected (self): 
#      print(f"Protected attribute: {self._protected_atr}")  
#   def __show_private_atr(self): 
#      print(f"Private attribute: {self.__private_atr}")  
     
# student1=Student("Ala","Beetroot3",85)
# # student1.display_info()
# student1.show_public()
# student1.show_protected()
# student1._Student__show_private_atr()


# Завдання 2: Клас “Car”
# Умова:
# Створити клас Car, який містить:
# Публічний атрибут brand.
# Захищений атрибут _engine_type.
# Приватний атрибут __mileage.
# Створити екземпляр класу Car і задати йому значення атрибутів.
# Завдання:
# Вивести значення атрибутів прямо з об’єкта:
# car.brand
# car._engine_type
# Спробувати звернутися до приватного атрибута car.__mileage – що відбудеться?
# Спробувати дістатися до значення __mileage через name mangling (car._Car__mileage).
class Car:
  def __init__(self,brand,engine_type,mileage):
   self.public_atr=brand
   self.protected_atr=engine_type
   self.__private_atr=mileage
  # def show_public(self): 
  #    print(f"Public attribute: {self.public_atr}")
     
  # def show_protected (self): 
  #    print(f"Protected attribute: {self.protected_atr}")  
  # def __show_private_atr(self): 
  #    print(f"Private attribute: {self.__private_atr}") 
     
car1=Car("Volvo","Petrol",35000)
print(car1.public_atr)
print(car1.protected_atr)
print(car1._Car__private_atr)