# Task 4

# Створити лист із днями тижня.
# В один рядок (ну або як завжди) створити словник виду: {1: "Monday", 2:...
# Також в один рядок або як вдасться створити зворотний словник {"Monday": 1,


# weekdays_list=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

# days_dict = {i + 1: day for i, day in enumerate(weekdays_list)}

# Зворотний словник {"Monday": 1, "Tuesday": 2, ...}
# reverse_days_dict = {day: i + 1 for i, day in enumerate(weekdays_list)}

# Вивід результатів
# print(days_dict)
# print(reverse_days_dict)


#Task1
# Make a program that has some sentence (a string) on input and returns a dict containing all unique words as keys and the number of occurrences as values. 
# input_sentence="It is hot day. It is too hot."
# words=input_sentence.lower().split()
# word_dict={}
# for word in words:
#   word = ''.join(char for char in word if char .isalnum())
#   word_dict[word] = word_dict.get(word,0)+1
#   print(word_dict)
  
#Task2 
  # Input data
# stock = {
#     "banana": 6,
#     "apple": 0,
#     "orange": 32,
#     "pear": 15
# }
# prices = {
#     "banana": 4,
#     "apple": 2,
#     "orange": 1.5,
#     "pear": 3
# }


# total_prices = {item: stock[item] * prices[item] for item in stock}

# print(total_prices)
#Task3 List comprehension exercise

# Use a list comprehension to make a list containing tuples (i, j) where 'i' goes from 1 to 10 and 'j' is corresponding to 'i' squared.
# my_list=[( i ,i**2) for i in range(1,10)]
# print(my_list)
#Task4
weekdays_list=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

days_dict = {i + 1: day for i, day in enumerate(weekdays_list)}
reverse_days_dict = {day: i + 1 for i, day in enumerate(weekdays_list)}
print(days_dict)
print(reverse_days_dict)