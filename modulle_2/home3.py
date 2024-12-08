#Task1
# class Person:
#   def __init__(self, firstname, lastname,age):
#    self.firstname=firstname
#    self.lastname=lastname
#    self.age=age
#   def talk(self):
#    return f"Hello,my name is {self.firstname} {self.lastname} and I am {self.age} old."
# person1=Person("Petro","Kris","45")
# print(person1.talk())

#Task2
# class Dog:
#     age_factor = 7
    
#     def __init__(self, dog_age):
#         self.dog_age = dog_age
    
#     def human_age(self):
#         result = self.dog_age * self.age_factor
#         return result

# dog1 = Dog(3)
# print(dog1.human_age())


#Task3
  
class TVController:

    def __init__(self, channels):
        self.channels = channels
        self.current_index = 0
      
    
    def first_channel(self):
        self.current_index = 0
        return self.channels[self.current_index]
    
    def last_channel(self):
        self.current_index = len(self.channels) - 1
        return self.channels[self.current_index]
    
    def turn(self, N):
        if N > 0 & N < len(self.channels):
            self.current_index = N - 1
            return self.channels[self.current_index]
        # else:
        #     return "Choose correct channel"
    
    def current_channel(self):
        return self.channels[self.current_index]
    
    def next_channel(self):
      if self.current_index+1>len(self.channels):
        self.current_index = 0
      else:
        self.current_index += 1
        
      return self.channels[self.current_index]
    
    def previous_channel(self):
      if self.current_index-1<0:
        self.current_index = len(self.channels)-1
      else:
        self.current_index -= 1  
      
        
        return self.channels[self.current_index]
    
    def exist(self, channel_name):
        return "YES" if channel_name in self.channels else "NO"

# Test the controller
CHANNELS = ["BBC", "Discovery", "TV1000"]
controller = TVController(CHANNELS)

# Example Usage
print(controller.first_channel())      
print(controller.last_channel())       
print(controller.turn(1))              
print(controller.current_channel())    
print(controller.next_channel())       
print(controller.previous_channel())   
print(controller.exist("BBC"))        
print(controller.exist("CNN"))  