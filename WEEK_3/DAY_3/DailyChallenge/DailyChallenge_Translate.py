from googletrans import Translator

def translate_french_words(french_words):
    translator = Translator()
    
    translations = {}
    for word in french_words:
        translation = translator.translate(word, src = "fr", dest="en").text
        translations[word] = translation
        
    return translations

french_words= ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"] 

translations = translate_french_words(french_words)

print(translations)
