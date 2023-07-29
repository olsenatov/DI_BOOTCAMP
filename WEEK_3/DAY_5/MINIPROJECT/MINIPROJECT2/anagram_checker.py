class AnagramChecker:
    def __init__(self, word_list_file):
        with open(word_list_file, "r") as file:
            self.word_list = set(word.strip().lower() for word in file)
    
    def is_valid_word(self, word):
        word = word.lower()
        return [anagram for anagram in self.word_list if self.is_anagram(word, anagram)]
    
    def get_anagrams(self, word):
        word = word.lower()
        return [anagram for anagram in self.word_list if self.is_anagram(word, anagram)]
    
    def is_anagram(self, word1, word2):
        return sorted(word1) == sorted(word2)
    