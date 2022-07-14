# rock-paper-scissors-exercise

## Prerequisites

  + Anaconda 3.7+
  + Python 3.7+
  + Pip

## Repo Setup

Go to [GitHub online] (https://github.com/) to create a new remote project repository called "rock-paper-scissors-exercise". Adding  "README.md" file and a Python-flavored ".gitignore" file for th new repo. After this process is complete, you should be able to view the repo on GitHub at an address like https://github.com/YOUR_USERNAME/rock-paper-scissors-exercise.

After creating the remote repo, use GitHub Desktop software or the command-line to download or "clone" it onto your computer. Choose a familiar download location like the Desktop.

After cloning the repo, navigate there from the command-line:

```sh
cd ~/download location/ock-paper-scissors-exercise
```

Use your text editor or the command-line to create a file in that repo called "game.py", and then place the following contents inside:

```sh
# this is the "game.py" file...

print("Rock, Paper, Scissors, Shoot!")
```

## Environment Setup

Create a new project-specific Anaconda virtual environment:

```sh
conda create -n my-game-env python=3.8 # (first time only)
```

Activate the virtual environment:

```sh
conda activate my-game-env
```

Test the virtual environment by running the Python script from the command-line:

```sh
python game.py
```

## Player Types

When you play games, you'll be able to select any of the following combinations of players:

player type(s) | description
--- | ---
`HUMAN` | A human player who will input their selections.
`COMPUTER-EASY` or `RANDOM` | A computer player which makes random selections. Easy to beat.
`COMPUTER-HARD` or `MINIMAX` | A computer player which thinks ahead to make optimal selections. Uses the "minimax" algorithm to simulate moves and evaluate all possible game states. Impossible to beat.
`MINIMAX-AB` | A much faster version of the hard computer player. Uses "alpha-beta" pruning to skip evaluations of unnecessary game states.

## Usage

### Game Play

Play a game:

```sh
python -m app.game
```


### Game Simulation

Play many games (computer vs computer), saves results to CSV file in "data" directory. Optionally pass the game count and/or player strategies as environment variables:

```sh
python -m app.jobs.play_games

# alternatively:
GAME_COUNT=3 python -m app.jobs.play_games

# alternatively:
X_STRATEGY="COMPUTER-HARD" O_STRATEGY="COMPUTER-EASY" GAME_COUNT=100 python -m app.jobs.play_games
```


## Testing

Run automated tests, to know whether the app is working as expected:

```sh
pytest
```


## Demo