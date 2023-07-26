# Exercise - Exception
# Create a colorize(text, color) function that contain this tuple colors = ('cyan', 'yellow', 'blue', 'green', 'magenta')
# If the color parameter is not present in the tuple, raise a ValueError exception
# If the text parameter is not a string raise a TypeError Exception
# make sure to catch the exception


# def colorize(text, color):
  
#     colors = ('cyan', 'yellow', 'blue', 'green', 'magenta')
    
#     try:
#         if color not in colors:
#             raise ValueError('Invalid Color, availablr are cyan, yellow, blue, green, magenta')
     
#         if not isinstance(text, str):
#             raise TypeError("text must be a string")
#     except Exception as err:
#         print(err)
#     else:
#         print("everything is ok")
#         #return

    

# text = "Hello colors"
# print(colorize(text, "cyan"))
# print(colorize(123, "cyan"))
     
     
     
# make the address attribute private
# implement a method that return the address of the employee --> getter
# implement a method that modifies the address of the employee, only if the employee is older than 30--> setter
# implement a method create_best_employee that should create a new employee only if their salary is > 30000 --> class method

     
     
class Employee :
    def __init__(self, fname, lname, age, job, salary, address):
        self.firstname = fname
        self.lastname = lname
        self.age = age
        self.job = job
        self.salary = salary
        self._address = address
        
    @property
    def address(self):
        return self._address
    
    @address.setter
    def address(self, new_address):
        try:
            if self.age >= 30:
               self._address = new_address
            else :
                raise TypeError ("Too young employee")
        except Exception as err:
            print(err)
    

    def get_fullname(self) :
        return f"{self.firstname} {self.lastname}"
    
    def happy_birthday(self) :
        self.age += 1

    def get_promotion(self, promotion_amount):
        self.salary += promotion_amount
    
    def __str__(self) :
        return f"{self.get_fullname()} - age : {self.age} - job : {self.job} - salary : {self.salary}"

    def __gt__(self, other_employee) :
        if self.salary > other_employee.salary :
            return self
        else :
            return other_employee
        
    def __add__(self, other_employee) :
        return self.salary + other_employee.salary


     
    
         
     
     
         