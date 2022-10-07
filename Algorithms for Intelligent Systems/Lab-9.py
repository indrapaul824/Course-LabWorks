#!/usr/bin/env python

# -------------------------------------------------------------------------------------
# Created By:  Indrashis Paul - 19MIM10046

# Name:        Lab-9.py / Tic-Tac-Toe
# Purpose:     Implementation of Min-Max and Alpha-Beta pruning algorithms through 
#              the Tic-Tac-Toe game. Runs a game of Tic-Tac-Toe between two players - 
#              the user and the computer. The computer uses the Min-Max/Alpha-Beta 
#              Pruning Algorithm to determine the best move.
# Input:	   User input for the position of the next move(X,Y) and the algorithm
# Output:	   Prints the following:
#              1. The board after each move
#              2. The evaluation time for each move
#              3. The next recommended move for the User
#              4. The winner of the game
# -------------------------------------------------------------------------------------

import time

class Game:
    def __init__(self):
        self.initialize_game()
    
    def initialize_game(self):
        self.current_state = [['.','.','.'],
                              ['.','.','.'],
                              ['.','.','.']]
        # Player X always plays first
        self.player_turn = 'X'
    
    def draw_board(self):
        for i in range(0,3):
            for j in range(0,3):
                print('{}|'.format(self.current_state[i][j]), end = ' ')
            print()
        print()
    
    # Determine if the made move is valid
    def is_valid(self, px, py):
        if px < 0 or px > 2 or py < 0 or py > 2:
            return False
        elif self.current_state[px][py] != '.':
            return False
        else:
            return True
    
    
    # Check if the game has ended and return the winner in each case
    def is_end(self):
        # Horizontal win check
        for i in range(0,3):
            if (self.current_state[i][0] == self.current_state[i][1] and
                self.current_state[i][1] == self.current_state[i][2] and
                self.current_state[i][0] != '.'):
                return self.current_state[i][0]
        
        # Vertical win check
        for i in range(0,3):
            if (self.current_state[0][i] == self.current_state[1][i] and
                self.current_state[1][i] == self.current_state[2][i] and
                self.current_state[0][i] != '.'):
                return self.current_state[0][i]
        
        # Main diagonal win check
        if (self.current_state[0][0] == self.current_state[1][1] and
            self.current_state[1][1] == self.current_state[2][2] and
            self.current_state[0][0] != '.'):
            return self.current_state[0][0]
        
        # Secondary diagonal win check
        if (self.current_state[0][2] == self.current_state[1][1] and
            self.current_state[1][1] == self.current_state[2][0] and
            self.current_state[0][2] != '.'):
            return self.current_state[0][2]
        
        # Check if there are any moves left
        for i in range(0,3):
            for j in range(0,3):
                # There is a move left on the board
                if (self.current_state[i][j] == '.'):
                    return None
        
        # It's a tie!
        return '.'
    
    # Player with 'O' is the MAX, in this case the computer / the algorithm
    def max(self):
        # Possible values for maxv are:
        # -1 - loss
        # 0  - a tie
        # 1  - win

        # We're initially setting it to -2 as worse than the worst case:
        maxv = -2
        
        px = None
        py = None
        
        result = self.is_end()
        
        # If the game came to an end, the function needs to return
        # the evaluation function of the end. That can be:
        # -1 - loss
        # 0  - a tie
        # 1  - win
        
        if result == 'X':
            return (-1, 0, 0)
        elif result == 'O':
            return (1, 0, 0)
        elif result == '.':
            return (0, 0, 0)
        
        for i in range(0,3):
            for j in range(0,3):
                if self.current_state[i][j] == '.':
                    self.current_state[i][j] = 'O'
                    (m, min_i, in_j) = self.min()
                    if m > maxv:
                        maxv = m
                        px = i
                        py = j
                    self.current_state[i][j] = '.'
        return (maxv, px, py)
    
    # Player with 'X' is the MIN, in this case the human / the user
    def min(self):
        # Possible values for minv are:
        # -1 - win
        # 0  - a tie
        # 1  - loss

        # We're initially setting it to 2 as worse than the worst case:
        minv = 2
        
        qx = None
        qy = None
        
        result = self.is_end()
        
        # If the game came to an end, the function needs to return
        # the evaluation function of the end. That can be:
        # -1 - win
        # 0  - a tie
        # 1  - loss
        
        if result == 'X':
            return (-1, 0, 0)
        elif result == 'O':
            return (1, 0, 0)
        elif result == '.':
            return (0, 0, 0)
        
        for i in range(0,3):
            for j in range(0,3):
                if self.current_state[i][j] == '.':
                    self.current_state[i][j] = 'X'
                    (m, max_i, max_j) = self.max()
                    if m < minv:
                        minv = m
                        qx = i
                        qy = j
                    self.current_state[i][j] = '.'
        return (minv, qx, qy)
    
    def play(self):
        while True:
            self.draw_board()
            self.result = self.is_end()
            
            # Printing the appropriate message if the game has ended
            if self.result != None:
                if self.result == 'X':
                    print('X wins')
                elif self.result == 'O':
                    print('O wins')
                elif self.result == '.':
                    print('It\'s a tie')
                
                self.initialize_game()
                return
            
            # If it's player's turn
            if self.player_turn == 'X':
                while True:
                    start = time.time()
                    (m, qx, qy) = self.min()
                    end = time.time()
                    print(f'Evaluation time: {end - start} seconds')
                    print('Recommended move: X = %d, Y = %d' % (qx, qy))
                    
                    px = int(input('Insert the X coordinate: '))
                    py = int(input('Insert the Y coordinate: '))
                    
                    (qx, qy) = (px, py)
                    
                    if self.is_valid(px, py):
                        self.current_state[px][py] = 'X'
                        self.player_turn = 'O'
                        break
                    else:
                        print('Invalid move')
            # If it's computer's turn
            else:
                (m, px, py) = self.max()
                self.current_state[px][py] = 'O'
                self.player_turn = 'X'
    
    def max_alpha_beta(self, alpha, beta):
        maxv = -2
        
        px = None
        py = None
        
        result = self.is_end()
        
        if result == 'X':
            return (-1, 0, 0)
        elif result == 'O':
            return (1, 0, 0)
        elif result == '.':
            return (0, 0, 0)
        
        for i in range(0,3):
            for j in range(0,3):
                if self.current_state[i][j] == '.':
                    self.current_state[i][j] = 'O'
                    (m, min_i, in_j) = self.min_alpha_beta(alpha, beta)
                    if m > maxv:
                        maxv = m
                        px = i
                        py = j
                    self.current_state[i][j] = '.'
                    
                    
                    if maxv >= beta:
                        return (maxv, px, py)
                    if maxv > alpha:
                        alpha = maxv
        return (maxv, px, py)
    
    def min_alpha_beta(self, alpha, beta):
        minv = 2
        
        qx = None
        qy = None
        
        result = self.is_end()
        
        if result == 'X':
            return (-1, 0, 0)
        elif result == 'O':
            return (1, 0, 0)
        elif result == '.':
            return (0, 0, 0)
        
        for i in range(0,3):
            for j in range(0,3):
                if self.current_state[i][j] == '.':
                    self.current_state[i][j] = 'X'
                    (m, max_i, max_j) = self.max_alpha_beta(alpha, beta)
                    if m < minv:
                        minv = m
                        qx = i
                        qy = j
                    self.current_state[i][j] = '.'
                    
                    if minv <= alpha:
                        return (minv, qx, qy)
                    if minv < beta:
                        beta = minv
        return (minv, qx, qy)
    
    def play_alpha_beta(self):
        while True:
            self.draw_board()
            self.result = self.is_end()
            
            if self.result != None:
                if self.result == 'X':
                    print('X wins')
                elif self.result == 'O':
                    print('O wins')
                elif self.result == '.':
                    print('It\'s a tie')
                
                self.initialize_game()
                return
            
            if self.player_turn == 'X':
                while True:
                    start = time.time()
                    (m, qx, qy) = self.min_alpha_beta(-2, 2)
                    end = time.time()
                    print(f'Evaluation time: {end - start} seconds')
                    print('Recommended move: X = %d, Y = %d' % (qx, qy))
                    
                    px = int(input('Insert the X coordinate: '))
                    py = int(input('Insert the Y coordinate: '))
                    
                    (qx, qy) = (px, py)
                    
                    if self.is_valid(px, py):
                        self.current_state[px][py] = 'X'
                        self.player_turn = 'O'
                        break
                    else:
                        print('Invalid move')
            else:
                (m, px, py) = self.max_alpha_beta(-2, 2)
                self.current_state[px][py] = 'O'
                self.player_turn = 'X'

def main():
    g = Game()
    print("** Game created **\n")
    n = int(input("Enter your choice(1 or 2): \n1. Min-Max,\n2. Alpha-Beta \n:"))
    if n == 1:
        g.play()
    elif n == 2:
        g.play_alpha_beta()
    else:
        print("Please enter a valid choice!")
        main()

if __name__ == "__main__":
    main()
