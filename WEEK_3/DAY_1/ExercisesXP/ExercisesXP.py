#Exercise_1 

# class Cat:
#     def __init__(self, cat_name, cat_age):
#         self.name = cat_name
#         self.age = cat_age
        
# cat1 = Cat("George", 13)
# cat2 = Cat("Milo", 9)
# cat3 = Cat("Honey", 5)


# def oldest_cat(cat_list : list[Cat]) ->Cat | None:
#     if len(cat_list) == 0:
#         return None
#     oldest_cat = cat_list[0]
    
#     for cat in cat_list:
#         if cat.age > oldest_cat.age:
#             oldest_cat = cat
    
#     return oldest_cat

# oldest = oldest_cat([cat1, cat2, cat3])
# print(f"{oldest.name}, {oldest.age}, is the oldest cat")
   
    
#Exercise_2

# class Dog:
#     def __init__(self, name, height):
#         self.name = name
#         self.height = height
        
#     def bark(self):
#         print(f"{self.name} goes Woof!")
        
#     def jump(self):
#         x = self.height*2
#         print(f"{self.name} jumps {x}cm high!")
        
# davids_dog = Dog("Rex", 50)
# print(f"David has a dog, whose name is {davids_dog.name}, and his height is {davids_dog.height} cm")
# davids_dog.bark()
# davids_dog.jump()

# sarahs_dog = Dog("Teacup", 20)
# print(f"Sarah has a dog, whose name is {sarahs_dog.name}, and his height is {sarahs_dog.height} cm")
# sarahs_dog.bark()
# sarahs_dog.jump() 

# if sarahs_dog.height > davids_dog.height:
#     print(f"{sarahs_dog.name} is bigger than {davids_dog.name}")
# else:
#     print(f"{davids_dog.name} is bigger than {sarahs_dog.name}")      


#Exercise_3

# class Song:
#     def __init__(self, lyrics):
#         self.lyrics = lyrics
    
#     def sing_me_song(self):
#         for line in self.lyrics:
#             print(line)
            
# stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])

# stairway.sing_me_song()


# Exercise_4
# 

class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
        
    def add_animal(self, new_animal):
        if new_animal not in self.animals:
           self.animals.append(new_animal)
           print(f"{new_animal} has been added to the Zoo")
           
    def get_animals(self):
        print("Animals in the Zoo: " )
        
        for animal in self.animals:
            print(animal)
            
    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print(f"{animal_sold} has been removed from the Zoo")
        else:
            print("there is no such animal")
    
    def sort_animals(self):
        sorted_animals = sorted(self.animals)
        grouped_animals = {}
    
        for animal in sorted_animals:
            first_letter = animal[0]
            if first_letter in grouped_animals:
               grouped_animals[first_letter].append(animal)
            else:
               grouped_animals[first_letter] = [animal]
  
        print(grouped_animals)
        
    def get_groups(self):
        grouped_animals = {}
        for animal in self.animals:
            first_letter = animal[0]
        if first_letter in grouped_animals:
            grouped_animals[first_letter].append(animal)
        else:
            grouped_animals[first_letter] = [animal]

        for group_i, animals_in_group in enumerate(grouped_animals.values(), start=1):
             if len(animals_in_group) == 1:
                print(f"{group_i}: {animals_in_group[0]}")
             else:
                print(f"{group_i}: {animals_in_group}")
            

ramat_gan_safari = Zoo("Ramat Gan Safari")

print("Which animal should we add to the zoo?")
new_animal = input()
ramat_gan_safari.add_animal(new_animal)

ramat_gan_safari.add_animal("Giraffe")
ramat_gan_safari.add_animal("Ape")
ramat_gan_safari.add_animal("Cat")
ramat_gan_safari.add_animal("Bear")
ramat_gan_safari.add_animal("Baboon")
ramat_gan_safari.add_animal("Emu")
ramat_gan_safari.add_animal("Cougar")
ramat_gan_safari.add_animal("Eel")

ramat_gan_safari.get_animals()

ramat_gan_safari.sell_animal("Giraffe")
ramat_gan_safari.sell_animal("Lion")  # Animal not present in the zoo

ramat_gan_safari.sort_animals()

ramat_gan_safari.get_groups()