# Artificial Intelligence Nanodegree

This repository contains all my solutions to the tutorials and projects of the [Udacity Artificial Intelligence Nanodegree Course](https://www.udacity.com/course/ai-artificial-intelligence-nanodegree--nd898). This course helped me refresh my knowledge of essential concepts of artificial intelligence.

## Certificate

[<img src="./AI.PNG">](https://www.udacity.com/certificate/e/3ac35480-6955-11ef-9567-a763f21fa593)

## Project 1: Sudoku Solver

Using constraint propagation to apply naked twins strategy in sudoku by extending the Sudoku-solving agent developed in the classroom lectures to solve diagonal Sudoku puzzles. A diagonal Sudoku puzzle is identical to traditional Sudoku puzzles with the added constraint that the boxes on the two main diagonals of the board must also contain the digits 1-9 in each cell.

### Resuorces:

- [Peter Norvig](https://norvig.com/sudoku.html)
- [More Peter Norvig](https://github.com/norvig/pytudes/blob/main/ipynb/Sudoku.ipynb)

## Project 2: Building a Forward-Planning Agent

Combining symbolic logic and classical search to implement an agent that performs progression search to solve planning problems. Then experimenting with different search algorithms and heuristics, and using the results to answer questions about designing planning systems.

## Project 3: Coding an Adversarial Game Playing Agent

Creating a custom advanced heuristic to experiment with adversarial search techniques by building an agent to play knights Isolation. In this version of Isolation, each agent has control over a single token that moves in L-shaped movements--like a knight in a game of chess. The agents have a fixed time limit (150 milliseconds by default) to search for the best move and respond. The search will be automatically cut off after the time limit expires, and the active agent will forfeit the game if it has not chosen a move. The new agent has been built by combining minimax search with alpha-beta pruning and iterative deepening, along with a custom heuristic.

## Project 4: Parts Of Speech (POS) Tagging

Using the Pomegranate library to build a Hidden Markov model for part of speech tagging with a universal tagset. Hidden Markov models have been able to achieve >96% tag accuracy with larger tagsets on realistic text corpora.
Hidden Markov models have been used for speech recognition and speech generation, machine translation, gene recognition for bioinformatics, and human gesture recognition for computer vision, and more.
A training accuracy of 97.53% and testing accuracy of 95.83% has been achieved in this project to correctly tag the parts of speech in the text.
