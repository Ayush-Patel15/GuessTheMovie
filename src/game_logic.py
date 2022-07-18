from create_players import HumanPlayer

def number_of_players(min, max):
    n = input("Number of Players: ")
    try:
        n = int(n)
        if n <= min:
            output = "There should be atleast 1 player to play the game."
        elif n > max:
            output = "Maximum limit of players is 4."
        else:
            output = n
    except Exception:
        output = "Invalid Integer! Please enter a valid integer."
    # print(type(output))
    return output


print("############# HUMAN PLAYERS  #############")
num_of_human = number_of_players(0,4)

human_players = [HumanPlayer(input("Enter Name of player {0}: ".format(i+1))) for i in range(num_of_human)]


if __name__ == "__main__":
    # print(number_of_players(0, 4))
    pass