# In economics, a Cournot duopoly is a model of competition between two firms (Company 1 and Company 2) that produce identical products and compete in terms of quantity rather than price. Each firm determines its output quantity, and the market price is then determined by the total quantity produced by both firms.

import nashpy as nash

# Payoff matrix for Company 1 (row player)
A = [[20, 10], [15, 5]]

# Payoff matrix for Company 2 (column player)
B = [[20, 15], [10, 5]]

# Create the game
game = nash.Game(A, B)

# Find the Nash equilibrium
equilibria = game.support_enumeration()

# Print the Nash equilibria
for eq in equilibria:
    print("Nash Equilibrium:", eq)

# Get the Nash equilibrium strategies
equilibrium_strategy_company1, equilibrium_strategy_company2 = list(game.support_enumeration())[0]

# Print the equilibrium strategies
print("Company 1's Nash Equilibrium Strategy:", equilibrium_strategy_company1)
print("Company 2's Nash Equilibrium Strategy:", equilibrium_strategy_company2)

