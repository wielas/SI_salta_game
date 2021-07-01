import numpy as np
from collections import defaultdict
from salta.board import Board
from state import GameState

class MonteCarloTreeSearchNode():
    def __init__(self, state: GameState, parent=None):
        self.state = state
        self.results = defaultdict(int)
        self._number_of_visits = 0
        self.child = []
        self.parent = parent

    @property
    def q(self):
        w = self.results[self.parent.state.next_to_move]
        l = self.results[-1*self.parent.state.next_to_move]
        return w - l
    @property
    def untried_actions(self):
        if not hasattr(self,'_untried_actions'):
            self._untried_actions=self.state.get_legal_actions()
        return self._untried_actions
    @property
    def n(self):
        return self._number_of_visits

    def is_terminal(self):
        return self.state.is_game_over()

    def expand(self):
        move = self._untried_actions.pop()
        next_state=self.state.move(move)
        child = MonteCarloTreeSearchNode(next_state,  parent=self)
        self.child.append(child)
        return child

    def rollout(self):
        current_state = self.state
        while not current_state.is_game_over():
            possible_moves = current_state.get_legal_actions()
            move = self.rollout_policy(possible_moves)
            current_state = current_state.move(move)
            print(move)


        return current_state.game_result()

    def rollout_policy(self, possible_moves):
        return possible_moves[np.random.randint(len(possible_moves))]

    def backpropagate(self, res):
        self._number_of_visits += 1
        self.results[res] += 1
        if self.parent:
            self.parent.backpropagate(res)

    def is_fully_expanded(self):
        return len(self.untried_actions) == 0

    def best_child(self, c_param=np.sqrt(2)):
        choices_weights = [
            (c.q() / float(c.n)) + c_param * np.sqrt((2 * float(np.log(self.n)) / float(c.n)))
            for c in self.child]
        return self.child[np.argmax(choices_weights)]

    # def get_legal_moves(self):
    #
    #     pieces = self.state.get_green_pieces()
    #     all_moves = []
    #     for piece in pieces:
    #         moves, smthing = self.state.get_valid_moves(piece)
    #         moves = list(moves)
    #         if len(moves) > 1:
    #             for i in range(len(moves)):
    #                 move = []
    #                 move.append(moves[i])
    #                 move.append(piece)
    #                 all_moves.append(move)
    #         else:
    #             moves.append(piece)
    #             all_moves.append(moves)
    #     filtered = filter(lambda c: len(c) == 2, all_moves)
    #     filtered = list(filtered)
    #     return filtered
    #
    #
    #
    #
    #
    # def is_game_over(self):
    #     pieces_green = self.state.get_green_pieces()
    #     pieces_red = self.state.get_red_pieces()
    #     if all(piece.on_place is True for piece in pieces_green):
    #         return True
    #     elif all(piece.on_place is True for piece in pieces_red):
    #         return True
    #     else:
    #         return False


    # def game_result(self):
    #     pieces_green = self.state.get_green_pieces()
    #     pieces_red = self.state.get_red_pieces()
    #     if all(piece.on_place is True for piece in pieces_green) and not all(
    #             piece1.on_place is True for piece1 in pieces_red):
    #         return 1
    #     elif all(piece.on_place is True for piece in pieces_red) and not all(
    #             piece1.on_place is True for piece1 in pieces_green):
    #         return -1
    #     elif all(piece.on_place is True for piece in pieces_red) and all(
    #             piece1.on_place is True for piece1 in pieces_green):
    #         return 0

# def do_move(self,move):
#
#
#     self.state=self.state.move(move[1],move[0][0], move[0][1])
#
#     return self
