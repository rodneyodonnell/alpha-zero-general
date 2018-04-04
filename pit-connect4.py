import Arena
from MCTS import MCTS
from connect4.Connect4Game import Connect4Game, display
from connect4.Connect4Players import *
from connect4.tensorflow.NNet import NNetWrapper as NNet

import numpy as np
from utils import dotdict

"""
use this script to play any two agents against each other, or play manually with
any agent.
"""

# g = Connect4Game(height=5, width=5, win_length=3)
g = Connect4Game()

# all players
rp = RandomPlayer(g).play
# gp = GreedyConnect4Player(g).play
hp = HumanConnect4Player(g).play
lp = OneStepLookaheadConnect4Player(g, verbose=False).play


# nnet players
# n1 = NNet(g)
# n1.load_checkpoint('./pretrained_models/connect4/tensorflow/', 'best.pth.tar')
# n1.load_checkpoint('./temp/', 'best.pth.tar')
# n1.load_checkpoint('./temp/', 'best.pth.tar')
# args1 = dotdict({'numMCTSSims': 50, 'cpuct': 1.0})  # 9/10/1 vs lp (iter 6 model), 4/5/1 vs lp (iter 4 model)
# args1 = dotdict({'numMCTSSims': 10, 'cpuct': 1.0})   # 5/15/0 vs lp
# args1 = dotdict({'numMCTSSims': 500, 'cpuct': 1.0})   # 14/5/1 vs lp (90 minutes!)
# mcts1 = MCTS(g, n1, args1)
# n1p = lambda x: np.argmax(mcts1.getActionProb(x, temp=0))


def nn_checkpoint_player(checkpoint, numMCTSSims=20, train_eps=10, train_mcts=10):
    nn = NNet(g)
    nn.load_checkpoint('./checkpoint/eps-%s_mcts-%s/' % (train_eps, train_mcts), 'checkpoint_%s.pth.tar' % checkpoint)
    mcts = MCTS(g, nn, dotdict({'numMCTSSims': numMCTSSims, 'cpuct': 1.0}))
    return lambda x: np.argmax(mcts.getActionProb(x, temp=0))

#n2 = NNet(g)
#n2.load_checkpoint('/dev/8x50x25/','best.pth.tar')
#args2 = dotdict({'numMCTSSims': 25, 'cpuct':1.0})
#mcts2 = MCTS(g, n2, args2)
#n2p = lambda x: np.argmax(mcts2.getActionProb(x, temp=0))

# arena = Arena.Arena(rp, rp, g, display=display)  # (490, 507, 3), Half time, swap ends. Score = 257/242/1.  Small alvantage to player1 for random?
# arena = Arena.Arena(n1p, hp, g, display=display)
# arena = Arena.Arena(rp, lp2, g, display=display)
# arena = Arena.Arena(lp1, rp, g, display=display)
# arena = Arena.Arena(lp, hp, g, display=display)
# arena = Arena.Arena(n1p, lp, g, display=display)
# print(arena.playGames(2, verbose=True))
# arena = Arena.Arena(nn_checkpoint_player(2, numMCTSSims=2), nn_checkpoint_player(6, numMCTSSims=2), g, display=display)  # 11/9/0
# arena = Arena.Arena(rp, nn_checkpoint_player(6, numMCTSSims=2), g, display=display)        # 2/18/0 to MSTC
# arena = Arena.Arena(rp, nn_checkpoint_player(2, numMCTSSims=2), g, display=display)        # 2/18/0 to MSTC
# arena = Arena.Arena(lp, nn_checkpoint_player(2, numMCTSSims=2), g, display=display)        # 18/2/0 to LP
# arena = Arena.Arena(lp, nn_checkpoint_player(6, numMCTSSims=2), g, display=display)        # 18/2/0 to LP
# arena = Arena.Arena(lp, nn_checkpoint_player(6, numMCTSSims=50), g, display=display)       # 9/6/5 to LP

# arena = Arena.Arena(rp, nn_checkpoint_player(3, numMCTSSims=10), g, display=display)         # 0/10/0 to nn3
# arena = Arena.Arena(rp, nn_checkpoint_player(3, numMCTSSims=2), g, display=display)         # 1/9/0 to nn3
# arena = Arena.Arena(nn_checkpoint_player(2, numMCTSSims=10), nn_checkpoint_player(3, numMCTSSims=10), g, display=display)         # (7,3,0), checkpoint2 > checkpoint3.
# arena = Arena.Arena(nn_checkpoint_player(1, numMCTSSims=2), nn_checkpoint_player(2, numMCTSSims=2), g, display=display)
# arena = Arena.Arena(nn_checkpoint_player(1, numMCTSSims=2), nn_checkpoint_player(7, numMCTSSims=2, train_eps=100, train_mcts=100), g, display=display)  # (8, 12, 0)
# arena = Arena.Arena(nn_checkpoint_player(1, numMCTSSims=50), nn_checkpoint_player(7, numMCTSSims=50, train_eps=100, train_mcts=100), g, display=display)  # full=(6, 8, 6), half=3/1/6
# arena = Arena.Arena(rp, nn_checkpoint_player(7, numMCTSSims=2, train_eps=100, train_mcts=100), g, display=display)  # (2, 18, 0)
# arena = Arena.Arena(rp, nn_checkpoint_player(8, numMCTSSims=2, train_eps=100, train_mcts=100), g, display=display)  # (6, 14, 0)
# arena = Arena.Arena(nn_checkpoint_player(1, numMCTSSims=50), nn_checkpoint_player(10, numMCTSSims=50, train_eps=100, train_mcts=100), g, display=display)  # (9, 8, 3)
# arena = Arena.Arena(nn_checkpoint_player(1, numMCTSSims=50), nn_checkpoint_player(12, numMCTSSims=50, train_eps=100, train_mcts=100), g, display=display)  # (9, 9, 2)
# arena = Arena.Arena(nn_checkpoint_player(1, numMCTSSims=50), nn_checkpoint_player(17, numMCTSSims=50, train_eps=100, train_mcts=100), g, display=display)  #
# arena = Arena.Arena(rp, nn_checkpoint_player(1, numMCTSSims=2), g, display=display)  # (3, 17, 0)

## With bugfix, maybe it works now?
# arena = Arena.Arena(nn_checkpoint_player(1, numMCTSSims=20, train_eps=20, train_mcts=20), nn_checkpoint_player(2, numMCTSSims=20, train_eps=20, train_mcts=20), g, display=display)  # (6, 11, 3)
# arena = Arena.Arena(nn_checkpoint_player(1, numMCTSSims=20, train_eps=20, train_mcts=20), nn_checkpoint_player(3, numMCTSSims=20, train_eps=20, train_mcts=20), g, display=display)  # (7, 12, 1)

## train -> eps=100, mcts=200
# arena = Arena.Arena(nn_checkpoint_player(1, numMCTSSims=20, train_eps=20, train_mcts=20), nn_checkpoint_player(3, numMCTSSims=20, train_eps=100, train_mcts=200), g, display=display)  # (2, 18, 0)
# arena = Arena.Arena(nn_checkpoint_player(1, numMCTSSims=20, train_eps=20, train_mcts=20), nn_checkpoint_player(4, numMCTSSims=20, train_eps=100, train_mcts=200), g, display=display)  # (5, 14, 1)
# arena = Arena.Arena(nn_checkpoint_player(1, numMCTSSims=20, train_eps=20, train_mcts=20), nn_checkpoint_player(6, numMCTSSims=20, train_eps=100, train_mcts=200), g, display=display)  # (6, 14, 0)
# arena = Arena.Arena(nn_checkpoint_player(1, numMCTSSims=20, train_eps=20, train_mcts=20), nn_checkpoint_player(8, numMCTSSims=20, train_eps=100, train_mcts=200), g, display=display)  # (4, 16, 0)


# print(arena.playGames(20, verbose=False))

# arena = Arena.Arena(hp, nn_checkpoint_player(8, numMCTSSims=20, train_eps=100, train_mcts=200), g, display=display)  # Human wins 2-0
arena = Arena.Arena(hp, nn_checkpoint_player(8, numMCTSSims=800, train_eps=100, train_mcts=200), g, display=display)  # Human wins 2-0
print(arena.playGames(2, verbose=True))
