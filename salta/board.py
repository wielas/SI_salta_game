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
        # TODO: make jumps single and compulsory
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row

        #if piece.color == RED:
        moves.update(self._traverse_left(row - 1, max(row - 3, -1), -1, piece.color, left))
        moves.update(self._traverse_right(row - 1, max(row - 3, -1), -1, piece.color, right))

        #if piece.color == GREEN:
        moves.update(self._traverse_left(row + 1, min(row + 3, ROWS), 1, piece.color, left))
        moves.update(self._traverse_right(row + 1, min(row + 3, ROWS), 1, piece.color, right))

        return moves

    def _traverse_left(self, start, stop, step, color, left, skipped=[]):
        moves = {}
        last = {}
        for r in range(start, stop, step):
            if left < 0:
                break

            current = self.board[r][left]
            if current == 0:  # if square is empty
                if skipped and not last:  # skipped over something, next move w/o possibility to jump again
                    print('if')
                    break
                elif skipped:
                    moves.clear()
                    moves[(r, left)] = last + skipped
                    print('elif')
                    return moves
                    # TODO returning of this point only
                else:
                    moves.clear()
                    moves[(r, left)] = last
                    print('else')

                # if last:  # check if can jump anymore from blank space after doing a move
                #     if step == -1:
                #         row = max(r-3, 0)
                #     else:
                #         row = min(r+3, ROWS)
                #
                #     moves.update(self._traverse_left(r+step, row, step, color, left-1, skipped=last))  # multi-jump
                #     moves.update(self._traverse_right(r+step, row, step, color, left+1, skipped=last))  # multi-jump
                break

            elif current.color == color:  # if allied color piece is on square
                break
            else:  # if another color is on square
                print('last current')
                last = [current]  # loop again

            left -= 1

        return moves

    def _traverse_right(self, start, stop, step, color, right, skipped=[]):
        moves = {}
        last = {}
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

                # if last:  # check if can jump anymore from blank space after doing a move
                #     if step == -1:
                #         row = max(r - 3, 0)
                #     else:
                #         row = min(r + 3, ROWS)
                #
                #     moves.update(self._traverse_left(r + step, row, step, color, right - 1, skipped=last))  # multi-jump
                #     moves.update(self._traverse_right(r + step, row, step, color, right + 1, skipped=last))  # multi-jump
                break

            elif current.color == color:  # if allied color piece is on square
                break
            else:  # if another color is on square
                last = [current]  # loop again

            right += 1

        return moves
