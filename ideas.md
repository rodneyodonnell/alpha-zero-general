Consider https://github.com/hhatto/autopep8

Write simple tree search approach without nnet?
 - How much benefit does nnet give?
 - Benefit likely depends on branching factor of game? Or total decision in game?

Submit code to github. Update README.md once latest iter done.

Drop first round of train data as it will mostly be learning garbage and polluting later iterations?

Try different lookahead?
 - 25 is default ... will very rarely move far enough ahead to find a win?
 - is 50/100/500 any better? Will we get better quality training data faster?
 - Accept if wins / draws > x, ignoring draws?



## Debug, what is mstc doing?
https://www.digitalocean.com/community/tutorials/how-to-use-the-python-debugger
ipython3 -m pdb main-connect4.py



Arena is slow for comparing models when numMCTSSims is high ... we should run model update tests with a lower value (using numMCTSSims=1 may be the right number to compare models with no lookahead)


We're generating heaps of new training samples for each game (#moves * #reflections) ... I though we were supposed to generate a single move per game? Should actually read the papers.


TODO: Reread papers. Ping original author for ideas?


Why are old checkpoints getting deleted? Hard to compare vs old model.
Is null checkpoint saved anywhere?

Writ out arena stats separately for going first vs second.





---------------

# done.
predict() returns uniform distribution to start ... nnet not randomized?
make canonical string more efficient ... using it as a dict key everywhere!
canonical string for player2 board has lots of -0 in it...

# Skip. Cache hit rate too low, mcts reused in arena too so this doesn't help there.
We should cache NNet calls, we're recalculating the same thing for every new MSTC (each new game sim)
 - Some caching, but not incredible. For a 'numMCTSSims': 100, 'numEps': 50 -> 18% hit rate.  (hit:15043, miss:68257, rate:18.06%)
