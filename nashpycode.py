# solving Nash equilibria for two-player games : simple rock-paper-scissors game

import nashpy as nash
import numpy as np

A = np.array([[0, -1, 1], [1, 0, -1], [-1, 1, 0]])
B = - A

rps = nash.Game(A, B)
print(rps)

equilibria = rps.support_enumeration()

for eq in equilibria:
    print("Nash Equilibrium:", eq) 

eq_strategy_player1, eq_strategy_player2 = list(rps.support_enumeration())[0]

print ("eq_strategy_player1:", eq_strategy_player1)
print ("eq_strategy_player2:", eq_strategy_player2)
