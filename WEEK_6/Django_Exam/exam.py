# #Which of the following is not a mutable data type in Python?
# #a) List
# #b) Dictionary
# #c) Tuple
# # d) Set
# answer is: c) tuple


# # Using a list comprehension, generate a list of the squares of numbers from 1 to 10, 
# # but only include squares of even numbers.
# even_squared= []
# for x in range(1, 11):
#     if x % 2 == 0:
#         even_squared.append(x ** 2)
# print(even_squared)


# # Using the range function, create a list of numbers from 1 to 10, 
# # then print numbers that are divisible by both 2 and 3.
# div_2_3 = []

# for num in range(1, 11):
#     if num % 2 == 0 and num % 3 == 0:
#         div_2_3.append(num)

# print(div_2_3)


#Loop through the provided list of dictionaries and print the names and ages:
# student_list = [
#     {
#     "name": "John", 
#     "age": 24
#     }, 
#     {
#     "name": "Anna", 
#     "age": 22
#     }, 
#     {
#     "name": "Mike", 
#     "age": 25
#     }
# ]
# for student in student_list:
#     name = student["name"]
#     age = student["age"]
#     print(f"Name: {name}, Age: {age}")
 
 
#Write a function combine_words that accepts any number of positional arguments and key-value arguments. 
#The function should return a single sentence combining all the words provided.   
# def combine_words(*args, **kwargs):
#     sentence = ""
#     for arg in args:
#         sentence += arg + " "
#     for key, value in kwargs.items():
#         sentence += f"{key} {value} "
#     return sentence[:-1] 

# print(combine_words("Hello", "world", second="is", third="great!", first="Python"))
####can't get it to print it without second, third and first

#Create a class Vehicle with string attributes type, brand, and integer attribute year. 
# Ensure instances of the vehicle cannot be created if any of these attributes are missing and include a method to display the vehicle’s info. 
# Use dunder method.
# class Vehicle:
#   def __init__(self, type, brand, year):
#     if not type:
#       raise ValueError("type is required")
#     if not brand:
#       raise ValueError("brand is required")
#     if not year:
#       raise ValueError("year is required.")

#     self.type = type
#     self.brand = brand
#     self.year = year

#   def display_info(self):
#     print(f"Type: {self.type}")
#     print(f"Brand: {self.brand}")
#     print(f"Year: {self.year}")

# vehicle = Vehicle("bike", "harleydavidson", 2010)
# print(vehicle)
# vehicle.display_info()


#Create a class Car with string attributes brand, model, and integer attribute mileage. Implement a method to return the car’s details.
#Create a subclass ElectricCar inheriting from Car with an additional float private attribute __battery_capacity. Override the car’s details method to include the battery capacity.
#Use the @property decorator to get the battery_capacity value and @battery_capacity.setter to modify the battery capacity only if the new value is positive.

# class Car:
#     def __init__(self, brand, model, mileage):
#         self.brand = brand
#         self.model = model
#         self.mileage = mileage
    
#     def car_details(self):
#         return f"brand: {self.brand}, model: {self.model}, mileage: {self.mileage}"

# class ElectricCar(Car):
#     def __init__(self, brand, model, mileage, battery_capacity):
#         super().__init__(brand, model, mileage)
#         self.battery_capacity = battery_capacity
    
#     @property
#     def battery_capacity(self):
#         return self.battery_capacity
    
#     @battery_capacity.setter
#     def battery_capacity(self, new_capacity):
#         if new_capacity > 0:
#             self.battery_capacity = new_capacity


#Create a BankAccount class with private float attribute _balance and private string attribute _account_holder. 
#Implement methods to deposit, withdraw, and view the balance. 
# Include a class method to track accounts created and a static method for a bank policy message. 
# Ensure the balance is non-negative.

# class BankAccount:
#     total_accounts = 0

#     @staticmethod
#     def bank_policy():
#         return "this is very secure bank"

#     def __init__(self, account_holder, initial_balance=0.0):
#         self.account_holder = account_holder
#         self.balance = max(0.0, initial_balance)
#         BankAccount.total_accounts += 1

#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             return True
#         else:
#             return False

#     def withdraw(self, amount):
#         if 0 <= amount <= self.balance:
#             self.balance -= amount
#             return True
#         else:
#             return False

#     def view_balance(self):
#         return self.balance

#     @classmethod
#     def total_accounts(cls):
#         return cls.total_accounts


##sorry didn't have time to transfer to jupyter notebook
#Create a numpy array of shape (3,3) filled with integers from 1 to 9 using arange().
# import numpy as np

# array = np.arange(1, 10).reshape(3, 3)
# print(array)

# import matplotlib.pyplot as plt
# import pandas as pd
# df = pd.DataFrame({'A': [1, 'apple', 3, 4, 'banana'], 'B': [5, 6, 7, 8, 9]})

# df['A'] = pd.to_numeric(df['A'])

# mean_A = df['A'].mean()

# df['A'].fillna(mean_A, inplace=True)

# plt.hist(df['A'], bins=10)
# plt.xlabel('Value')
# plt.ylabel('Frequency')
# plt.title('Histogram of Column A')
# plt.show()

##for columns:
# plt.figure(figsize=(10, 6)) 
# plt.plot(df['A'], label='Column A')
# plt.plot(df['B'], label='Column B')
# plt.xlabel('Index')
# plt.ylabel('Value')
# plt.title('Plot of Columns A and B')
# plt.legend()
# plt.show()

