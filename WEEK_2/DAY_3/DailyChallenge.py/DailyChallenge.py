#Challenge_1
# user_word = input("Enter a word: ")

# letter_index = {}

# for index, letter in enumerate(user_word):
#     if letter in letter_index:
#         letter_index[letter].append(index) 
#     else:
#         letter_index[letter] = [index]  

# print(letter_index)


#Challenge_2

items_purchase = {
    "Water": "$2",
    "Bread": "$3",
    "TV": "$1,000",
    "Fertilizer": "$20",
    "Apple": "$4",
    "Honey": "$3",
     "Fan": "$14",
     "Bananas": "$4",
    "Pan": "$100",
    "Spoon": "$2",
     "Phone": "$999",
    "Speakers": "$300",
    "Laptop": "$5,000",
    "PC": "$1200"
}

wallet = "$" + input("Write how much money is in your wallet in dollars: ") 
wallet_amount = int(wallet.replace("$", "").replace(",", ""))


affordable = []

for item, price in items_purchase.items():
    item_price = int(price.replace("$", "").replace(",", ""))
    if wallet_amount >= item_price:
        affordable.append(item)  
        
affordable.sort()

if affordable:
    print("You can afford: ", affordable)
else:
    print("You can afford nothing")