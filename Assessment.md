Aim: The aim of this assignment is to implement (in Python) a version of the popular
Tic-Tac-Toe game. The tasks below describe some basic requirements/specs for your
program, but you have the freedom to make further decisions in terms of
functionality and implementation details.


1. Two players alternate placing Xs and Os into a grid until one player has three
matching symbols in a row, either horizontally, vertically, or diagonally. Your
program displays a three-by-three grid containing the digits 1 through 9, similar to
the display in Figure 1. The user who plays first should be able to choose the symbol
of their preference (i.e. X or O). A player can choose a valid position by typing a
number (i.e. 1 – 9 are allowed) to place a symbol in the appropriate spot. For
example, after the player chooses 3, the grid looks like the display in Figure 2. A
player should be prevented from placing a symbol where one has already been
placed. When a player has three symbols in a row, a winner is declared. If all
positions have been used and no one has three symbols in a row, a tie is declared.


2. Enhance your program implementation from Task 1 so that a single player can
play against the computer.
Hint: No need for the computer’s behavior to be sophisticated/complex. For example,
your program could generate a random number for the position where the computer
will place its symbol.


3. Getting Tasks 1 and 2 from above (almost) fully functioning will most likely mean
a PASS result for your submission. However, if you wish to try an additional
challenge or have some further practice, you can attempt this task, too.
Enhance your program implementation from Task 2 so that when the computer has
two matching symbols in any row, column, or diagonal, it selects the winning
position for its next move rather than selecting a position randomly.