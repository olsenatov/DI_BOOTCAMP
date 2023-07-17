# #challenge_1
# number = int(input("enter a number: \n"))
# length = int(input("enter the needed length \n"))

# l_multiples = []

# for i in range(1, length + 1):
#    l_multiples.append(number * i)
   
# print("list of multiples: ", l_multiples)


#challenge_2

user_string = input("Enter a string: \n")

output = user_string[0]

for i in range(1, len(user_string)):
    if user_string[i] != user_string[i - 1]:
        output += user_string[i]
        
print("new string with any duplicate consecutive letters removed: \n", output)