# VOWELS = ["A","E","I","O","U"]
ALPHABETS = "BCDFGHJKLMNPQRSTVWXYZ"
VOWELS = "AEIOU"
INTEGERS = "0123456789"
SYMBOLS = ["-","!","$","&",",",".","'",":","?"," "]

def movie_name_guessing(movie, guessed=[]):
    movie_name = ""
    for char in movie:
        if (char in VOWELS) or (char in INTEGERS) or (char in SYMBOLS) or (char in guessed):
            movie_name = movie_name + char + "  "
        else:
            movie_name = movie_name + "_" + "  "
    # print(movie)
    return movie_name

if __name__ == "__main__":
    # "movie" should be in upper case letters.
    # print(movie_name_guessing(get_movie_name()))
    print(movie_name_guessing("BLACK PANTHER-2",["B","N","R"]))
