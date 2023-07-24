class Dog :
    def __init__(self, name, age):
        self.dog_name = name
        self.dog_age = age 
        
    def barks(self):
        print(f"{Dog} says WOOF")

my_dog = Dog()

print(my_dog)

# INHERITANCE

class GermanShepard (Dog):
#no init - uses attributes from the parent class, but for new attributes:
# def __init__(self): #overwrites the init of parent class, so no previous attributes 
#to add new attribute to those of the parent:

    def __init__(self, name, age):
        super().__init__(name,age)
        self.big_ears = True
        
    
    def run (self):
        print(f"{GermanShepard} can run very fast")
        
        #inheritace of inheritance - grandchild
class GuideDog(GermanShepard):
     def guide_people(self) :
         print("I guide people")
        
        
        

    