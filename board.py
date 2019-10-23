# -*- coding: utf-8 -*-
"""
Spyder Editor

Dies ist eine temporäre Skriptdatei.
"""

import numpy as np

class Board(object):
    
    def __init__(self, n=7, player_symbol='x', beginner='bot'):
        """ 
        Constructor that should init a connect four board by making
        a 7x7 matrix, and initializing all entries as zero.
        the default symbol of the player is X, and the default
        beginner of the game is the bot.
        
        """
        self.board = None
        self.reset_board(n)
        self.stale = False
        
        #Init the board
        
        self.symbol_o = {
            'mark': 'O',
            'value': 1
        }
        
        self.symbol_x = {
            'mark': 'X'
            'value': 2
        }
        
        self.symbol_empty = {
            'mark': ' '
            'value': 0
        }
        
        self.player_symbol, self.bot_symbol = (self.symbol_x, self.symbol_o) \ 
                                              if player_symbol.lower() == 'x' \
                                              else (self.symbol_o, self.symbol_x)
        
        self.winner = None

    def reset_board(n): 
        #initializes a nxn-matrix with all zero entries
        self.board = np.zeros((n, n)).astype(int)
        self.winner = None
    
    def check_winner()
        
    def check_stale() :
        
    def draw_board():
        """
        draw some user friendly version of board
        
        """
        print(board)
        
    def have_same_value(self, item_x, item_y, item_int, axis):
        """
        should check the amount of same symbols around the last input. only
        horizontal and vertical
        params:
            > axis : gives info about the direction which is supposed to be checked
            > item_x and item_y give information about position of the last input
        return an integer I guess
        """
        
        
        
        
        
    def have_same_value_diag(self, item_x, item_y, item_int, degree):
        """
        diagonal version of upper function
        """
        
    def make_move_bot(row)

    def make_move_player(row)     
        
    

        
        