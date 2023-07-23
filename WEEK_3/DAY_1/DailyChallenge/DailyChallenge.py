class Farm:
    def __init__(self, name):
        self.name = name
        self.animals = {}
        
    def add_animal(self, animal_type, count=1):
        if animal_type in self.animals:
            self.animals[animal_type] += count
        else:
            self.animals[animal_type] = count
    
    def get_info(self):
        info = f"{self.name}'s farm \n"
        for animal, count in sorted(self.animals.items()):
            info += f"{animal} : {count}\n"
        info += "e-i-e-i-o"
        return info
    
    def get_types(self):
        return sorted(self.animals.keys())
    
    def get_short_info(self):
        animal_type = self.get_types()
        types_string = ", ".join(str(animal) for animal in animal_type)
        
        return f"{self.name}'s farm has {types_string}"
        

macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep', 2)
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())
print(macdonald.get_short_info())