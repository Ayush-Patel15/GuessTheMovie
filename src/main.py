## Import Statements
from helpers import filling_movie_name, movie_showboard, number_of_players, removing_spaces, spin_wheel, VOWELS, INTEGERS, SYMBOLS, ALPHABETS
from get_movie import get_movie_name
from create_players import HumanPlayer
import time

## GLobal variables
index = 0
guessed_letters = []
winner = False

print("\n############# HUMAN PLAYERS  #############")
num_of_human = number_of_players(0,4)

## Prompting for number of players and level of difficulty
if type(num_of_human) is int:
    human_players = [HumanPlayer(input("Enter Name of player {0}: ".format(i+1))) for i in range(num_of_human)]
    print("\n1 - EASY, 2 - MEDIUM, 3 - DIFFICULT")
    difficulty = input("Level of Difficulty: ")

    movie_name = get_movie_name(difficulty)
    # print(movie_name)

    print("\n")
    print("=="*40)
    print("\n")
    [print("WELCOME {0}..! Your Prize Money is Rs.{1}/-".format(each.name,each.prize_money)) for each in human_players]

    print(movie_showboard(movie=movie_name, guessed=guessed_letters))


    ##########  ACTUAL LOGIC OF GAME    ##########
    while True:
        player = human_players[index]
        print("\n{0}'s turn..!".format(player.name))
        time.sleep(2)
        option = spin_wheel()
        chance = list(option.keys())[0]

        ## Checking for the chance
        if chance == "PASS":
            print("{0} got PASS. {1}".format(player.name, option["PASS"]))
        elif chance == "PUNISHMENT":
            print("{0} got punishment. {1}".format(player.name, option["PUNISHMENT"]))
            player.punish_charge()
        elif chance == "CHANCE":
            print("{0} got CHANCE. {1}".format(player.name, option["CHANCE"]))
            player.add_prize_lst(prize= option["CHANCE"])
            guess = player.human_get_move()
            # print(guess)

            ## Logic of taking the guess and checking
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

                    if count <= 0:
                        player.prize_money = player.prize_money - 50
                    else:
                        player.add_prize_money(count)

                    print("{0}'s guesses {1}".format(player.name, guess))
                    print("Movie has {0} {1}.".format(count, guess))

                    ## Checking for the whole guess as correct or not
                    movie_title = filling_movie_name(movie=movie_name,guessed=guessed_letters)
                    if removing_spaces(movie_title) == removing_spaces(movie_name):
                        winner = player
                        break
        
            else:
                ## If the whole movie is guessed in once. Then, check:-
                if removing_spaces(guess) == removing_spaces(movie_name):
                    winner = player
                    player.add_prize_money(count=len(removing_spaces(guess)))
                    break
                else:
                    print("{0} is not the correct movie.".format(guess))
        
        print("Now, {0}'s total prize money is Rs.{1}/-".format(player.name,player.prize_money))
        print(movie_showboard(movie=movie_name, guessed=guessed_letters))
        print("\nGuessed letters are: ",guessed_letters)

        index = (index + 1) % len(human_players)


    ##########  WINNER DECLARATION  ##########

    if winner:
        print("\n\n{0} WINS..! Correct movie name was {1}.\nCongratulations..! Your winning prize amount is Rs.{2}/-.".format(winner.name, movie_name,winner.prize_money))
        print("Additional prizes you won are :")
        [print(prize) for prize in set(winner.prizes_lst)]
    else:
        print("NoBody Wins..! Movie name was {0}".format(movie_name))

## If limit of players is either low or out of bound on higher side
else:
    print(num_of_human)
