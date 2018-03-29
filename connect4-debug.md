;; This buffer is for text that is not saved, and for Lisp evaluation.
;; To create a file, visit it with C-x C-f and enter text in its buffer.

canonicalBoard: [[-0. -0. -0. -0. -0. -0. -0.]? [-0. -0. -0. -0. -0. -0. -0.]? [-0. -0. -
          uses temp=0.                                                                                               0. -1. -0. -0. -0.]? [-0. -0. -0.  1. -0. -0. -0.]? [-0. -1. -0. -1. -0. -1. -1.]? [-0.
                                                                                                                       1.  1.  1. -0. -1.  1.]]
          Returns:                                                                                                 episodeStep: 12
              trainExamples: a list of examples of the form (canonicalBoard,pi,v)                                  p: list
                             pi is the MCTS informed policy vector, v is +1 if
                             the player eventually won the game, else -1.
                                                                                                                r: 0



pi with guaranteed win on next move after 25 mstc steps. (21% of time we take win)
pi: [0.14285714285714285, 0.17857142857142858, 0.14285714285714285, 0.14285714285714285, 0.21428571428571427, 0.07142857142857142, 0.10714285714285714]



With 350 mstc - sampled first 'win state' with base of 3 actions  [-1. -0. -0. -1. -0.  1. -0.]
Sensible values for 'pi', hitting two potential win squares immediately at ~30% each, and others at ~6%
[0.06633906633906633, 0.2972972972972973, 0.36363636363636365, 0.0687960687960688, 0.06633906633906633, 0.0687960687960688, 0.0687960687960688]

Blocks a 1-move loss 95% of the time.


self.game.stringRepresentation(board)



P[] = [0, 0, 0, 1, 0, 0, 0] ... why? Bad valud out of nnet? Haven't really been looking a P's ...
Happening because temp=0 ... why is temp 0?

   temp = int(episodeStep < self.args.tempThreshold)
   Once we get to step15 (15 pieces played?) we start emitting the exact choice made.
Before this we recorde a full distribution as the training sample, and select from that distribution.
Returning max value seems to throw away info the nnet should be learning??
Choosing the max value seems to be removing eploration from our training corpus??

.......
.....O.
.....X.
...?.O.
.O.X.OX
XOXXOOX
