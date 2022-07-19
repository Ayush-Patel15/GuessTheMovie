import random

# VOWELS = ["A","E","I","O","U"]
ALPHABETS = "BCDFGHJKLMNPQRSTVWXYZ"
VOWELS = "AEIOU"
INTEGERS = "0123456789"
SYMBOLS = ["-","!","$","&",",",".","'",":","?"," "]

def filling_movie_name(movie, guessed=[]):
    movie_name = ""
    for char in movie:
        if (char in VOWELS) or (char in INTEGERS) or (char in SYMBOLS) or (char in guessed):
            movie_name = movie_name + char + "  "
        else:
            movie_name = movie_name + "_" + "  "
    # print(movie)
    return movie_name


def movie_showboard(movie, guessed):
    title = filling_movie_name(movie, guessed)
    return """
    ********************  GUESS  ********************\n
    {0}\n
    *************************************************
    """.format(title)


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


def player_move(player):
    guess = player.human_get_move()
    return guess


def removing_spaces(string):
    return string.replace(" ","")


# def wheel_spin():
#     option = random.choice(["CASH","LOSETURN","PRISON"])
#     return option

if __name__ == "__main__":
    # "movie" should be in upper case letters.
    # print(filling_movie_name(get_movie_name()))
    # print(filling_movie_name("BLACK PANTHER-2",["B","N","R"]))
    # print(number_of_players(0, 4))
    # obj = HumanPlayer("Ayush")
    # print(player_move(obj))
    # print(wheel_spin())
    print(movie_showboard("BLACK PANTHER-2",["B","N","R"]))