# sample_dict = { 
#    "class":{ "student":{ "name":"Mike", "marks":{  "physics":70, "history":80
#          }
#       }
#    }
# }

# print("the history value is:", sample_dict["class"]["student"]["marks"]["history"])

# sample_dict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"

# }




# del sample_dict["name"]
# del sample_dict["salary"]
# print(sample_dict)


# x = 0
# while x < 5:
#     print(f'x is {x}')
#     x += 1
# else:
#     print('x is bigger than 5')


while True:
    s = input('Enter something or "quit" to exit: ')
    if s == 'quit':
        break
    if len(s) < 10:
        print('Too small')
        continue
    print('Input is of sufficient length')
    