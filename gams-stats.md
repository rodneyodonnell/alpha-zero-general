
After checkpoint0 (arena 1):
self.Ps[s]: [0.11543559 0.12438519 0.22961421 0.14087985 0.10423645 0.13692304? 0.14852576]
s: '.......\n.......\n.......\n.......\n.......\n.......'
counts: [7, 6, 60, 7, 5, 7, 7]



MSTC tree recycled in the Arena, so counts are preserved!
Game 20 will be played at a higher standard than game 0.
... Does this mean that we swap players half way through the Arena?
... DOes preserving counts make sense? Probably doesn't matter in c4 as state determines current plaer.
[0.11543559 0.12438519 0.22961421 0.14087985 0.10423645 0.13692304? 0.14852576]
counts: [7, 6, 60, 7, 5, 7, 7]
counts: [26, 9, 118, 13, 8, 11, 14]
counts: [34, 18, 1259, 28, 15, 21, 24]   ## count after 14(?) iters, MCTS expansions from empty board.


TODO: SHould print out win counts before/after player swap.


For each self-play we start from scratc.
For each arena-compare we use existing MCTS.


;; -- iter 1 --
NEW/PREV WINS : 26 / 12 ; DRAWS : 2


;; -- iter 2 --
; self play
s: '.......\n.......\n.......\n.......\n.......\n.......'
self.Ps[s]: [0.11543559 0.12438519 0.22961421 0.14087985 0.10423645 0.13692304? 0.14852576]
counts: [9.0, 9.0, 23.0, 23.0, 8.0, 11.0, 16.0]


;; -- iter 3 --
; self play
self.Ps[s]: [0.15114938 0.12735166 0.19330119 0.17204084 0.09323579 0.10905858? 0.15386261]
counts: [14, 12, 23, 16, 9, 10, 15]     ;; pit 1
counts: [96, 63, 189, 89, 57, 119, 86]  ;; pit 7


;; -- iter 4 --
self.Ps[s]: [0.10452504 0.10126945 0.18862683 0.18847114 0.10720821 0.14385669? 0.1660426 ]
[5, 5, 33, 36, 5, 7, 8]

;; -- iter 5 --
self.Ps[s]: [0.09761921 0.10434748 0.21721822 0.1456127  0.14320204 0.14327195? 0.14872849]
counts: [4, 4, 167, 6, 6, 6, 6]

;; -- iter 7 --
self.Ps[s]: [0.12386388 0.12706228 0.18303615 0.1522573  0.10623192 0.16113697? 0.14641157]
