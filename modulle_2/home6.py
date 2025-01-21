# Завдання: Тестування функції перевірки пароля
# Мета:
# Попрактикувати написання тестів з різними вхідними даними.
# Вимоги:
# Напишіть функцію is_valid_password(password), яка перевіряє, чи задовольняє пароль наступні вимоги:
# Має бути не менше 8 символів.
# Має містити хоча б одну велику літеру.
# Має містити хоча б одну цифру.
# Має містити хоча б один розділовий знак або специфічний символ (& , . ^ # @ * ( ! \ / |)
# Створіть тестовий клас для перевірки цієї функції з використанням бібліотеки unittest.
# Напишіть тести для різних випадків:
# Пароль відповідає всім вимогам.
# Пароль коротший за 8 символів.
# Пароль не містить цифр.
# Пароль не містить великих літер.
# Пароль не містить розділового знаку/специфічного символу
# Порожній рядок або None як пароль.
# Запустіть тести та впевніться в правильності їх виконання.




# Task1 

def is_valid_password(password):

    if len(password) < 8 :
        raise ValueError(" Пароль має бути не менше 8 символів.")

    special_characters="& , . % ^ # @ * ( ! \ / |)"
    if not any(char in special_characters for char in password):
   
      raise ValueError(" Пароль має містити хоча б один розділовий знак або специфічний символ")             
                
    if not any(char.isdigit() for char in password):
   
     raise ValueError("Пароль має містити хоча б одну цифру.") 
                  
    if not any(char.isupper() for char in password):
        raise ValueError("Пароль має містити хоча б одну велику літер.") 
      
      
    # print("Password is valid")  
    return True       
    
try:
    password = input("Write password: ")
    print(is_valid_password(password))
except ValueError as e:
    print(e)
    
    

# import unittest



# class TestFunction(unittest.TestCase):
#     def test_valid_password(self):
#         self.assertTrue(is_valid_password("Secure@123"))

#     def test_short_password(self):
#         with self.assertRaises(ValueError, msg="Пароль має бути не менше 8 символів."):
#             is_valid_password("Se@123")
    
#     def test_is_digital_password(self): 
#       with self.assertRaises(ValueError, msg="Пароль має містити хоча б одну цифру."):
#             is_valid_password("SecureId#")
    
    
    
#     def test_is_special_char_password(self):
#       with self.assertRaises(ValueError, msg=" Пароль має містити хоча б один розділовий знак або специфічний символ"):
           
#         is_valid_password("Secure123")
    
#     def test_isupper_char_password(self):
#        with self.assertRaises(ValueError, msg="Пароль має містити хоча б одну велику літеру."):
#             is_valid_password("secure#123")
            
            
#     def test_empty_password(self):
#        with self.assertRaises(ValueError, msg="Порожній рядок або None як пароль"):
#             is_valid_password(" ")
  
 
    
    
    









