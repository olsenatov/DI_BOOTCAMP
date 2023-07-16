# Exercise 1

# print("Hello World \n"*4)


# Exercise 2

# result = int((99**3) * 8)
# print(result)


# Exercise 3

# >>> 5 < 3  False
# >>> 3 == 3 True
# >>> 3 == "3" False
# >>> "3" >= 3 TypeError: '>' not supported between instances of 'str' and 'int'
# >>> "Hello" == "hello"  False


# Exercise 4

# computer_brand = "mac"
# print("I have a", computer_brand, "computer")


# # Exercise 5
# name = "Olga"
# age = "30"
# shoe_size = "Eu39"
# info = f"My name is {name}, and I am {age} years old, and for some reason I want to tell you my shoes size, which is {shoe_size}"
# print(info)


# Exercise 6
# a = 9
# b = 6
# if a > b:
#     print("Hello World")
# else:
#     print("Bye-bye") 


# Exercise 7
# number = input("Write an integer number \n")
# if int(number) %2 == 0:
#     print("this is an even number")
# else:
#     print("this is an odd number")


# Exercise 8
# my_name = "Olga"
# user_name = input("What is your name? \n")
# if user_name == my_name:
#     print("Wow, what a coincidence, mine too!")
# else:
#     print("Nice to meet you!")
    
    
   # Exercise 9
height_inch = input("Before the ride, please define your height in inches \n")
height_cm = float(height_inch)*2.54
if float(height_cm) >= 145:
    print("Welcome to the ride!")
else:
    print("You need to grow up a bit more")