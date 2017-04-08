# Peg Solitaire Solver

Solver in python for peg solitaire on triangle board. Brute force method witout optimalization.

![Peg solitaire board](https://github.com/marcinklimek/peg_solitaire/blob/master/img/peg_solitaire.jpg?raw=true)

## Why?

A few days ago, my daughter tried to solve this puzzle. To impress her :) I needed to find the solution. A Billion tries later I've found one. But this led me to solve all possible starting points. We can group starting positions to 4 cases. I've known 3 of 4 after a while, but one was hard to find. The one in the middle on index __04__. That's why I wrote this solver. It took me 3h late night, so the code is a bit ugly. But it works :) 

## More info - links

- [many usefull info](https://en.wikipedia.org/wiki/Peg_solitaire)
- [wiki about solitaire](http://www.gibell.net/pegsolitaire/tindex.html)

## TODO 

-  map with steps, to improve searching for solution, if there is already solved sequence stop, and point to proper moves
- generic map


## What's in the code

How it's indexed:

```
      00
    01  02
   03 04 05
 06 07 08 09
10 11 12 13 14
```

List of the possible move directions in the triangle:

```
(0,1,3,6,10), 
(0,2,5,9,14), 
(1,4,8,13), 
(3,7,12), 
(2,4,7,11), 
(5,8,12), 
(3,4,5), 
(6,7,8,9), 
(10,11,12,13,14)
```

Based on this list we can prepare all possible moves pairs (from, to) based on rules.
Then in every iteration we need to find all possible moves, and make it. It's brute force method, so if there is more then one move we will check every path. Every iteration generates new Stage object with it's own board and history of the moves which led to this board state.