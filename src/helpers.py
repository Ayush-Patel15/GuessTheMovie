from get_movie import get_movie_name

VOWELS = ["A","E","I","O","U"]
INTEGERS = [0,1,2,3,4,5,6,7,8,9]
SYMBOLS = ["-","!","$","&",",",".","'",":","?"]

def movie_name_with_vowels():
    movie = get_movie_name()
    movie_name = ""
    for char in movie:
        if (char in VOWELS) or (char in str(INTEGERS)) or (char in SYMBOLS):
            movie_name = movie_name + char + "  "
        else:
            movie_name = movie_name + "_" + "  "
    print(movie)
    return movie_name

if __name__ == "__main__":
    # "movie" should be in upper case letters.
    print(movie_name_with_vowels())