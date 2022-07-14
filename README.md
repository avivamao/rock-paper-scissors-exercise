# rock-paper-scissors-game

## Prerequisites

  + Anaconda 3.7+
  + Python 3.7+
  + Pip

## Environment Setup

You may play this game under base or virtual environment. Below is the guidacne to set up the virtual environment.
Create a new project-specific Anaconda virtual environment:

```sh
conda create -n my-game-env python=3.8 # (first time only)
```

Activate the virtual environment:

```sh
conda activate my-game-env
```

## Game Play

You will be playing the game with computer.

When you play games, you'll be asked to input from 'rock', 'paper', or 'scissors'. Your input is not case sensitive but you need to ensure the spelling is correct.

Play a game:

```sh
python game.py
```

## Demo

Here is a demostration of the game:

```
Welcome to the rock-papaer-scissors game!
Please choose from 'rock', 'paper' or 'scissors':paper
You chose: 'paper'
The computer chose:'scissors'
Sorry, the computer won..Try next time.
Thanks for playing. Please play again!
```

You will get an error message when your input is not correct. And the game will stop.

```
Welcome to the rock-papaer-scissors game!
Please choose from 'rock', 'paper' or 'scissors':rocks
Sorry, your choice is not correct. Please check the spelling and try again.
```