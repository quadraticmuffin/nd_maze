import numpy as np


class NdMaze():
    '''

    '''
    def __init__(self, nd, size, start=None):
        self.board = np.zeros(shape=[size]*nd)
        self.nd = nd
        self.size = size
        self.pos = start
        if start is None:
            self.pos = [0]*nd
        self.dimr = 0
        self.dimc = 1
    
    def move(self, dim, amt):
        if (self.pos[dim] + amt) not in range(self.size):
            raise ValueError('Attempted to move out of bounds')
        temp_pos = list(self.pos)
        temp_pos[dim] += amt
        self.pos = tuple(temp_pos)
        return self.get2d()

    def seeDim(self, newdim):
        if newdim not in range(self.nd):
            raise ValueError(f'Dimension {newdim} does not exist in board of {self.nd} dimensions.')
        self.dimr = self.dimc
        self.dimc = newdim
        return self.get2d()

    def get2d(self):
        idx = list(self.pos)
        idx[self.dimr] = slice(None)
        idx[self.dimc] = slice(None)
        ret = self.board[tuple(idx)]
        if self.dimr > self.dimc:
            return ret.T
        else:
            return ret
    
    def __repr__(self):
        return str(self.board)
    
    def __str__(self):
        return str(self.get2d())


if __name__ == '__main__':
    game = NdMaze(5, 2)
    game.board = np.arange(32).reshape([2]*5)