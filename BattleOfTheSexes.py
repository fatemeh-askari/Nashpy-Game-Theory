# The setup typically involves two players, often representing a couple, who must decide where to go or what to do for the evening. The players have two options, and they have preferences for each option. The challenge is to coordinate their choices to maximize their joint satisfaction.
# example:
# Player 1 has two options: "Cinema" and "Staying at Home" with corresponding payoffs of (3, 0) and (0, 2).
# Player 2 also has two options: "Cinema" and "Staying at Home" with corresponding payoffs of (2, 0) and (0, 3).


import nashpy as nash

# Payoff matrix for Player 1 (row player)
A = [[3, 0], [0, 2]]

# Payoff matrix for Player 2 (column player)
B = [[2, 0], [0, 3]]

# Create the game
game = nash.Game(A, B)

# Find the Nash equilibrium
equilibria = game.support_enumeration()

# Print the Nash equilibria
for eq in equilibria:
    print("Nash Equilibrium:", eq)


print("First Nash equ")

# Get the Nash equilibrium strategies
equilibrium_strategy_player1, equilibrium_strategy_player2 = list(game.support_enumeration())[0]

# Print the equilibrium strategies
print("Player 1's Nash Equilibrium Strategy:", equilibrium_strategy_player1)
print("Player 2's Nash Equilibrium Strategy:", equilibrium_strategy_player2)


print("Second Nash equ")

equilibrium_strategy_player1, equilibrium_strategy_player2 = list(game.support_enumeration())[1]
print("Player 1's Nash Equilibrium Strategy:", equilibrium_strategy_player1)
print("Player 2's Nash Equilibrium Strategy:", equilibrium_strategy_player2)
