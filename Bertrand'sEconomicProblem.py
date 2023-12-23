# Bertrand's economic problem in game theory is a model of price competition among firms that produce identical products and set prices simultaneously. In the Bertrand competition model, firms compete by choosing a price for their product, and consumers purchase from the firm with the lowest price.

import nashpy as nash


A = [[4, 3], [5, 1]]
B = [[4, 5], [3, 1]]

game = nash.Game(A, B)
equilibria = game.support_enumeration()
for eq in equilibria:
    print("Nash Equilibrium:", eq)

print('first nash eq bertrand')
equilibrium_strategy_firm1, equilibrium_strategy_firm2 = list(game.support_enumeration())[0]

print("Firm 1's Nash Equilibrium Strategy:", equilibrium_strategy_firm1)
print("Firm 2's Nash Equilibrium Strategy:", equilibrium_strategy_firm2)

print('second nash eq bertrand')
equilibrium_strategy_firm1, equilibrium_strategy_firm2 = list(game.support_enumeration())[1]

print("Firm 1's Nash Equilibrium Strategy:", equilibrium_strategy_firm1)
print("Firm 2's Nash Equilibrium Strategy:", equilibrium_strategy_firm2)