from copy import copy
import random
import sys
import logging

FAULT_PROB = 0.

class Matrix:
    def __init__(self, nrows, ncols, fill_random=False):
        self._mat = []
        self._nrows = nrows
        self._ncols = ncols
        for r in range(nrows):
            self._mat.append([None]*ncols)

        if fill_random:
            logging.info(f'Initializing {nrows}x{ncols} matrix with random values')
            for i in range(nrows):
                for j in range(ncols):
                    self._mat[i][j] = random.random()

    def __mul__(self, other):
        if self._ncols != other._nrows:
            raise ValueError('Incompatible matrices, cols {self._ncols} and rows {other._nrows} must be the same!')
        left_rows = self._nrows
        left_cols = self._ncols
        right_rows = other._nrows
        right_cols = other._ncols
        logging.info(f'Multiplying {left_rows}x{left_cols} with {right_rows}x{right_cols}')
        inject_fault = random.choices(
            [True, False], [FAULT_PROB, 1-FAULT_PROB])[0]
        if inject_fault:
            logging.debug('Will be injecting fault in this run')
            faulty_row = random.randint(0, left_rows+1)
            faulty_col = random.randint(0, right_cols+1)
        prod = Matrix(left_rows, right_cols)
        for i in range(left_rows):
            if i % 10 == 0:
                logging.debug(f'Calculating row {i}')
            for j in range(right_cols):
                if inject_fault and i == faulty_row and j == faulty_col:
                    raise RuntimeError('KABOOM!')
                rvals = self.row(i)
                lvals = other.col(j)
                p = 0
                for n in range(left_cols):
                    p += rvals[n]*lvals[n]
                prod[i,j] = p
        return prod

    def row(self, i):
        return copy(self._mat[i])

    def col(self, j):
        vals = [None] * self._nrows
        for i in range(self._nrows):
            vals[i] = self._mat[i][j]
        return vals

    def __setitem__(self, key, val):
        i, j = key
        if 0 <= i < self._nrows and 0 <= j < self._ncols:
            self._mat[i][j] = float(val)
        else:
            raise IndexError(f'Invalid index [{i},{j}]')

    def __getitem__(self, key):
        i, j = key
        if 0 <= i < self._nrows and 0 <= j < self._ncols:
            return self._mat[i][j]
        else:
            raise IndexError(f'Invalid index [{i},{j}]')

    def __str__(self):
        ret = ''
        for r in range(self._nrows):
            for c in range(self._ncols):
                ret += str(self._mat[r][c]) + ' '
            ret += '\n'
        return ret


def test():
    x = Matrix(3, 3)
    y = Matrix(3, 3)
    i = 1
    for r in range(3):
        for c in range(3):
            x[r,c] = i
            y[r,c] = i/2
            i += 1
    print(x)
    print(y)
    z = x * y
    print(z)

    a = Matrix(3, 3, fill_random=True)
    print(a)


def main():
    logging.basicConfig(level=logging.DEBUG)
    size = int(sys.argv[1])
    fault_prob = float(sys.argv[2])
    global FAULT_PROB
    FAULT_PROB = fault_prob

    x = Matrix(size, size, fill_random=True)
    y = Matrix(size, size, fill_random=True)
    z = x * y
    # print(z)

if __name__ == '__main__':
    main()
