# #exercise_1
# import random

# def get_words_from_file(file_path):
#     try:
#         with open(file_path, "r") as file:
#             content = file.read()
#             words = content.split()
#             return words
#     except FileNotFoundError:
#         print("File not found")
#         return []
    
# def get_random_sentence(words, length):
#     if not words:
#         return ""
    
#     if length <2 or length > 20:
#         print("Invalid sentence length. Choose between 2 and 20 words")
#         return ""
    
#     random_words = random.sample(words, length)
#     sentence = " ".join(random_words).lower()
#     return sentence


# def main():
#     print("Generator of random sentences from a file")
#     file_path = "words.txt"
#     words = get_words_from_file(file_path)
    
#     if not words:
#         return
    
#     while True:
#         try:
#             length = int(input("enter the length of the sentence - 2-20 words : "))
#             if 2 <= length <= 20:
#                 break
#             else:
#                 print("Invalid sentence length. Choose between 2 and 20 words")
#         except ValueError:
#             print("Invalid, please enter an integer")
            
#     sentence = get_random_sentence(words, length)
#     if sentence:
#         print(f"generated random sentence: {sentence}")

# main()

# exercise_2

import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

python_dict = json.loads(sampleJson)
print(python_dict)
print(python_dict["company"]["employee"]["payable"]["salary"])
python_dict["company"]["employee"]["birth date"] = "18-02-1993"

new_json_string = json.dumps(python_dict)
print(new_json_string)

with open("dict.json", "w") as file :
    json.dump(python_dict, file, indent = 2)