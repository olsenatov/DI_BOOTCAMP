# def say_hello(name):
#     '''printing str:hello'''
#     print(f'hello {name}')
   
    
# say_hello(name)

# print(say_hello.__doc__) #calling the function
# say_hello("Donald")
# say_hello("Anna")


# def say_hello(name, language):
#     '''printing str:hello to the name with specified language'''
#     if language == "EN":
#          print(f'hello {name}')
#     elif language == "RU":
#         print(f"privet {name}")
#     else: 
#         print("Sorry, this function doesn't support other languages")

# say_hello(name = "Olga", language = "RU")

# def calculation(a, b):
#     """calculate addition and subtraction of a and b"""
#     # print(f"{a} + {b}") 
#     # print(f"{a} - {b}") 
#     result = a + b
#     return print(result)

# calculation(40, 10)

# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron'] 
# completed_models = []

# # Simulate printing each design until none are left. 
# # Move each design to completed_models after printing. 

# while len(unprinted_designs) != 0:    
#     current_design = unprinted_designs.pop() 

#     # Simulate creating a 3D print from the design.    
#     print("Printing model: " + current_design)    
#     completed_models.append(current_design)    

# # Display all completed models. 
# print("\nThe following models have been printed:") 
# for completed_model in completed_models:    
#     print(completed_model)
    
    
lst = [1, 2, 3, 4, 5, 6, 7]
print(lst[0:4])
print(lst[::])
print(lst[::-1])
    