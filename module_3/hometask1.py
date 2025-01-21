# Task3
# Завдання 3. Жарти про Чака Норріса
# Створіть консольну програму, яка:
# Отримує та виводить на екран 5 випадкових жартів з API (https://api.chucknorris.io/jokes/random)
# Зберігає отримані жарти у текстовий файл

# import requests

# url = 'https://api.chucknorris.io/jokes/random'
# file_name= 'chuck_norris_jokes.txt'

# with open ('chuck_norris_jokes.txt','w',encoding='utf-8') as file:
#  for _ in range(5):  
#     response = requests.get(url)  # Make a request to the API
#     if response.status_code == 200:
#         joke = response.json().get('value')  # Extract the joke text
#         print(joke)
#         file.write(joke+'\n')
#     else:
#         print("Error fetching joke")
#         file.write("Error fetching joke")
# print(f"Joke is saved in txt file:chuck_norris_jokes.txt")


# Task3
# Завдання 2 Інформація про країни
# Створіть консольну програму, яка:
# Приймає назву країни англійською мовою
# Використовуючи API (https://restcountries.com/v3.1/name/{country}) отримує та виводить:
# Столицю
# Населення
# Площу
# Основні мови
# Валюту
# Зберігає результати пошуку у JSON файл
 
 
# import requests
# import json

# def country_info():
#     # Get user input for country name
#   name = input("Write country name: ").strip()
    
#   country_url = f'https://restcountries.com/v3.1/name/{name}?fields=name,capital,currencies,languages,area,population'
#   file_name= 'country_info.json'

#     # Make the GET request
#   response = requests.get(country_url)
    
#     # Check if the request was successful
#   if response.status_code == 200:
#         # Parse JSON response and return it
#     country_data = response.json()
#     print(country_data)
#     with open (file_name,'w',encoding='utf-8') as file:  
#       json.dump(country_data, file, indent=4)    
#       print(f"Country_data is saved in json file:country_info.json")
#   else:
#     with open (file_name,'w',encoding='utf-8') as file:    
#      file.write('Error')
#      print("Error")  
#      return None

# result = country_info()

# Task1
# Завдання 1
# Завантажте та збережіть у файл robots.txt дані з веб-сайтів wikipedia.org та twitter.com (виберіть якусь одну сторінку). Порівняйте їх вміст.

import requests

def data_info():
  url='https://ru.wikipedia.org/wiki/%D0%A0%D0%BE%D0%B1%D0%BE%D1%82_(%D0%B7%D0%BD%D0%B0%D1%87%D0%B5%D0%BD%D0%B8%D1%8F)'
  file_name='robots.txt'
  response = requests.get(url)
    
    # Check if the request was successful
  if response.status_code == 200:
       
     data = response.text
     print("Success")
     with open (file_name,'w',encoding='utf-8') as file:  
       
        file.write(data +'\n')   
        print(f"Data is saved in file:{file_name }")
        return data
  else:
    with open (file_name,'w',encoding='utf-8') as file:    
        file.write('Error')
        print("Error")  
        return None

result = data_info()
  
  