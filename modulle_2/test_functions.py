import unittest
from home6  import is_valid_password


class TestFunction(unittest.TestCase):
    def test_valid_password(self):
        self.assertTrue(is_valid_password("Secure@123"))

    def test_short_password(self):
        with self.assertRaises(ValueError, msg="Пароль має бути не менше 8 символів."):
            is_valid_password("Se@123")
    
    def test_is_digital_password(self): 
      with self.assertRaises(ValueError, msg="Пароль має містити хоча б одну цифру."):
            is_valid_password("SecureId#")
    
    
    
    def test_is_special_char_password(self):
      with self.assertRaises(ValueError, msg=" Пароль має містити хоча б один розділовий знак або специфічний символ"):
           
        is_valid_password("Secure123")
    
    def test_isupper_char_password(self):
       with self.assertRaises(ValueError, msg="Пароль має містити хоча б одну велику літеру."):
            is_valid_password("secure#123")
            
            
    def test_empty_password(self):
       with self.assertRaises(ValueError, msg="Порожній рядок або None як пароль"):
            is_valid_password(" ")