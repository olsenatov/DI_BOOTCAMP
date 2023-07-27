#for bonus

import string
import re
from nltk.corpus import stopwords #pip install --user -U nltk
from nltk.tokenize import word_tokenize #pip install --user -U nltk


#part 1
class Text:
    def __init__(self, text):
        self.text = text
        
    def word_freq(self, word):
        word_list = self.text.split()
        word_count = word_list.count(word)
        
        if word_count == 0:
            return None
        else:
            return f"The word *{word}* appears in text {word_count} times"

    def most_common(self):
        word_list = self.text.split()
        word_count_dict = {}
        for word in word_list:
            word_count_dict[word] = word_count_dict.get(word, 0) + 1
            
        if not word_count_dict:
            return None

        most_common = max(word_count_dict, key = word_count_dict.get)
        return f"The most common word is {most_common}"
    #added as part 2
    @classmethod
    def from_file(cls, file_path):
        with open(file_path, "r") as file:
            text = file.read()
        return cls(text)
    
example = "A good book would sometimes cost as much as a good house." 
text_anylyzer = Text(example)       
        

#word_frequency method
print(text_anylyzer.word_freq("as"))
print(text_anylyzer.word_freq("would"))

#  most_common method
print(text_anylyzer.most_common())

# part 2 analyze from text
text_inst = Text.from_file("the_stranger.txt")

print(text_inst.word_freq("will"))
print(text_inst.most_common())


#bonus

class TextModification(Text):
    def __init__(self, text):
        super().__init__(text)
        
    def remove_punct(self):
        no_punct_text = self.text.translate(str.maketrans("", "",string.punctuation))
        return no_punct_text

    def remove_stop_words(self):
        stop_words = set(stopwords.words("english"))
        words = word_tokenize(self.text)
        filtered_words = [word for word in words if word.lower() not in stop_words]
        return " ".join(filtered_words)
    
    def remove_special_char(self):
        no_special_char_text = re.sub(r'[^a-zA-Z0-9\s]', '', self.text)
        return no_special_char_text
    
example2= "I had to run to catch the bus. I suppose it was my hurrying like that, what with the glare off the road and from the sky, the reek of gasoline, and the jolts, that made me feel so drowsy. Anyhow, I slept most of the way. "    
text_anylyzer2 = TextModification(example2) 
#punctuation removal
print(text_anylyzer2.remove_punct())  

# remove_stop_words 
print(text_anylyzer2.remove_stop_words()) 

#remove_special_char
print(text_anylyzer2.remove_special_char())  
