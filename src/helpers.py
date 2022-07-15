# VOWELS = ["A","E","I","O","U"]
ALPHABETS = "BCDFGHJKLMNPQRSTVWXYZ"
VOWELS = "AEIOU"
INTEGERS = "0123456789"
SYMBOLS = ["-","!","$","&",",",".","'",":","?"]

def movie_name_with_vowels(movie):
    movie_name = ""
    for char in movie:
        if (char in VOWELS) or (char in INTEGERS) or (char in SYMBOLS):
            movie_name = movie_name + char + "  "
        else:
            movie_name = movie_name + "_" + "  "
    # print(movie)
    return movie_name

if __name__ == "__main__":
    # "movie" should be in upper case letters.
    # print(movie_name_with_vowels(get_movie_name()))
    print(movie_name_with_vowels("BLACK PANTHER - 2"))
