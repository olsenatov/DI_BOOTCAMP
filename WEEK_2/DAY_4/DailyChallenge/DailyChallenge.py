
def decode(matrix):
    secret_message = " "
    
    for column in range(len(matrix[0])):
        for row in range(len(matrix)):
            char = matrix[row][column]
            if char.isalpha():
                secret_message += char
            elif char == "#":
                secret_message += " "
    return secret_message
    
def main():
    matrix = [
        "7ii",
        "Tsx",
        "h%?",
        "i #",
        "sM ",
        "$a ",
        "#t%",
        "^r! "
    ]
    
    secret_message = decode(matrix)
    
    print("the secret message is: \n", secret_message)
    
main()