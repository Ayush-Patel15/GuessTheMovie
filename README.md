# GuessTheMovie

A multiplayer movie-guessing game, which extracts random movie name from the rest api and then let the players to guess it.. !


## DESCRIPTION

It uses [https://www.themoviedb.org/documentation/api](https://www.themoviedb.org/documentation/api) api to extract a random movie_name on the basis of some parameters. Parameters used are - 

- api_key : your_api_key    (Required)
- language : en-IN
- sort_by : revenue.desc    (Highest to lowest revenue)
- page : on the basis of level of difficulty

Program prompts the user for number of players (range 0-4). And initialize the player with some basic properties like name, prize_money i.e. Rs.500/- etc. And then, let the player's to guess the movie_name (Vowels will be displayed).
It will also prompt to select level of difficulty (default is 1 i.e. easy), which will increase the number of pages to search for a movie_name and make it hard to guess the movie. Movies displayed, will be well-known or highest revenue collectors of all time.

Then, the program requests the rest_api on the basis of query_parameters and select a random movie_name. It initiates an infinite while loop of guessing consonants, til the phrase is correctly guessed. Loop consist of a `spin_wheel` function similar to a probabilistic function to get a "CHANCE", "PASS" OR "PUNISHMENT" randomly. If and only, a player gets a chance - then he/she can make a guess or can even guess the whole phrase at once. Program will count for the number of times, that particular guessed letter has occured and will fill that letter at their respective places/indexes. A list consisting of guessed letters is also maintained. And the process will continue....

The project also consist of some interesting features like additional prizes, spin_wheel function to get a chance or punishment, etc. Like - 

- Additional prize bumpers like "Won a 5D-4N tour of Mumbai-Pune", "Won a brand new Pulsar 150 Bike" etc.
- Each Correct guess will add Rs.50/- to the prize_money.
- And each incorrect guess will deduct Rs.50/- from the prize_money.
- And getting punishment, after spin wheel also deducts Rs.50/-.


## INSTALLATION

- Make sure you have python(version>=2.7) installed in your system.

- Install the requirements.txt file.

```bash
pip install -r requirements.txt
```

- Register on the api website and get an api_key. Place it in `get_movie.py` file - under the key "api_key".

- Now, You are ready to play. Run the `main.py` file from `src` to play.

```bash
python ..\GuessTheMovie\src\main.py
```

- Enter Name, select Level of difficulty and continue to play.


## IMAGES

<br>
<img src="images\game_start.png">
<br>
<img src="images\game_play.png">
<br>
<img src="images\game_win.png">

<br>
A python OOP'S based fun game to test your skills or the movie base.