# In the prisoners' dilemma, two suspects are arrested, and the prosecution lacks sufficient evidence to convict them on the principal charge. However, they can each be convicted on a lesser charge, leading to a dilemma about whether to cooperate with each other or betray their partner.

import nashpy as nash

# Payoff matrix for Player 1 (row player)
A = [[3, 0], [5, 1]]

# Payoff matrix for Player 2 (column player)
B = [[3, 5], [0, 1]]

# Create the game
game = nash.Game(A, B)

# Find the Nash equilibrium
equilibria = game.support_enumeration()

# Print the Nash equilibria
for eq in equilibria:
    print("Nash Equilibrium:", eq)

# Get the Nash equilibrium strategies
equilibrium_strategy_player1, equilibrium_strategy_player2 = list(game.support_enumeration())[0]


print("Player 1's Nash Equilibrium Strategy:", equilibrium_strategy_player1)
print("Player 2's Nash Equilibrium Strategy:", equilibrium_strategy_player2)


