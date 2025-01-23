#Task1
# class Animal:
#   def talk(self):
#     print("Some sound")
    
    
# class Dog(Animal):
#   def talk(self):
#     super().talk()
#     print("Woof")    
    
# class Cat(Animal):
#   def talk(self):
#     super().talk()
#     print("Meow")  
    
    
# cat1=Cat()
# dog1=Dog()


# cat1.talk()
# dog1.talk

# Завдання 1: “Транспорт” (поліморфізм)
# Мета:
# Навчитися використовувати поліморфізм для різних типів транспорту.
# Вимоги:
# Створіть базовий клас Transport з методом move(), який поки що нічого не робить (заглушка, можна просто написати pass).
# Створіть два класи-нащадки:
# Car (метод move() виводить “Машина їде по дорозі“),
# Boat (метод move() виводить “Човен пливе по воді“).
# Напишіть функцію start_transport(transport), яка приймає об‘єкт типу Transport і викликає його метод move().
# Очікуваний результат:
# Створіть по одному об‘єкту кожного типу транспорту.
# Викличте start_transport() для кожного з них, щоб показати, як метод move() поводиться по-різному.
# Завдання 2: “Користувачі та зміна пароля” (інкапсуляція, магічні методи)
# Мета:
# Продемонструвати використання інкапсуляції через роботу з приватними атрибутами та доступом до них через методи.
# Вимоги:
# Створити клас User з атрибутами:
# __username (приватний, ім‘я користувача),
# __password (приватний, пароль).
# Додати методи:
# change_password(new_password) для зміни пароля,
# check_password(input_password) для перевірки, чи правильний пароль введено.
# Додати магічний метод __str__, щоб об‘єкт користувача виводив лише ім‘я користувача, але не пароль.
# Очікуваний результат:
# Створити об‘єкт User.
# Спробувати перевірити та змінити пароль через методи.
# Надрукувати об‘єкт користувача (має показати тільки ім’я).


# Task1


# def  start_transport(transport):
#   print(transport.move())


# class  Transport:
#   def move():
#     pass 
  
  
# class Car(Transport):
#    def move(self):
#     return "Машина їде по дорозі"

# class Boat(Transport):
#   def move(self):
#    return "Човен пливе по воді" 
 
  
# car1=Car()
# boat1=Boat()
# start_transport(car1) 
# start_transport(boat1)

# Task2
class User:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password

    def change_password(self):
        new_password = input("Введіть новий пароль: ")
        if len(new_password) == 0:
            raise ValueError("Пароль не може бути пустим")
        self.__password = new_password  
        print("Password is changed")

    def check_password(self):
        input_password = input("Введіть пароль: ")

        if len(input_password) == 0:
            raise ValueError("Пароль не може бути пустим")

        if input_password != self.__password:
            raise ValueError("Пароль не вірний")
        else:
            return True

    def __str__(self):
       return self._User__username    




obj = User("Polina", "Dnipru#1")



print(str(obj))

# Changing password
obj.change_password()

# Checking password
try:
    if obj.check_password():
        print("Пароль правильний")
except ValueError :
    print("Error")



