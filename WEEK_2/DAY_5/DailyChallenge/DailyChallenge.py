# Challenge_1

# def main():
#   user_input = input("Enter words separated by comma: ")
#   words = [word.strip() for word in user_input.split(",")]
#     #print(words)
#   separate_words = sorted(words)
#   output = ",".join(separate_words)
#   print(f"Sorted words are: {output}")
  
# main ()


#challenge_2

def longest_word(sentence):
    words = sentence.split()
    longest = ""
    
    for word in words:
        clean_word = "".join(c for c in word if c.isalnum())
        if len(clean_word) > len(longest):
            longest = clean_word
    return longest

def main():
    input_sentence = input("Enter a sentence: ")
    result = longest_word(input_sentence)
    print(f"The Longest Word is: {result}")
    
main()