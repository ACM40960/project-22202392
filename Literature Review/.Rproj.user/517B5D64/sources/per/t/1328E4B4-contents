<p align="center"><img width=60.5% src="https://github.com/ACM40960/project-22202392/blob/main/assets/RCD005NEW_03.png?raw=true"></p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
![Python](https://img.shields.io/badge/python-v3.6+-blue.svg)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

# AI plays checkers


## Overview

This project contains how to create an AI bot for playing checkers against it. The bot game strategy is based on the minimax algorithm.
A brief introduction to the minimax algorithm theory can be found in the [Minimax](https://info.sydcon.com/blog/a-brief-introduction-to-game-theory-the-minimax-algorithm) web. The code is in this [Repository](https://github.com/ACM40960/project-22202392/tree/main) and the presentation is in this pdf file [Presentation](AI plays checkers - presentation.pdf) .


## Getting Started

This project is written using Python 3.9.16. The modules are installed in an environment using Anaconda.

The modules used in this project are:

- `pygame`
- `deepcopy`

It is necessary to install these modules before executing the code.


## Project documents

The main parts of the project are divided in two folders ([Checkers](https://github.com/ACM40960/project-22202392/tree/main/Checkers) and [minimax](https://github.com/ACM40960/project-22202392/tree/main/minimax)).

#### Checkers  

- [Constants](https://github.com/ACM40960/project-22202392/blob/main/Checkers/constants.py) file: It is where the constants used in the project are saved. 
- [Board](https://github.com/ACM40960/project-22202392/blob/main/Checkers/board.py) file: It is where the board attributes, structure and drawn are created.
- [Piece](https://github.com/ACM40960/project-22202392/blob/main/Checkers/piece.py) file: It is where the pieces attributes, structure and drawn are created.
- [Game](https://github.com/ACM40960/project-22202392/blob/main/Checkers/game.py) file: It is where the game dynamics and functions are created.

#### Minimax

[Algorithm](https://github.com/ACM40960/project-22202392/blob/main/minimax/algorithm.py) file: It is where the algorithm minimax is created.


## How to run the game

By default, running `main.py` will run a multiplayer checkers game, where white pieces are the AI bot and red's are the manual player.


#### Minimax function

The complexity of the minimax algorithm is determined by the depth. The depth is the number of turns the algorithm simulated in advance before making a movement, it can be modified changing the parameter `depth` in the function:

`minimax(position, depth, max_player, game, alpha , beta)`

The function has the following parameters:

- `position`: pieces position in the board. 
- `depth`: number of movements simulated.
- `max_player`: player which maximize the evaluation function in the algorithm.
- `game`: Game class.
- `alpha`: alpha parameter of alpha-beta pruning.
- `beta`: beta parameter of alpha-beta pruning.

### Game example

Recorded game between two AI bots:

![](https://github.com/ACM40960/project-22202392/blob/main/assets/game.gif?raw=true)


### Acknowledgements

Board class for checkers game and base version of the minmax algorithm is adapted from the project of [TechWithTim](https://github.com/techwithtim/Python-Checkers-AI).


### Contact

Jesús Pardo - jesus.pardoalvarez@ucdconnect.ie








