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
          
     def is_legal_move(self, position):
          if self.algebraic_to_numeric(position) != None:
               return True
          else:
               return False

     def move(self, position):
          if self.is_legal_move(position) is True:
              newposition = position
              moves.append((position, newposition, 5))
              return moves
          else:
              return False

#piece = ChessPiece('a1', [])
#print piece.is_legal_move('b1')
#print piece.move('a6')

class Rook(ChessPiece):
     prefix = 'R'
     
     def is_legal_move(self, position, newposition = 'b1'):
          temp = self.algebraic_to_numeric(position)
          newtemp = self.algebraic_to_numeric(newposition) 
          if (temp[0] == newtemp[0] or temp[1]==newtemp[1]) and (self.algebraic_to_numeric(position) != None):
               return True
          else:
               return False

class Bishop(ChessPiece):
     prefix = 'B'
     
     def is_legal_move(self, position, newposition = 'c3'):
          temp = self.algebraic_to_numeric(position)
          newtemp = self.algebraic_to_numeric(newposition) 
          if (int(temp[0])+ 1 == newtemp[0] and int(temp[1])+1==newtemp[1]) and (self.algebraic_to_numeric(position) != None):
               return True
          else:
               return False
#bishop = Bishop('a1', [])
#print bishop.is_legal_move('a1')

class King(ChessPiece):
     prefix = 'K'
     
     def is_legal_move(self, position, newposition = 'b1'):
          temp = self.algebraic_to_numeric(position)
          newtemp = self.algebraic_to_numeric(newposition) 
          if ((newtemp[0]==int(temp[0])+1) or (newtemp[0]==int(temp[0])-1))or ((newtemp[1]==int(temp[1])+1) or (newtemp[1]==int(temp[1])-1)) and (self.algebraic_to_numeric(position) != None):
               return True
          else:
               return False     
king = King('a1', [])
print king.is_legal_move('a1')                                                                               


        
    
