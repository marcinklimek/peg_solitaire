"""
      00
    01  02
   03 04 05
 06 07 08 09
10 11 12 13 14

"""
board_size = 15

#all possible move directions in triangle
lines = [ (0,1,3,6,10), (0,2,5,9,14), (1,4,8,13), (3,7,12), (2,4,7,11), (5,8,12), (3,4,5), (6,7,8,9), (10,11,12,13,14) ]

#generate possible move pairs
moves = {}
for i in range( board_size ):
    moves[i] = []

for l in lines:
    for i in range( max(len(l)-2, 1)):
        moves[ l[i] ].append( l[ i+2 ]  )
        moves[ l[i+2] ].append( l[ i ]  )




class Stage:

    def __init__(self, s=None, mv=None):

        self.history = []
        self.board = [1] * board_size

        if s != None:

            self.copy_board(s)

            for h in s.history:
                self.history.append(h)

            self.history.append(mv)

    def draw_board(self):

        b = self.board
        print "    {0}".format(b[0])
        print "   {0} {1}".format(b[1], b[2])
        print "  {0} {1} {2}".format(b[3], b[4], b[5])
        print " {0} {1} {2} {3}".format(b[6], b[7], b[8], b[9])
        print "{0} {1} {2} {3} {4}".format(b[10], b[11], b[12], b[13], b[14])


    def get_i(self, i):
        return self.board[i]

    def set_i(self, i, s):
        self.board[i] = s

    def get_middle(self, m, i):

        for l in lines:
            if (m in l) and (i in l):

                i_start = l.index(m)
                i_end = l.index(i)

                #example, move from left to right
                # _oo__  --> ___o_
                # oo___  --> __o__
                # oooo_  --> oo__o

                #find middle peg
                if i_start < i_end:
                    middle = l[ i_start + 1 ]
                else:
                    middle = l[ i_end + 1 ]

                return middle

        return None        

    def find_moves(self):

        possible_m = []

        for i in range(board_size):

            #search for empty hole
            if self.get_i(i) == 0:
             
                #check possible moves into this free hole   
                for m in moves[i]:
                    if self.get_i(m) == 1: 

                        middle = self.get_middle(m, i)

                        #if there is a peg in the hole, we can make a move
                        if middle is not None and self.get_i(middle) == 1:
                            possible_m.append( (m, middle, i) )

        return possible_m

    def copy_board(self, b):

        for i in range(board_size):
            self.set_i(i, b.get_i(i))

    def make_move(self, m):

        s = Stage(self, m)

        s.set_i(m[0], 0)
        s.set_i(m[1], 0)
        s.set_i(m[2], 1)

        return s

    def count(self):

        c = 0
        for i in range(board_size):
            c += self.get_i(i)

        return c

def test():
    s = Stage()
    s.draw_board()
    s.set_i(0, 0)
    s.draw_board()

    ss= Stage()
    ss.copy_board(s)
    ss.draw_board()
    print s.find_moves()

    b = Stage()
    b.board = [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1]
    print b.find_moves()

#test()

def run(s, mv=None):

    solutions_counter = 0
    if mv is not None:

        s = s.make_move(mv)

        if s.count() == 1:
            solutions_counter += 1
            for x in s.history:
                print "({}, {})".format( x[0], x[2] ),

            print ""
            return solutions_counter

    fm = s.find_moves()

    for m in fm:
        solutions_counter += run(s, m)

    return solutions_counter

"""
      00
    01  02
   03 04 05
 06 07 08 09
10 11 12 13 14
"""

s = Stage()
s.set_i(0, 0)
s.set_i(1, 0)
s.set_i(2, 0)
s.set_i(3, 0)
s.set_i(4, 0)
s.set_i(7, 0)
s.set_i(12, 0)
s.draw_board()

solutions_counter = run(s)

print "Total solutions:", solutions_counter

#poz 5
# (14, 5) (12, 14) (4, 13) (3, 8) (10, 3) (1, 6) (14, 12) (11, 4) (2, 7) (7, 9) (6, 13) (12, 14) (15, 13)

#poz 4
# (11, 4) (2, 7) (6, 4) (7, 2) (13, 11) (1, 4) (4, 13) (14, 12) (15, 6) (3, 10) (11, 13) (13, 6) (6, 15)