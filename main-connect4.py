from Coach import Coach
from connect4.Connect4Game import Connect4Game
from connect4.tensorflow.NNet import NNetWrapper as nn
from utils import dotdict

args = dotdict({
    'numIters': 10,
    'numEps': 10,
    'tempThreshold': 15,
    'updateThreshold': 0.6,
    'maxlenOfQueue': 200000,
    'numMCTSSims': 49 * 7,
    'arenaCompare': 20,
    'cpuct': 1,

    'checkpoint': './temp/',
    'load_model': True,
    'load_folder_file': ('models/connect4','best.pth.tar'),
    'numItersForTrainExamplesHistory': 20,

})

if __name__=="__main__":
    g = Connect4Game()
    nnet = nn(g)

    if args.load_model:
        nnet.load_checkpoint(args.load_folder_file[0], args.load_folder_file[1])

    c = Coach(g, nnet, args)
    if args.load_model:
        print("Load trainExamples from file")
        c.loadTrainExamples()
    c.learn()
