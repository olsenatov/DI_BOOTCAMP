# Part 1. Quizz
#*don't know if i'm supposed to answer these q here, but ok*

# What is a class?
#It's template for creating objects in OOP. It usually has a set of attributes and methods per object. Class encapsulates data.
# What is an instance?
#It's an object created from some class to represent a real thing or some abstract concept
# What is encapsulation?
#1 of 4 principles of OOP. This is a concept of building attributes and methods, basically data, within a single unit, for example class. You can manipulate it only within that object by methods, and not with any external code. 
# What is abstraction?
#Another principle of OOP. This allows to focus on what objest does rather than on how it's being done, so that it simplifyes complex subjects and defies only essential features.
# What is inheritance?
#This principle allows class inherit attributes and methods from another class, plus extend and specialize that functionality, modify the inherited features. 
# What is multiple inheritance?
#This means that class can inherit from more than one class (parent), but it can be rather confusing, even though powerful sometimes.
# What is polymorphism?
#This principle allows a single interface represent various types of objects, and also provides functuonality to use them interchangeably. (but to be honest, I don't get it that good just yet - maybe haven't got enough practice) 
# What is method resolution order or MRO?
#This is what happens, when there's multiple inheritance - there's like an order of inheritance determination going - creating a hierarchy of methods calling of multiple parent classes

#part 2
import random

class Card:
    def __init__(self, suit, value):
        self.suits = suit 
        self.values = value 
        
    def __str__(self):
        return f"{self.values} of {self.suits}"
    
class Deck:
    def __init__(self):
        self.suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self.values =  ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = [Card(suit,value) for suit in self.suits for value in self.values]
        
    def shuffle(self):
        random.shuffle(self.cards)
        
    def deal(self):
        if not self.is_empty():
            return self.cards.pop()
        else:
            return None
        
    def is_empty(self):
        return len(self.cards) == 0
    
    
deck = Deck()
      
deck.shuffle()
    # print(deck) #checking

for _ in range (51): #53 - writes the deck is empty, from 1 to 53 deals randomly
    card = deck.deal()
    if card:
        print(card)
    else: 
        print("the deck is empty")


