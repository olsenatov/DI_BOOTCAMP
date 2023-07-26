# class A():

#     def dothis(self):
#         print("doing this in A")


# class B(A):
#     pass


# class C():
#     def dothis(self):
#         print("doing this in C")


# class D(B, C):
#     pass

# d_instance = D()
# d_instance.dothis() 


# class Book():
#     def __init__(self, title, author, publication_date, price):
#         self.title = title
#         self.author = author
#         self.publication = publication_date
#         self.price = price

#     def present(self):
#         print(f'Title: {self.title}')

# class Fiction(Book):
#     def __init__(self, title, author, publication_date, price, is_awesome):
#         super().__init__(title, author, publication_date, price)
#         self.genre = 'Fiction'
#         self.is_awesome = is_awesome
#         if self.is_awesome:
#             self.bored = False
#             print('Woow this is an awesome book')
#         else:
#             self.bored = True
#             print('I am very bored')

# if __name__ == '__main__':
#     foundation = Fiction('Asimov', 'Foundation', '1966', '5£', True)
#     foundation.present()
#     print(foundation.price)
#     print(foundation.bored)
#     boring_book = Fiction('boring_guy', 'boring_title', 'boring_date', '9000£', False)
#     print(boring_book.bored)

#Exercise_Lise

class Employee:
    def __init__(self, firstname, lastname, age, job, salary, address):
        self.__firstname = firstname
        self.__lastname = lastname
        self.__age = age
        self.__job = job
        self.__salary = salary
        self.__address = address

    def get_fullname(self):
        return f"{self.__firstname} {self.__lastname}"

    def happy_birthday(self):
        self.__age += 1
        return self.__age

    def get_promotion(self, promotion_amount):
        self.__salary += promotion_amount
        return self.__salary

    def __gt__(self, other):
        return self.__salary > other.__salary

    def __add__(self, other):
        return self.__salary + other.__salary

    def __str__(self):
        return f"{self.__firstname} {self.__lastname} - {self.__age} years old, {self.__job}, Salary: {self.__salary}, Address: {self.__address}"


# Creating two instances of Employee
employee1 = Employee("Lea", "Smith", 30, "developer", 20000, "123 Main Street")
employee2 = Employee("David", "Schartz", 20, "teacher", 17000, "456 Elm Avenue")

# Displaying their attributes
print(employee1.get_fullname())  # Output: Lea Smith
print(employee1.happy_birthday())  # Output: 31
print(employee1.get_promotion(3000))  # Output: 23000
print(employee2.get_fullname())  # Output: David Schartz
print(employee2.happy_birthday())  # Output: 21
print(employee2.get_promotion(2000))  # Output: 19000

# Using dunder methods
print(employee1 > employee2)  # Output: True (since 23000 > 19000)
print(employee1 + employee2)  # Output: 42000 (20000 + 17000)

# Printing the employee info using __str__ method
print(employee1)  # Output: Lea Smith - 31 years old, developer, Salary: 23000, Address: 123 Main Street
print(employee2)  # Output: David Schartz - 21 years old, teacher, Salary: 19000, Address: 456 Elm Avenue


#create 2 files