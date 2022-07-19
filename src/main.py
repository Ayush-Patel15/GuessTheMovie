from helpers import filling_movie_name, movie_showboard, number_of_players, player_move, removing_spaces, VOWELS, INTEGERS, SYMBOLS, ALPHABETS
from get_movie import get_movie_name
from create_players import HumanPlayer


movie_name = get_movie_name()
# print(movie_name)
index = 0
guessed_letters = []
winner = False

print("############# HUMAN PLAYERS  #############")
num_of_human = number_of_players(0,4)

if type(num_of_human) is int:
    human_players = [HumanPlayer(input("Enter Name of player {0}: ".format(i+1))) for i in range(num_of_human)]

    print(movie_showboard(movie=movie_name, guessed=guessed_letters))

    while True:
        player = human_players[index]
        print("\n{0}'s turn..!".format(player.name))
        guess = player_move(player)
        # print(guess)

        if guess == "EXIT":
            print("Thank You for your time {0}..! Please come back to GuessTheMovie.".format(player.name))
            break
        elif guess == "PASS":
            print("{0} passes..!".format(player.name))
        elif len(guess) == 1:
            if (guess in VOWELS):
                print("{0} is a vowel".format(guess))
            elif (guess in INTEGERS):
                print("{0} is an integer".format(guess))
            elif (guess in SYMBOLS):
                print("{0} is a symbol".format(guess))
            elif (guess in guessed_letters):
                print("{0} is already guessed! Guess another..!".format(guess))
                continue
            elif (guess in ALPHABETS):
                guess = guess
                guessed_letters.append(guess)
                count = movie_name.count(guess)
                print("{0}'s guesses {1}".format(player.name, guess))
                print("Movie has {0} {1}.".format(count, guess))
                print(movie_showboard(movie=movie_name, guessed=guessed_letters))

                movie_title = filling_movie_name(movie=movie_name,guessed=guessed_letters)
                if removing_spaces(movie_title) == removing_spaces(movie_name):
                    winner = player
                    break

            else:
                print("Invalid Guess")
        
        else:
            if guess == movie_name:
                winner = player
                break
            else:
                print("{0} is not the correct movie.".format(guess))

        index = (index + 1) % len(human_players)


    ##### WINNER DECLARATION

    if winner:
        print("{0} WINS..! Correct movie name was {1}.".format(winner.name, movie_name))
    else:
        print("NoBody Wins..! Movie name was {0}".format(movie_name))
else:
    print(num_of_human)

            
if __name__ == "__main__":
    pass
