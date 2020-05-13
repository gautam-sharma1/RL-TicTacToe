"""
Made by Gautam Sharma

"""




import matplotlib.pyplot as plt
import pickle
from matplotlib import style
import time
import numpy as np
import operator
import copy

"""
#############################################################################
Main class that defines the actions and states of the game
#############################################################################
"""
HM_EPISODES = 100000
epsilon = 0.9
EPS_DECAY = 0.9998
SHOW_EVERY = 300
LEARNING_RATE = 0.1
DISCOUNT = 0.9
class Game:
    def __init__(self):
        self.game = [-1 for i in range(9)]
        self.comb = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    def state(self):
        self.rep = self.game[0],self.game[1],self.game[2],self.game[3],self.game[4],self.game[5],self.game[6],self.game[7],self.game[8]
    def action(self,player,choice):
        if choice == 0:
            self.move(player,n=0)
        elif choice == 1:
            self.move(player,n=1)
        elif choice == 2:
            self.move(player,n=2)
        elif choice == 3:
            self.move(player,n=3)
        elif choice == 4:
            self.move(player,n=4)
        elif choice == 5:
            self.move(player,n=5)
        elif choice == 6:
            self.move(player,n=6)
        elif choice == 7:
            self.move(player,n=7)
        elif choice == 8:
            self.move(player,n=8)
        pass



    def move(self,player,n):

        #self.game[n] == -1:
        self.game[n] = player
        # else:
        #     np.random.choice(self.update())

    def check(self):
        for line in self.comb:
            l = [self.game[line[0]], self.game[line[1]], self.game[line[2]]]
            if l[0] == l[1] == l[2] == 1:
                print('Game Over! AI won')
                return 1
            elif l[0] == l[1] == l[2] == 0:
                print('Game Over! Human won')
                return -1
        return False


    def reward(self):
        r = 0
        for line in self.comb:
            #print(line)
            rev = [self.game[line[0]] , self.game[line[1]] , self.game[line[2]]]
            if sum(rev) == 3:
                #print("AI won")
                return 25


        for line in self.comb:
            #print(line)
            rev = [self.game[line[0]] , self.game[line[1]] , self.game[line[2]]]
            if rev[0] == 0 and rev[1] == 0 and  rev[2] == 0:
                #print("Human Won")
                return -25

        #
        for line in self.comb:
            #print(line)
            rev = [self.game[line[0]] , self.game[line[1]] , self.game[line[2]]]
            if rev[0] == 0 and rev[1] == 0 and  rev[2] == 1:
                 r = 15
            elif rev[0] == 0 and rev[1] == 1 and  rev[2] == 0:
                r = 15
            elif rev[0] == 0 and rev[1] == 0 and  rev[2] == 1:
                r = 15
            if rev[0] == 0 and rev[1] == 1 and  rev[2] == 1:
                r -= 10
            elif rev[0] == 1 and rev[1] == 1 and  rev[2] == 0:
                r -= 10
            elif rev[0] == 0 and rev[1] == 0 and  rev[2] == 1:
                r -= 10
            else:
                continue
        if r != 0:
            return r
        else:
            return 0
    def print(self):
        for i in range(9):

            if self.game[i]==0:
                print('O ',end = " ")
            elif self.game[i]==1:
                print('X ',end = " ")
            else:
                print(-1,end = " ")
            if (i+1)%3==0:
                print('\n')
        print('---------------')


q_table={}
q_table1={}

start_q_table ="qtable-1589392282.pickle"




if start_q_table is None:
    for y1 in range(-1 ,2):
        for y2 in range(-1 ,2):
            for y3 in range(-1 ,2):
                for y4 in range(-1 ,2):
                    for y5 in range(-1 ,2):
                        for y6 in range(-1 ,2):
                            for y7 in range(-1 ,2):
                                for y8 in range(-1 ,2):
                                    for y9 in range(-1 ,2):
                                        q_table[(y1,y2,y3,y4,y5,y6,y7,y8,y9)] = [0 for i in range(9)]




else:
    with open(start_q_table, "rb") as f:
        print("-----------------Loaded q_table--------------------")
        q_table = pickle.load(f)
#print(q_table)
episode_rewards=[]

# for episodes in range(HM_EPISODES):
#     g = Game()
#     #player2 = Blob()
#
#     reward = 0
#
#     if episodes % SHOW_EVERY == 0:
#         print(f"on #{episodes}, epsilon: {epsilon}")
#         print(f"{SHOW_EVERY} ep mean {np.mean(episode_rewards[-SHOW_EVERY:])}")
#         show = True
#     else :
#         show = False
#     episode_reward = 0
#     done = [i for i in range(9)]
#     for i in range(9):
#         if i%2 == 0:
#             #print("Player is Human")
#             player = 0
#         else:
#             #print("Player is AI")
#             player = 1
#         #print(player)
#         obs = (g.game[0],g.game[1],g.game[2],g.game[3],g.game[4],g.game[5],g.game[6],g.game[7],g.game[8])
#
#         if player == 1:
#             if np.random.random() > epsilon:
#                 pos_left = {}
#                 total_pos =  q_table[obs]
#                 for i in done:
#                     pos_left[i] = total_pos[i]
#                 #print(pos_left)
#                 action = max(pos_left.items(), key=operator.itemgetter(1))[0]
#                 #print(action)
#
#                 #print("1 action done now ", done, "Removed", action)
#             else:
#                 action = np.random.choice(done)
#
#                 #print("1 action done now ", done, "Removed", action)
#
#         else:
#             action = np.random.choice(done)
#                 # print(action)
#
#         #print("Zero action done now ", done, "Removed", action)
#         g.action(player, action)
#         done.remove(action)
#         if not done :
#             """
#             Draw
#             """
#             new_q = 15
#             q_table[obs][action] = new_q
#             print("Draw")
#             break
#         # print(action)
#         # g.print()
#
#
#         # print(done)
#         #g.print()
#         #time.sleep(2)
#
#         """
#         EDIT THE SECTION BELOW
#         REWARD SECTION BEGIN
#         """
#
#         reward = g.reward()
#         rew = g.reward()
#
#         new_obs = (g.game[0],g.game[1],g.game[2],g.game[3],g.game[4],g.game[5],g.game[6],g.game[7],g.game[8])
#
#         """
#         AI
#         """
#         max_future_q = np.max(q_table[new_obs])
#         current_q = q_table[obs][action]
#
#         if rew == 25:
#             new_q = 25
#         elif rew == -25:
#             new_q = -25
#         else:
#             new_q = (1-LEARNING_RATE)*current_q + LEARNING_RATE*(reward+DISCOUNT*max_future_q)
#         q_table[obs][action] = new_q
#
#         episode_reward += reward
#         if rew == 25:
#             print('AI won')
#             break
#
#         if rew == -25:
#             print('Human Won')
#             break
#
#
#     episode_rewards.append(episode_reward)
#     epsilon *= EPS_DECAY
# moving_avg = np.convolve(episode_rewards, np.ones((SHOW_EVERY,))/SHOW_EVERY,mode="valid")
#
# with open(f"qtable-{int(time.time())}.pickle", "wb") as f:
#     pickle.dump(q_table, f,protocol=2)
# plt.figure()
# plt.plot([i for i in range(len(moving_avg))], moving_avg)
# plt.ylabel(f"reward {SHOW_EVERY}ma")
# plt.xlabel("episode #")
# plt.show()
# plt.savefig("game.png")


if __name__ == "main" :
    pass
