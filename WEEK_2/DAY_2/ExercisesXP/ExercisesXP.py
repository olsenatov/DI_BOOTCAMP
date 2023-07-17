#Exercise_1

# myfav_num = {1, 3, 5, 9}
# print("My numbers:",myfav_num) 
# myfav_num.add (4)
# myfav_num.add (7)
# print("Added two numbers \n", myfav_num)

# myfav_num.remove (3)
# print("Removed one number \n", myfav_num)

# friendfav_num = {2, 4, 7, 8}
# print("Friend's numbers:", friendfav_num)
# ourfav_num = myfav_num.union(friendfav_num)
# print(f"This is my and my friend's favourite numbers together:{ourfav_num}")


#Exercise_2

# No, it's not possible to add any elements to the tuple, as the tuple is immutable and can't be modified when created


#Exercise_3

# basket = ["Banana", "Apples", "Oranges", "Blueberries"]

# basket.remove("Banana")
# basket.remove("Blueberries")
# print(basket)

# basket.insert(4, "Kiwi")
# basket.insert(0, "Apples")
# print(basket)

# count = basket.count("Apples")
# print(count)

# basket = []

# print(basket)


#Exercise_4

# integer stands for whole numbers, while floats represent numbers with decimal points
# you can use loop to generate a sequence of floats (can't generate range for floats, as i found out)

# first = 1.5
# last = 5.0
# gain = 0.5

# sequence = []
# new = first
# while new <= last:
#     sequence.append(new)
#     new += gain
    
#     print(sequence)
    
    


#Exercise_5

# sequence = []
# for n in range(1,21):
#     sequence.append(n)
    
# print(sequence)

# for n in range(1,21):
#     if n % 2 ==0:
#      print(n)
     
     
#Exercise_6

# my_name = "Olga"

# while True:
#     username = input("please, write your name \n")
#     if username == my_name:
#         print(f"nice to meet you, {username}, bye-bye")
#         break
#     else:
#         print("Invalid, try again")

        
#Exercise_7

# user_fruits = input("please write your favourite fruits separated by single space only \n")
# fruits_list = user_fruits.split()
# print(fruits_list) 
# new_fruit = input("write any fruit name \n")

# if new_fruit in fruits_list:
#     print("You chose one of your favorite fruits! Enjoy!")
# else:
#     print("You chose a new fruit. I hope you enjoy")
    

#Exercise_8

# add_toppings = []
# price_topping = 2.5
# pizza_price = 10.0

# while True:
#     topping = input("Enter a pizza topping (type 'quit' to exit): ")
#     if topping == "quit":
#         break
#     add_toppings.append(topping)
#     print("Adding " + topping + " to your pizza.")

# total_price = pizza_price + (price_topping * len(add_toppings))

# print("Toppings on your pizza: ", add_toppings)
# print("Total pizza price: $", total_price)


#Exercise_9

#prices
# tp_under_3 = 0
# tp_3_12 = 10
# tp_over_12 = 15

# # Ask ages
# fam_size = int(input("Enter the number of family members:" ))
# total_price = 0

# for i in range(fam_size):
#     age = int(input("Enter the age of family member {}: ".format(i+1))) 

#     if age < 3:
#         ticket_cost = tp_under_3
#     elif age <= 12:
#         ticket_cost = tp_3_12
#     else:
#         ticket_cost = tp_over_12

#     total_price += ticket_cost

# print("Total cost for the family: $", total_price)

# Teenagers Movie Restrictions
# age_restriction_min = 16
# age_restriction_max = 21

# teenagers = ["John", "Emma", "Michael", "Sophia"]

# teenagers_allowed = []
# for teen in teenagers:
#     age = int(input("Enter the age of {}: ".format(teen))) 
#     if age >= age_restriction_min and age <= age_restriction_max:
#         teenagers_allowed.append(teen)
        

# print("Final list of teenagers allowed: ", teenagers_allowed)


#Exercise_10

sandwich_orders = ["Tuna sandwich", 
                   "Pastrami sandwich", 
                   "Avocado sandwich", 
                   "Pastrami sandwich", 
                   "Egg sandwich", 
                   "Chicken sandwich", 
                   "Pastrami sandwich"]

print("Deli has run out of Pastrami.\n")

finished_sandwiches = [] 
  
while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")
print("Preparing other sandwiches from the order")
 
while sandwich_orders:
    sandwich = sandwich_orders.pop(0)
    finished_sandwiches.append(sandwich)
    print("I made your", sandwich)
 
