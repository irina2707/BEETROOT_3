# Завдання 1. Напишіть програму, яка запитує ціле число у користувача. Якщо користувач вводить текст або інший некоректний формат, програма повинна вивести повідомлення про помилку.
# Завдання 2. Напишіть програму, яка має додавати два числа. Якщо ми пробуємо додати число і стрічку, програма повідомляє про це.
# Завдання 3. Напишіть програму, яка просить користувача ввести два числа, а потім ділить перше число на друге. Якщо користувач вводить нуль у якості другого числа, програма повинна вивести повідомлення про помилку.
#Task1
try:
  num=int(input("Write a number:")) 
  result="it is  number"
  print(result)
  
except ValueError:
  
  print("You didn't write  number!")

except Exception as e:
  print(f"It is unknown error{e}!") 
finally:  
 print("The program is finished!")


#Task2
# try:
  
#   number1=int(6)
#   number2=int('two')
#   result=number1+number2
#   print(result) 

# except ValueError: 
#   print("It is not number!")
# except Exception as e:
#   print(f"It is unknown error {e}!") 
# finally:
#   print("The program is finished!") 



#Task3

# num1=int(input("Write number:"))
# try: 
#   num2=int(input("Write number:"))
#   result=num1/num2
#   print(result)
# except  ZeroDivisionError:
#   print("Error:division on Zero")
# finally:
#   print("The program is finished!")