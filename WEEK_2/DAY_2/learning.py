# counter = 0

# counter += 1
# counter += 1
# counter += 1
# counter += 1
# counter -= 1
# counter *=2

# print(counter)

# all_colors = ["red", "blue, yellow"]

# user_answer = input("give me a number and a color devided by a dash \n")

# list_answer = user_answer.split("-")

# all_colors.insert(int(list_answer[0]), list_answer[1])

# print(all_colors)


# for num in range(0,15):
#     if num%2 == 0:
#         print("the number is even") #result = "even"
#     else:
#         print("the numbe is odd")  #result = "odd"
        
#print(f"the number {num} is {result}")

# a_tuple = (10, 20, 30, 40)
# a, b, c, d = a_tuple
# print(a) # should print 10
# print(b) # should print 20
# print(c) # should print 30
# print(d) 

# active = True

# while active: 
#     city = input("Please enter the name of a city you have visited (enter 'quit' when you are finished): ")
#     if city == 'quit':
#         active = False
#     elif city == 'leave me alone':
#         active = False
#     elif city == 'stop':
#         active = False
#     else:
#         print("I'd love to go to", city)

# print("Goodbye !")

secret_number = 4

while True:
  user_number = input('Guess the secret number: ')
  if int(user_number) == secret_number:
    print('Congrats! You win!')
    break
  else:
    print('Wrong guess...')
    