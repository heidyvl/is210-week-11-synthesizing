#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Docstring"""

import time
moves =[]
class ChessPiece(object):
     position = ''
     moves = []
     prefix = ''
     tile = ''
     def __init__(self, position, moves):
          self.position = position
          self.moves = moves
          
     def algebraic_to_numeric(self,tile):
          temp = 0
          table = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
          for key, value in table.iteritems():
               if (tile[0] in table) or int(tile[1]<8):
                    temp = table[tile[0]]-1, int(tile[1])-1
               else:
                    temp = None
          return temp
          
     def is_legal_move(self, newposition):
          if self.algebraic_to_numeric(newposition) != None:
               return True
          else:
               return False

     def move(self, newposition):
          if self.is_legal_move(newposition) is True:
              #newposition = position
              moves.append((self.position, newposition, 5))
              return moves
          else:
              return False

piece = ChessPiece('a1', [])
#print piece.is_legal_move('b1')
#print piece.move('a6')

class Rook(ChessPiece):
     prefix = 'R'
     
     def is_legal_move(self, newposition):
          temp = self.algebraic_to_numeric(self.position)
          newtemp = self.algebraic_to_numeric(newposition) 
          if (temp[0] == newtemp[0] or temp[1]==newtemp[1]) and (self.algebraic_to_numeric(newposition) != None):
               return True
          else:
               return False
#rook = Rook('a1', [])
#print rook.move('h1')

class Bishop(ChessPiece):
     prefix = 'B'
     
     def is_legal_move(self, newposition):
          temp = self.algebraic_to_numeric(self.position)
          newtemp = self.algebraic_to_numeric(newposition) 
          if (int(temp[0])+ 1 == newtemp[0] and int(temp[1])+1==newtemp[1]) and (self.algebraic_to_numeric(newposition) != None):
               return True
          else:
               return False
#bishop = Bishop('a1', [])
#print bishop.is_legal_move('a1')

class King(ChessPiece):
     prefix = 'K'
     
     def is_legal_move(self, newposition):
          temp = self.algebraic_to_numeric(self.position)
          newtemp = self.algebraic_to_numeric(newposition) 
          if ((newtemp[0]==int(temp[0])+1) or (newtemp[0]==int(temp[0])-1))or ((newtemp[1]==int(temp[1])+1) or (newtemp[1]==int(temp[1])-1)) and (self.algebraic_to_numeric(self.position) != None):
               return True
          else:
               return False     
king = King('a1', [])
print king.move('b1')

class ChessMatch():
     def __init__(self, pieces):
          self.pieces = None
          
     


        
    
