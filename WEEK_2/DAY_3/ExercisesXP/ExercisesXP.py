#Exercise_1
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]

# new_dict = dict(zip(keys, values))

# print("here is a dictionary: ", new_dict)
    

#Exercise_2

# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
# tp_under_3 = 0
# tp_3_12 = 10
# tp_over_12 = 15

# total_cost = 0

# for member, age in family.items():
#     if age <= 3:
#         ticket_cost = tp_under_3
#     elif age <= 12:
#          ticket_cost = tp_3_12
#     else:
#         ticket_cost = tp_over_12

#     total_cost+=ticket_cost 
#     print(f"The ticket cost for {member} is ${ticket_cost}") 
# print(f"Total cost for your family is ${total_cost}")  
    
#Bonus 
# family = {} #goes instead of assigned family dictionary

              #goes in between total cost and for loop
# num_members = int(input("Enter the number of family members: ")) 
# for i in range(num_members):
#     name = input(f"Enter the name of family member {i+1}: ")
#     age = int(input(f"Enter the age of family member {i+1}: "))
#     family[name] = age


#Exercise_3
# brand = {
#     "name": "Zara",
#     "creation_date": 1975,
#     "creator_name": "Amancio Ortega Gaona",
#     "type_of_clothes": ["men", "women", "children", "home"],
#     "international_competitors": ["Gap", "H&M", "Benetton"],
#     "number_stores": 7000,
#     "major_color": {
#         "France": "blue",
#         "Spain": "red",
#         "US": ["pink", "green"]}
# }
# print(brand)

# brand["number_stores"] = 2

# print(brand)

# print("Zara's clients are", brand["type_of_clothes"])

# brand["country_creation"] = "Spain"
# print(brand)

# if "international_competitors" in brand:
#     brand["international_competitors"].append("Desigual")

# print(brand)

# del brand["creation_date"]
# print(brand)
# print("The last int competitor from the list is : ", brand["international_competitors"][-1])

# print("major colors in US: ", brand["major_color"]["US"][0], brand["major_color"]["US"][1])

# num_key_value = len(brand) 
# print(num_key_value)

# for key in brand:
#   print(key)
  
# more_on_zara = {
#     "creation_date": 1975,
#     "number_stores": 10000,
# }
# brand.update(more_on_zara)
  
# print(brand)
# print(brand["number_stores"])


#Exercise_4

# users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

# disney_users_A = {}

# for i, user in enumerate(users):
#     disney_users_A[user] = i
#     print(disney_users_A)

# disney_users_B = {}
# for i, user in enumerate(users):
#     disney_users_B[i] = user
#     print(disney_users_B)
    
# disney_users_C = {}
# disney_users_sort = sorted(users)
# for i, user in enumerate(disney_users_sort):
#     disney_users_C[user] = i
#     print(disney_users_C) 

# filter_i = {name: value for name, value in disney_users_A.items() if 'i' in name}

# print("dictionary for words only with letter i :", filter_i)

# filter_mp = {name: value for name, value in disney_users_A.items() if name[0].lower() in ['m', 'p']}
# print("dictionary for words starting with m or p :", filter_mp)
