# The Stackelberg model is a strategic interaction model in game theory where players make decisions sequentially, and one player, known as the leader, makes decisions before the other player, called the follower. The leader's actions are observed by the follower, and the follower then makes their decisions accordingly.

import nashpy as nash


A = [[(3, 2), (0, 4)], [(2, 1), (1, 3)]]
B = [[(3, 2), (0, 4)], [(2, 1), (1, 3)]]

game = nash.Game(A, B)
equilibria = game.support_enumeration()


for eq in equilibria:
    print("Nash Equilibrium:", eq)


equilibrium_strategy_player1, equilibrium_strategy_player2 = list(game.support_enumeration())[0]

print("Player 1's Nash Equilibrium Strategy:", equilibrium_strategy_player1)
print("Player 2's Nash Equilibrium Strategy:", equilibrium_strategy_player2)
