from mcts import MonteCarloTreeSearchNode
class MCTS:
    def __init__(self, node: MonteCarloTreeSearchNode):
        self.root = node


    def _tree_policy(self):
        current_state = self
        while not current_state.root.is_terminal():
            if not current_state.root.is_fully_expanded():
                return current_state.root.expand()
            else:
                current_state = current_state.root.best_child()
        return current_state


    def run(self,n):
        number_of_simulations = n
        for i in range(number_of_simulations):
            v = self._tree_policy()
            reward = v.rollout()
            v.root.backpropagate(reward)
        return self.root.best_child()