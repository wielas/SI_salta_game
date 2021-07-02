import pygame
from .constants import RED, GREEN, BLUE, SQUARE_SIZE, CROWN, WIDTH, HEIGHT
from salta.board import Board
from mcts_fin import MCTS
from state import State
from mcts import MonteCarloTreeSearchNode

class Game:
    def __init__(self, win):
        self._init()
        self.win = win

    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    def _init(self):
        self.compulsory_jump = False
        self.selected = None
        self.board = Board()
        self.turn = RED
        self.valid_moves = {}

    def reset(self):
        self._init()

    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)

        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            if self.compulsory_jump:
                _, valid_skip = self.board.get_valid_moves(piece)
                if valid_skip:
                    self.selected = piece
                    self.valid_moves, _ = self.board.get_valid_moves(piece)

            else:
                self.selected = piece
                self.valid_moves, valid_skip = self.board.get_valid_moves(piece)
            return True

        return False

    def _move(self, row, col):
        piece = self.board.get_piece(row, col)

        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            move=self.board.move(self.selected, row, col)
            self.change_turn()
        else:
            return False
        # mcts = MCTS(MonteCarloTreeSearchNode(State(self.board)))
        # print(mcts.run(10))
        return True

    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, BLUE, (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 15)


    def change_turn(self):
        self.valid_moves = []
        if self.turn == RED:
            self.turn = GREEN

            self.compulsory_jump = False
            self.check_for_green_skips()
        else:
            self.turn = RED

            self.compulsory_jump = False
            self.check_for_red_skips()

    def check_for_green_skips(self):
        all_pieces = self.board.get_green_pieces()

        # check if all on place
        if all(piece.on_place is True for piece in all_pieces):
            self.draw_win_statement('GREEN')

        for piece in all_pieces:
            v_moves, valid_skip = self.board.get_valid_moves(piece)

            if valid_skip:
                self.valid_moves = v_moves
                self.compulsory_jump = True
                self.selected = None

        self.update()

    def check_for_red_skips(self):
        all_pieces = self.board.get_red_pieces()
        # check if all on place
        if all(piece.on_place is True for piece in all_pieces):
            self.draw_win_statement('RED')

        for piece in all_pieces:
            v_moves, valid_skip = self.board.get_valid_moves(piece)

            if valid_skip:
                self.valid_moves = v_moves
                self.compulsory_jump = True
                self.selected = None

        self.update()

    def draw_win_statement(self, color):
        pygame.draw.circle(self.win, eval(f'{color}'), (WIDTH //2, HEIGHT//2), 80)
        self.win.blit(CROWN, (WIDTH * 0.5, HEIGHT * 0.5))
