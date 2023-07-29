from anagram_checker import AnagramChecker

def validate_input(word):
    words = word.split()
    if len(words) != 1:
        return False
    return words[0].isalpha()

def get_valid_input():
    while True:
        word = input("Enter a word (or *exit* to quit): ").strip()
        if word.lower() == "exit":
            return None
        if validate_input(word):
            return word
        print("invalid. Enter a single word, english aphabet only")
        
def display_anagrams(word, anagrams):
    print(f"Your word *{word}*")
    if anagrams:
        print("this is a valid english word")
        print("Anagrams are: ", ','.join(anagrams))
    else:
        print("This word has no anagrams or not valid")
        
def main():
    anagram_checker = AnagramChecker("anagram.txt")
    
    while True:
        word = get_valid_input()
        if word is None:
            break
        
        if anagram_checker.is_valid_word(word):
            anagrams = anagram_checker.get_anagrams(word) 
            display_anagrams(word, anagrams)
        else:
            print("this is not valid word")

main()
            
            
