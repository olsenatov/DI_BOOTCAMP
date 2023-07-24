#ex_1

class Employee:
    def __init__(self, firstname, lastname, age, job, salary):
        self.f_name = firstname
        self.l_name = lastname
        self.age = age
        self.job = job
        self.salary = salary
        
    def get_fullname(self):
        return self.f_name + self.l_name
    
    def happy_birthday(self):
        self.age += 1
        return self.age
    
    def promotion(self, promotion_amount):
        self.salary += promotion_amount
        print(f"{self.name} was promoted by {promotion_amount}")
    def show_info(self):
        print(f"{self.f_name} {self.l_name} is {self.age} years old, works as {self.job} and earns {self.salary} shekels")
        
        

emp1 = Employee("Lea", "Smith", 30, "developer", 20000)
emp2 = Employee("David", "Schwartz", 20, "teacher", 10000)

# print(emp1)
# print(emp2)

emp1.show_info()
emp2.show_info()

emp1.get_fullname()
emp2.get_fullname()

emp1.happy_birthday()
emp2.happy_birthday()

emp1.promotion(2000)
emp2.promotion(1000)

emp1.show_info()
emp2.show_info()



