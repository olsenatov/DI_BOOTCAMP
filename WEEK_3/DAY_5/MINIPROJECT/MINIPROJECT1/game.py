import random

class Game:
    def get_user_item(self):
        while True:
            user_item = input("Select an item(rock/paper/scissors): ").lower()
            if user_item in ["rock", "paper", "scissors"]:
                return user_item
            else:
                print("Invalid choice, Please select from the options provided")
    
    def get_computer_item(self):
        return random.choice(["rock", "paper", "scissors"])
    
    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            return "draw"
        elif user_item == "rock" and computer_item == "scissors" or user_item == "paper" and computer_item == "rock" or user_item =="scissors" and computer_item == "paper":
            return "win"
        else:
            return "loss"
        
    def play(self):
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        
        print(f"You selected{user_item}, the computer selected {computer_item}")
        
        result = self.get_game_result(user_item, computer_item)
        
        if result == "draw":
            print("There's a draw, try once again")
        elif result == "win":
            print("You won!")
        else:
            print("You lost!")
            
        return result