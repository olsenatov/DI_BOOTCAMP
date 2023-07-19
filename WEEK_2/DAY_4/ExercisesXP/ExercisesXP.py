#Exercise_1

# def display_message():
#     print("I am studying in this course to become a full-stack developer")

# display_message()


#Exercise_2

# def favourite_book(title):
#     print(f'One of my favourite books is {title}')
    
# favourite_book("Dune")


#Exercise_3

# def describe_city(city, country = "UK"):
#     print(f"{city} is in {country}")

# describe_city("Glasgow")


#Exercise_4
# from random import randint

# def compare(number):
#     random_number = randint(1, 100)
#     print(random_number)
#     if number == random_number:
#         print("success!")
#     else:
#         print("fail!")
    
# compare(8)
# compare(19)
# compare(25)
# compare(38)
# compare(44)


#Exercise_5

# def make_shirt(size, text2print):
#     print(f"The size of the shirt is {size} and the text is {text2print}")
    
# make_shirt("M", "This is UFO")

# def make_shirt2(size = "L", text2print = "I love Python"):
#     print(f"The size of the shirt is {size} and the text is {text2print}")
    
# make_shirt2()
# make_shirt2("M", )
# make_shirt2("S", "Understandable")


#Exercise_6

# magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
    
# def show_magician(name):
#     for name in magician_names:
#         print(name)
        
# show_magician(magician_names)


# def make_great(name, phrase):
#     great_magicians = []
#     for name in magician_names:
#         great_magicians.append(name + phrase)
#     return great_magicians

# great_result = make_great(magician_names, " The Great")
# print(great_result)


#Exercise_7

# from random import randint

# def get_random_temp(season):
    
#     if season == "Winter":
#      random_temp = randint(-10, 5)   
#     elif season == "Spring":
#      random_temp = randint(10, 24) 
#     elif season == "Summer":
#      random_temp = randint(25, 40)
#     elif season == "Fall":
#      random_temp = randint(6, 14)
#     return random_temp    
       

# user_season = input("please, write a season from the following - Spring, Summer, Fall, Winter: ")    

# def main():
#     temperature = get_random_temp(user_season)
#     print(f"The temperature now is {temperature} degrees Celcius")
#     if temperature < 0:
#         print("Brrr, that’s freezing! Wear some extra layers today")
#     elif temperature < 16:
#         print("Quite chilly! Don’t forget your coat") 
#     elif temperature < 23:
#         print("Nice Weather, enjoy! ") 
#     elif temperature < 32:
#         print("Let's go to the beach! ") 
#     elif temperature < 40:
#         print("Better hug your AC at home! ") 
        
     
# main()

#Exercise_8

data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]

def questions(data):
    correct = 0
    wrong = []
    
    for item in data:
        question = item["question"]
        answer = item["answer"]
        
        user_answer = input(question +"Your answer is: ")
        
        if user_answer == answer:
            print("Correct!")
            correct += 1
        else:
            print(f"Incorrect, the answer is {answer}")
            wrong.append({"question":"answer"})
    return correct, wrong

def show_results(correct, wrong):
    total_q = correct + len(wrong)
    print(f"\n Results: You answered {correct} questions correctly out of {total_q}. \n")
    
        
def main ():
    correct, wrong = questions(data)
    show_results(correct, wrong)
    
main()