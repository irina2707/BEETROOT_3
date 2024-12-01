# Завдання до теми роботи з текстовими файлами
# 1. Створення та запис у файл
# Створіть текстовий файл my_file.txt і запишіть у нього кілька рядків тексту.
# Використайте методи write() або writelines().
# 2. Читання з файлу
# Прочитайте вміст файлу my_file.txt і виведіть його у термінал.
# Спробуйте використати методи read(), readline(), readlines().
# 3. Додавання тексту у файл
# Відкрийте файл my_file.txt у режимі додавання ('a') і запишіть новий рядок
#Task1
# with open('my_file.txt','w') as file:
#   file.write('Hello,everybody!\n')
#   file.write('It is nice day!')
# with open('my_file.txt','r') as file:
  # content=file.read()
  # print(content)
  # line=file.readline()
  # print(line)
  # lines=file.readlines()
  # print(lines)
# with open('my_file.txt','a') as file:
#   file.writelines('Good luck!/n')
# with open('my_file.txt','r') as file:
#   content=file.read()
#   print(content) 
#   1. Напишіть програму, яка читає текстовий файл words.txt, рахує, скільки разів кожне слово зустрічається у файлі, і виводить результати у новий файл word_counts.txt.
# 2. Напишіть програму, яка підраховує, скільки рядків у файлі example.txt, і виводить цей результат у термінал.
# 3. Створіть список студентів, де кожен студент представлений як словник із такими полями: ім'я, вік, середній бал. Збережіть цей список у JSON-файлі students.json.
# 4. Напишіть програми, яка виведе у термінал дані з файлу з завдання 3
#Task3
# import json
# list_students=[{'name':'Anna',
# 'age':28,
# 'aver_score':95},{'name':'Bogdan',
# 'age':24,
# 'aver_score':85},{'name':'Lily',
# 'age' : 34,
# 'aver_score':75}]
# with  open ("output.json","w") as file:
#   json.dump(list_students,file,indent=4)
  #Task4 
# import json   
# with open ("output.json","r") as file:
#   data=json.load(file)
# print(data) 



#Task1
# try:
#   with open ('my_file.txt','r',encoding='utf-8')as file:
#    text=file.read()
# except FileNotFoundError:
#     print("Файл 'my_file.txt' не знайдено. Переконайтесь, що файл існує.")
#     exit()  
# words=text.split()
# word_counts=0
# for word in words:
#   word_counts+=1
# print(word_counts)
# with open ('word_counts.txt','w',encoding='utf-8')as file:
#   file.write('word_counts')
# print("Підрахунок слів завершено. Результати збережено у файлі 'word_counts.txt'.")


# Завдання 1. Відкрити та прочитати CSV-файл
# Мета: Відкрити файл і вивести всі його рядки на екран. (перед цим вам потрібно створити власний CSV-файл, додати хедери (заголовки) і додати якусь інформацію)
# Завдання 2. Порахувати кількість рядків у файлі
# Мета: Знайти кількість рядків у файлі (включно із заголовком).
# Завдання 3. Порахувати кількість рядків (без заголовка)
# Мета: Порахувати кількість даних (тільки рядків із записами, без заголовка).
# Завдання 4. Записати дані у CSV-файл.
# Мета: Створіть список або словник з даними і запишіть їх у CSV-файл
#Task1
import csv
data = [
    ["Name", "Age", "City","Country"],
    ["Anna", 25, "Kyiv","Ukraine"],
    ["Ivan", 30, "Lviv","Ukraine"],
    ["Olga", 22, "Odesa","Ukraine"]
]
with open("example.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("CSV-файл 'example.csv' створено.")
with open("example.csv", mode="r", encoding="utf-8") as file:
    reader = csv.reader(file)
    print("\nВміст файлу 'example.csv':")
    for row in reader:
        print(row)
#Task2
# with open("example.csv", mode="r", encoding="utf-8") as file:
#     reader = csv.reader(file)
#     print("\nВміст файлу 'example.csv':")
#     count=0
#     for row in reader:
#       count+=1
#       print(count)
    
#Task3
with open("example.csv", mode="r", encoding="utf-8") as file:
    reader = csv.reader(file)
    print("\nВміст файлу 'example.csv':")
    count=0
    for row in reader:
      
     count+=1
    print(count-1)