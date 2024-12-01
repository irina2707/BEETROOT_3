# Завдання на цикли for для різних типів даних (strings (стрічки), lists (списки), tuples (кортежі), sets (множини), dicts(словники))
# Рядки (strings)
# Завдання 1: Напишіть цикл for, щоб вивести кожну букву у слові “Python”.
# Завдання 2: Порахуйте кількість голосних букв у рядку text = "Hello World".
# Завдання 3: Перетворіть всі малі літери на великі у рядку text = "good morning" за допомогою циклу for
# Списки (lists)
# Завдання 4: Створіть список чисел від 1 до 5 і виведіть кожен елемент на екран за допомогою for.
# Завдання 5: Виведіть тільки парні числа зі списку чисел [3, 7, 2, 8, 5, 10].
# Завдання 6: Знайдіть суму всіх чисел у списку [4, 5, 9, 2] за допомогою циклу.
# Кортежі (tuples)
# Завдання 7: Напишіть цикл for, щоб вивести всі елементи кортежу colors = ('red', 'blue', 'green').
# Завдання 8: Створіть кортеж з чисел (10, 20, 30, 40) і порахуйте їхній добуток (потрібно перемножити всі елементи).
# Завдання 9: Перевірте, чи містить кортеж names = ('Alice', 'Bob', 'Charlie') ім’я “Bob”, і виведіть результат.
# Множини (sets)
# Завдання 13: Створіть множину чисел {1, 3, 5, 7, 9} і виведіть кожен елемент за допомогою for.
# Завдання 14: Для двох множин A = {1, 2, 3, 4} та B = {3, 4, 5, 6}, виведіть їхнє перетин за допомогою циклу for.
# Завдання 15: Дано множину numbers = {5, 10, 15, 20}, використовуйте цикл for, щоб створити нову множину з чисел, поділених на 5.
# Словники (dicts)
# Завдання 10: Для словника scores = {'Alice': 90, 'Bob': 75, 'Charlie': 85}, виведіть ім’я та оцінку кожного студента.
# Завдання 11: Знайдіть середню оцінку студентів у словнику grades = {'John': 88, 'Emily': 92, 'Sam': 79, 'Lily': 85}.
# Завдання 12: Створіть словник із предметів та їхніх цін { 'apple': 1, 'banana': 2, 'orange': 1.5 }, і виведіть загальну вартість всіх предметів.


#Task1
# Task3
# text = "good morning"
# text1=""
# for i in text :
#   i.upper()
#   text1+=i.upper()
# print(text1)


#Task4
# number_list= [1,2,3,4,5]
# for i in number_list:
#   print(i)

#Task6
# number_list1=[4, 5, 9, 2]
# sum =0
# for i in number_list1:
#   sum+=i
# print(sum)


#Task7
# colors = ('red', 'blue', 'green')
# for  color in colors:
#   print(color ) 
    
#  Task8 
# my_tuples=(10, 20, 30, 40)
# multipl =()
# for i in range(len(my_tuples)):
#   multipl*=i
#   print(multipl)
  

#Task9
# names = ('Alice', 'Bob', 'Charlie')
# for i  in names:
#   if i == 'Bob':
#     print(True)
#   else:
#     print(False) 
    
    
     
 #Task13
# my_set= {1, 3, 5, 7, 9} 
# for i in my_set:
#   print(i)
  
  #Task15
# numbers_1 = {5, 10, 15, 20}
# numbers_2=set()

# for i in numbers_1:
#    numbers_2.add(i/5)
#    print(numbers_2)
   
   
#Task10
# scores = {'Alice': 90, 'Bob': 75, 'Charlie': 85}  
# for x,y in scores.items():
#   print(x,y) 
  
  #Task11
# grades = {'John': 88, 'Emily': 92, 'Sam': 79, 'Lily': 85}
# count=0
# sum = 0
#   #res = sum/count
# for value in grades.values():
#     sum+=value
#     count+=1
# print(sum/count)  


#Task12
fruts ={ 'apple': 1, 'banana': 2, 'orange': 1.5 }
sum=0
for x in fruts.values():
  sum+=x
  print (sum)
  