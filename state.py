from salta.board import Board
import numpy as np
import copy
class State:
    P1=1
    P2=-1
    def __init__(self,state,next_to_move=1,c_move=None):
        self.board=state
        self.next_to_move=next_to_move
        self.current_move=c_move
    def game_result(self):
        pieces_green = self.board.get_green_pieces()
        pieces_red = self.board.get_red_pieces()
        if all(piece.on_place is True for piece in pieces_green) and not all(
                piece1.on_place is True for piece1 in pieces_red):
            return 1
        elif all(piece.on_place is True for piece in pieces_red) and not all(
                piece1.on_place is True for piece1 in pieces_green):
            return -1
        elif all(piece.on_place is True for piece in pieces_red) and all(
                piece1.on_place is True for piece1 in pieces_green):
            return 0
    def is_game_over(self):
        pieces_green = self.board.get_green_pieces()
        piece=self.board.get_piece(0,1)
        pieces_red = self.board.get_red_pieces()

        if all(piece.on_place is True for piece in pieces_green):
            return True
        elif all(piece.on_place is True for piece in pieces_red):
            return True
        else:
            return False

    def get_legal_moves(self):
        player=self.next_to_move
        if player==1:
            pieces = self.board.get_green_pieces()
            all_moves = []
            for piece in pieces:
                moves, smthing = self.board.get_valid_moves(piece)
                moves = list(moves)
                if len(moves) > 1:
                    for i in range(len(moves)):
                        move = []
                        move.append(moves[i])
                        move.append(piece)
                        all_moves.append(move)
                else:
                    moves.append(piece)
                    all_moves.append(moves)
            filtered = filter(lambda c: len(c) == 2, all_moves)
            filtered = list(filtered)
            return filtered
        else:
            pieces = self.board.get_red_pieces()
            all_moves = []
            for piece in pieces:
                moves, smthing = self.board.get_valid_moves(piece)
                moves = list(moves)
                if len(moves) > 1:
                    for i in range(len(moves)):
                        move = []
                        move.append(moves[i])
                        move.append(piece)
                        all_moves.append(move)
                else:
                    moves.append(piece)
                    all_moves.append(moves)
            filtered = filter(lambda c: len(c) == 2, all_moves)
            filtered = list(filtered)
            return filtered

    def move(self,move):
        new_board=copy.deepcopy(self.board)
        new_board.move(move[1], move[0][0], move[0][1])
        next_to_move=State.P2 if self.next_to_move==State.P1 else State.P1
        return State(new_board,next_to_move,move)
