#Exercise_1

# class Pets():
#     def __init__(self, animals):
#         self.animals = animals

#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())

# class Cat():
#     is_lazy = True

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def walk(self):
#         return f'{self.name} is just walking around'

# class Bengal(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Chartreux(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
    
# class Siamese(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
    
# cat1 = Bengal("lulu", 2)
# cat2 = Chartreux("bubu", 3)
# cat3 = Siamese("zulu", 5)

# all_cats = [cat1, cat2, cat3]

# sarah_pets = Pets(all_cats)

# sarah_pets.walk()


#Exercise_2

class Dog:
    def __init__(self, name, age, weight):
     self.name = name
     self.age = age
     self.weight = weight
        
    def bark(self):
        print(f"{self.name} is barking WOOF")
    
    def run_speed(self):
        return self.weight / self.age * 5 
    
    def fight(self, other_dog):
       self_win = self.run_speed() * self.weight
       other_win = other_dog.run_speed() * other_dog.weight
        
       if other_win > self_win:
          return f"{other_dog.name} wins with score {other_win}!"
       else:
           return f"{self.name} wins with score {self_win}!"
           
dog1 = Dog("Zorro", 3, 41)
dog2 = Dog("Bat", 5, 43)
dog3 = Dog("Hummer", 2, 34)



dog1.bark()
dog2.bark()
dog3.bark()

dog1.run_speed()
dog2.run_speed()
dog3.run_speed()
print("Dogs fight!")

print(f"{dog1.name} runs at speed {dog1.run_speed()} km/h")
print(f"{dog2.name} runs at speed {dog2.run_speed()} km/h")
print(f"{dog3.name} runs at speed {dog3.run_speed()} km/h")


print(dog2.fight(dog3))
print(dog1.fight(dog3))
print(dog1.fight(dog2))


#Exercise_3
#see in XP1_imported.py




            
            
        
        
    
