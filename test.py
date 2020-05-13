from TicTacToe import logic

import pickle
import numpy as np

print("Hello")


start_q_table ="qtable-1589392282.pickle"

with open(start_q_table, "rb") as f:
    print("-----------------Loaded q_table--------------------")
    q_table = pickle.load(f)

win = 0
loss = 0
draw = 0
for i in range(100):
    g = logic.Game()
    done = [i for i in range(9)]
    g.print()
    action = np.random.choice(done)
    g.move(0,action)
    done.remove(action)
    g.print()
    print("AI's move")
    state = (g.game[0],g.game[1],g.game[2],g.game[3],g.game[4],g.game[5],g.game[6],g.game[7],g.game[8])
    action = (np.argmax(q_table[state]))
    g.move(1,action)
    done.remove(action)
    g.print()

