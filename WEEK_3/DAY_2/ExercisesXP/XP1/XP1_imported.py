from XP1 import Dog 
from random import choice
class PetDog(Dog): 
    def __init__(self, name, age, weight, trained = False):
        super().__init__(name, age, weight)
        self.trained = trained
        
    def train(self):
        self.bark()
        self.trained = True
        
    def play(self, *args):
        dog_names = ", ".join([dog.name for dog in args])
        print(f"{dog_names} all play together")
        
    def do_trick (self):
        if self.trained:
            trick = choice([f'{self.name} does a barrel roll',
                           f"{self.name} stands on his back legs",
                           f"{self.name} shakes your hand",
                           f"{self.name} plays dead"])
            print(trick)
        else:
            print(f"{self.name} runs away")
        


pet_dog1 = PetDog("Buddy", 4, 35)
pet_dog2 = PetDog("Max", 3, 40)


pet_dog1.train()
pet_dog1.play(pet_dog2, pet_dog1)
pet_dog1.do_trick()
pet_dog2.do_trick()
