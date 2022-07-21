## Import Statements
import random

## Global Variables
# VOWELS = ["A","E","I","O","U"]
ALPHABETS = "BCDFGHJKLMNPQRSTVWXYZ"
VOWELS = "AEIOU"
INTEGERS = "0123456789"
SYMBOLS = ["-","!","$","&",",",".","'",":","?"," ","~"]


## Filling the _ _ movie_name with vowels and guessed letters
def filling_movie_name(movie, guessed=[]):
    movie_name = ""
    for char in movie:
        if (char in VOWELS) or (char in INTEGERS) or (char in SYMBOLS) or (char in guessed):
            movie_name = movie_name + char + "  "
        else:
            movie_name = movie_name + "_" + "  "
    # print(movie)
    return movie_name


## The showboard to display the movie_name.
def movie_showboard(movie, guessed):
    title = filling_movie_name(movie, guessed)
    return """\n
    ********************  GUESS  ********************\n
    {0}\n
    *************************************************
    """.format(title.replace("-",""))


## Taking input for number of players
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


## Removing the spaces, and special symbols to match the movie_name with guessed movie_title
def removing_spaces(string):
    return string.replace(" ","").replace("-","").replace("~","")


## A spin_wheel function to make the game interesting by adding additional rewards and punishments.
def spin_wheel():
    options_dict = [
        {"CHANCE": "Won a 5D-4N tour of Mumbai-Pune."},
        {"CHANCE": "Won a brand new Pulsar 150 Bike."},
        {"CHANCE": "Won a cash prize of Rs.1,00,000."},
        {"CHANCE": "Won a 1D free family tour of Imagica."},
        {"CHANCE": "Nothing in hand! Just blessings.."},
        {"CHANCE": "Nothing in hand! Just blessings.."},
        {"CHANCE": "Nothing in hand! Just blessings.."},
        {"PASS": "Chance has passed..!"},
        {"PUNISHMENT": "Go to Jail..! Kidding..!"},
        {"PUNISHMENT": "Pay Rs.2000 for your birthday party"}
    ]
    result = random.choice(options_dict)
    return result


if __name__ == "__main__":
    # "movie" should be in upper case letters.
    # print(filling_movie_name(get_movie_name()))
    # print(filling_movie_name("BLACK PANTHER-2",["B","N","R"]))
    # print(number_of_players(0, 4))
    # obj = HumanPlayer("Ayush")
    # print(player_move(obj))
    # print(spin_wheel())
    print(movie_showboard("BLACK PANTHER-2",["B","N","R"]))
    # print(removing_spaces_n_symbols("~Z-O-M-B-I-E-S~"))
