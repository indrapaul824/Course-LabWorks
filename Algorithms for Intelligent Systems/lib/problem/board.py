# Lab8 - Coding and Implementation
# Solving N-Queen Problem using the an Informed Search Algorithm (Hill Climbing)
# Indrashis Paul
# 19MIM10046

"""
Board to save the state and positions of the Queens
"""

from collections import Counter
from random import randrange


class Board:
    """
    Board store the Queen position based on the column position in a list

    Attributes
    ----------
    __n : int, default=4
        number of queens
    __counter : int
        check conditions
    """
    def __init__(self, n=4):
        self.__n = n
        self.__counter = 3

    def generateBoard(self):
        """
        Initialize the board with random column indexes
        """
        return [randrange(self.__n) for _ in range(self.__n)]

    def calculateHeuristic(self, state: list):
        """
        Calculating the heuristics based on the row, column matches and
        diagonal matches between Queens
        """
        heuristics = 0
        a, b, c = [Counter() for _ in range(self.__counter)]

        # count the matches
        for row, col in enumerate(state):
            a[col] += 1
            b[row - col] += 1
            c[row + col] += 1

        # heuristics cal and removing extra count
        for count in [a, b, c]:
            for key in count:
                heuristics += count[key] * (count[key] - 1) / 2

        return heuristics

    def getNeighbours(self, state):
        """
        Finding neighbours and changing the state of the board
        Parameters
        ----------
        state : array type list
            board state

        Returns
        -------
        list
            list of board states after moves
        """
        neighbours = list()

        for row in range(self.__n):
            for col in range(self.__n):
                if col != state[row]:
                    # changing column for the row Queen
                    newState = list(state)
                    newState[row] = col
                    neighbours.append(list(newState))

        return neighbours

    def printBoard(self, state):
        """
        Utility to print the board
        Parameters
        ----------
        state : array like list
            board state
        """
        board = list()
        for row in range(self.__n):
            for col in range(self.__n):
                if col != state[row]:
                    board.append("-  ")
                else:
                    board.append("Q  ")
            board.append("\n")

        print(''.join(board))