from Coach import Coach
from connect4.Connect4Game import Connect4Game
from connect4.tensorflow.NNet import NNetWrapper as nn
from utils import dotdict
from os.path import isfile

args = dotdict({
    'numIters': 100,
    'numEps': 100,
    # 'tempThreshold': 15,
    'tempThreshold': 999999,   # Not sure why we have this? Seems like it would generally make things worse.
    'updateThreshold': 0.6,
    'maxlenOfQueue': 200000,
    # 'numMCTSSims': 350,  # ~7^3, roughly 3 ply lookahead. ... how many iterations until a win/loss?
    # 'numMCTSSims': 800,   # 800 MctS sims used in paper (Silver 2017a)
    'numMCTSSims': 100,
    # 'numMCTSSims': 10,
    # 'numMCTSSims': 25,
    'arenaCompare': 2,
    'cpuct': 1,

    # 'checkpoint': './checkpoint/',
    # 'load_model': False,
    # 'load_folder_file': ('/dev/models/8x100x50', 'best.pth.tar'),
    'load_model': True,
    # 'load_folder_file': ('checkpoint/eps-100_mstc-100', 'checkpoint_3.pth.tar'),
    'numItersForTrainExamplesHistory': 20,
    'start_iter': 1,
})

args.checkpoint = "checkpoint/eps-%d_mstc-%d" % (args.numEps, args.numMCTSSims)
if args.load_model:
    for i in range(args.numIters, 0, -1):
        if isfile('%s/checkpoint_%s.pth.tar.index' % (args.checkpoint, i)):
            args.load_folder_file = (args.checkpoint, 'checkpoint_%s.pth.tar' % i)
            args.start_iter = i
            break
    else:
        print('No previous model found, setting load_model=False')
        args.load_model = False

## Rerun from scratch.
# args.load_model = False

if __name__ == "__main__":
    g = Connect4Game()
    # g = Connect4Game(height=5, width=5, win_length=3)
    nnet = nn(g)

    if args.load_model:
        nnet.load_checkpoint(args.load_folder_file[0], args.load_folder_file[1])

    c = Coach(g, nnet, args)
    if args.load_model:
        print("Load trainExamples from file")
        c.loadTrainExamples()
    c.learn()
