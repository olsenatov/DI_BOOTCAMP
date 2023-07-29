from game import Game

def get_user_menu_choice():
    while True:
        print("Menu")
        print("1.Play a new game")
        print("2.Show scores")
        print("3.Quit")
        choice = input("enter your choice (1, 2, 3): ")
        if choice in ["1", "2", "3"]:
            return choice
        else:
            print("Invalid, select from the 3 options")
            
def print_results(results):
    print("\n Results of the game: ")
    for outcome, count in results.items():
        print(f"{outcome.capitalize()}:{count}")
        
def main():
    game = Game()
    results = {"win": 0, "loss" : 0, "draw" : 0}
    
    print("Rock-Paper_Scissors!")
    while True:
        choice = get_user_menu_choice()
        
        if choice == "1":
            result = game.play()
            results[result] +=1
        elif choice == "2":
            print_results(results)
        elif choice == "3":
            print_results(results)
            print("Thanks for the play")
            break

main()