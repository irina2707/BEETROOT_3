# Завдання по темі функцій:
# Завдання 1: Фільтрування за типом
# Напишіть функцію, яка приймає довільну кількість значень через *args і повертає список лише тих елементів, які є рядками.
# Завдання 2: Пошук найдовшого слова
# Напишіть функцію, яка приймає список слів і повертає найдовше слово. Якщо таких слів кілька, поверніть перше з них.
# Завдання 3: Фільтрування за значенням
# Напишіть функцію, яка приймає список чисел і значення x. Поверніть список, що містить лише ті числа, які більше за x.
# Завдання 4: Об‘єднання кількох списків
# Напишіть функцію, яка приймає кілька списків через *args і повертає новий список, який є об’єднанням усіх елементів без повторів.
# Завдання 5: Середнє арифметичне
# Напишіть функцію, яка приймає список чисел і повертає їхнє середнє значення.
# Завдання 6: Фільтр за довжиною слів
# Напишіть функцію, яка приймає список слів і повертає новий список, що містить лише ті слова, які починаються на певну літеру (зазначену як аргумент).

#Task1
# def filter_strings(*args):
#     result =[]
#     for arg in args:
#         if isinstance(arg, str):
#             result.append(arg)
#     return result

# # Приклад використання:
# result = filter_strings(1, "hello", 3.14, "world","rat","Python")
# print(result) 
#Task2
# def longest_word (words):
#       max_len_word=words[0]
#       for word in words:
       
#        if len(word)>len(max_len_word):
#         max_len_word=word
#        print("The longest word is:word")
#       return max_len_word
     
# thisword=['cat','banana','cucumber'] 
# print(longest_word(thisword))   

#Task3
# def compare_number(numbers,x):
#   result=[]
#   for number in numbers:
#     if number> x:
#       result.append(number)
#   return(result)
# list_of_numbers=[5,7,9,15,11] 
# print(compare_number(list_of_numbers,8) )  
#Task4
# def unique_list(*args):
#   result=set()
#   for lst in args:
#     result.update(lst)
  
#   return list(result)

# number_list=[3,5,6,7,5]
# number_list1=[4,5,6,8,9]
# print(unique_list(number_list,number_list1))

#Task5
# def aver_number(numbers):
#   sum=0
#   for number in numbers:
#     sum+=number
#   result=sum/len(numbers)
#   return(result) 
# number_list1=[4,5,6,8,9]
# print(aver_number(number_list1))


#Task6
def like_letter(words,letter):
  result=[]
 
  for word in words:
    if word.startswith(letter):
      result.append(word)
    else:
      print("There are not words starting whith:{letter}")   
      return None
  return result
    
    
list_words=["bambuc","cat","rat"] 
letter="a"
print(like_letter(list_words,"a"))   