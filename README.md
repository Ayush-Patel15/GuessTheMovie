# GuessTheMovie

A multiplayer movie-guessing game, which extracts random movie name from the rest api and then let the players to guess it.. !


## DESCRIPTION

It uses `https://www.themoviedb.org/documentation/api` the api to extract a random movie_name on the basis of some parameters. Parameters used are - 

- language : en-IN
- sort_by : popularity.desc
- primary_release_year: 2020
- page : on the basis of level of difficulty

Asks the user for number of players (range 0-4). And initialize the player with some basic properties like name, prize_money etc. And then, let the player's to guess the movie_name. (Vowels will be displayed)
It will also ask for the level of difficulty (default is) that will increase the number of searches and make it hard to guess the movie.
The project also consist some interesting features like additional prizes, spin_wheel function to get a chance or punishment, etc.

- Each Correct guess will add Rs.50/- to the prize_money.
- And each incorrect guess will deduct Rs.50/- from the prize_money.


## INSTALLATION

- Make sure you have python(version>=2.7) installed in your system.

- Install the requirements.txt file.

```bash
pip install -r requirements.txt
```

- You are ready to play. Run the `main.py` file from `src` to play.

```bash
python ..\GuessTheMovie\src\main.py
```

- Enter Name,Level of difficulty and continue to play.


## IMAGES

<br>
<img src="images\game_start.png">
<br>
<img src="images\game_play.png">
<br>
<img src="images\game_win.png">

<br>
A python OOP'S based fun game to test your skills or the movie base.