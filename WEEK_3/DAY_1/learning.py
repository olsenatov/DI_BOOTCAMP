# OOP
# class Animal:
    
#     def __init__(self, legs, name="Animal"):
#         self.name = name
#         self.legs = legs 
        
#     def voice(self):
#         print(f"{self.name} is calling")
        
#     def jump(self):
#         if self.legs == 0:
#           print(f"{self.name} cannot jump!")
#         else:
#           print(f"{self.name} jumps!")
          
          
# obj1 = Animal(legs = 4, name="Dog")

# obj1.voice()
# obj1.jump()

# obj2 = Animal(legs = 0, name="Snake")

# obj2.voice()
# obj2.jump()



# TYPE HINTS

# def printsmth(some_str:str): #some_dict:dict, some_tuple:tuple, number:int
#     str_cap = some_str.capitalize()
#     print(str_cap)
    
# def add_funct(num1:int, num2:int)-> int:
#     return num1 + num2

# def create_list() -> list(int):
#     return [1,2,3]

# def create_dict() -> dict[str, int]:
#     return {"A" : 1}

#LAMBDA_FUNCTION

# multiply_2 = lambda num : num * 2
# print(multiply_2(4))

a_list = [n for n in range(100)]

print(a_list)

b_list = list(map(lambda num : num * 3, a_list))

print(b_list)

c_list = list(filter(lambda num: False if num % 2 == 1 else True, b_list))
print(c_list)


