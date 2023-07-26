# exercise_1

# class Currency:
#     def __init__(self, currency, amount):
#         self.currency = currency
#         self.amount = amount
        
#     def __str__(self):
#         return f"{self.amount} {self.currency}" + ("s" if self.amount != 1 else "")
    
#     def __int__(self):
#         return self.amount
    
#     def __repr__(self):
#         return f"{self.amount}{self.currency}"
    
#     def __add__(self, other):
#         if isinstance(other, (int, float)):
#             return Currency(self.currency, self.amount + other)
#         elif isinstance(other, Currency):
#             if self.currency == other.currency:
#                 return Currency(self.currency, self.amount + other.amount)
#             else:
#                 raise TypeError(f"Cannot add between types {self.currency} and {other.currency}")
#         else:
#             raise TypeError(f"Unsupported type for Currency {type(other).__name__}")
    
#     def __add__(self, other):
#         if isinstance(other, (int, float)):
#             self.amount += other
#         elif isinstance(other, Currency):
#             if self.currency == other.currency:
#                 self.amount +=other.amount
#             else:
#                 raise TypeError(f"Cannot add between types <{self.currency}> and <{other.currency}>")
#         else:
#             raise TypeError(f"Unsupported type for Currency {type(other).__name__}") 
#         return self

#testing
# c1 = Currency("dollar", 5)
# c2 = Currency("dollar", 10)
# c3 = Currency("shekel", 4)
# c4 = Currency("shekel", 8)

# print(str(c1))
# print(int(c1))
# print(repr(c1))

# print(c1 + 5)
# print(c2 + c2)

# print(c1)

# c1+=5
# print(c1)

# c1 += c2
# print(c1)

# c1 +c3


# exercise_2
#look files func.py & ex_one.py


#exercise_3

# from random import randint

# def roll_check(user_number):
#     if not 1 <= user_number <= 100:
#         # user_number = int(input("please enter a number between 1 and 100"))
#         return
#     random_number = randint(1,100)
    
#     print (f"you chose: {user_number}")
#     print(f"randomly rolled: {random_number}")
    
#     if user_number == random_number:
#         print("Congrats, it's a match!")
#     else:
#         print("Good luck next time")
# user_number = int(input("Enter a number between 1 and 100 :"))

# roll_check(user_number)


#exercise_4
# import string
# import random

# def generate_random_string(length = 5):
#     letters = string.ascii_letters
#     random_string = " ".join(random.choice(letters) for _ in range(length))
#     return random_string

# random_string = generate_random_string()
# print(random_string)


#exercise_5

# import datetime

# def display_current_date():
#     current_date = datetime.datetime.now().date()
#     print(f"Current date is: {current_date}")
    
# display_current_date()


#exercise_6
# import datetime 

# def time_left_1stjan():
#     current_date = datetime.datetime.now().date() 
#     current_datetime = datetime.datetime.combine(current_date, datetime.datetime.min.time())
#     jan1st = datetime.datetime(current_date.year + 1, 1, 1)
#     time_left = jan1st - current_datetime
    
    
#     total_seconds_left = time_left.total_seconds()
#     days_left = int(total_seconds_left // (3600 * 24))
#     total_seconds_left %= (3600 * 24)
#     hours_left = int(total_seconds_left // 3600)
#     total_seconds_left %= 3600
#     minutes_left = int(total_seconds_left // 60)
#     seconds_left = int(total_seconds_left % 60)
    
#     print(f"The 1st of Januay is in {days_left} days and {hours_left}:{minutes_left}:{seconds_left} hours")
    
# time_left_1stjan() 

#can't make it count down in hours minutes seconds


#exercise_7
# import datetime

# def minutes_lived(birthdate):
    
#         birthdate = datetime.datetime.strptime(birthdate, "%Y-%m-%d")
#         current_date = datetime.datetime.now()
#         time_lived = current_date - birthdate
#         minutes_lived = time_lived.total_seconds()/60
        
#         print(f"You have lived for around {minutes_lived} minutes")
    

# user_birthdate = input("Enter your birthdate (YYYY-MM-DD): ")
# minutes_lived(user_birthdate)


#exercise_8
# from faker import Faker

# fake = Faker()
# users = []

# def add_user():
#     user_data = {
#         "name" : fake.name(),
#         "address" : fake.address(),
#         "language_code" : fake.language_code()
#     }
    
#     users.append(user_data)
    
# add_user()
# add_user()

# print(users)
