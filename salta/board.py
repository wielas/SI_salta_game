import pygame
from .constants import BLACK, RED, GREEN, WHITE, BRONZE, DBRONZE, SQUARE_SIZE, ROWS, COLS
from .piece import Piece


class Board:
    def __init__(self):
        self.board = []
        self.create_board()

        self.red_left = self.white_left = 15  # not necessary

    def draw_squares(self, win):
        win.fill(DBRONZE)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(win, BRONZE, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)

        # TODO: make on_place val == True (II 20:00)

    def get_piece(self, row, col):
        return self.board[row][col]

    def get_green_pieces(self):
        piece_list = []
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.board[row][col] != 0 and self.board[row][col].color == GREEN:
                    piece_list.append(self.board[row][col])
        return piece_list

    def get_red_pieces(self):
        piece_list = []
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.board[row][col] != 0 and self.board[row][col].color == RED:
                    piece_list.append(self.board[row][col])
        return piece_list

    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row, col, GREEN))
                    elif row > 6:
                        self.board[row].append(Piece(row, col, RED))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    def draw(self, win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)

    def get_valid_moves(self, piece):
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row

        # making moves bb
        # vars in [{movelist}, {skipped boolean}] format
        left_up = self._traverse_left(row - 1, max(row - 3, -1), -1, piece.color, left)
        right_up = self._traverse_right(row - 1, max(row - 3, -1), -1, piece.color, right)

        left_down = self._traverse_left(row + 1, min(row + 3, ROWS), 1, piece.color, left)
        right_down = self._traverse_right(row + 1, min(row + 3, ROWS), 1, piece.color, right)

        movelist = [left_up, right_up, left_down, right_down]
        boollist = [x[1] for x in movelist]

        # update move list /w compulsory jumps
        valid_skip = False

        if True not in boollist:
            moves.update(left_up[0])
            moves.update(right_up[0])
            moves.update(left_down[0])
            moves.update(right_down[0])
        else:
            for move in movelist:
                if move[1] is True:
                    moves.update(move[0])
                    if move[0]:
                        valid_skip = True
            if not valid_skip:
                for move in movelist:
                    moves.update(move[0])

        return moves, valid_skip

    def _traverse_left(self, start, stop, step, color, left, skipped=[]):
        moves = {}
        last = {}
        skippando = False
        for r in range(start, stop, step):
            if left < 0:
                break

            current = self.board[r][left]
            if current == 0:  # if square is empty
                if skipped and not last:  # skipped over something, next move w/o possibility to jump again
                    break
                elif skipped:
                    moves[(r, left)] = last + skipped

                else:
                    moves.clear()
                    moves[(r, left)] = last

                break

            elif current.color == color:  # if allied color piece is on square
                break
            else:  # if another color is on square
                last = [current]  # loop again
                skippando = True

            left -= 1

        return moves, skippando

    def _traverse_right(self, start, stop, step, color, right, skipped=[]):
        moves = {}
        last = {}
        skippando = False
        for r in range(start, stop, step):
            if right >= COLS:
                break

            current = self.board[r][right]
            if current == 0:  # if square is empty
                if skipped and not last:  # skipped over something, next move w/o possibility to jump again
                    break
                elif skipped:
                    moves[(r, right)] = last + skipped
                else:
                    moves[(r, right)] = last

                break

            elif current.color == color:  # if allied color piece is on square
                break
            else:  # if another color is on square
                last = [current]  # loop again
                skippando = True

            right += 1

        return [moves, skippando]
