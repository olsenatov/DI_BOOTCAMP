def count_repeat(string, charachter):
    count = 0
    for char in string:
        if char == charachter:
            count +=1
    return count

def main():
    user_string = input("Enter a string: ")
    user_charachter = input("Enter a character:")
    
    if len(user_charachter) != 1:
        print("Please enter only one character")
        return
    
    occurre_n = count_repeat(user_string, user_charachter)
    
    print(f"The charachter'{user_charachter}' appears {occurre_n} times in the string")

main ()