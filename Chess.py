#  File: Chess.py

#  Description: This program will use backtracking to find all of the soliutions for an n size chess board.

#  Student's Name: Johnny Tran

#  Student's UT EID: jht825

#  Partner's Name: Crystal Le

#  Partner's UT EID: cl44964

#  Course Name: CS 313E

#  Unique Number: 51120

#  Date Created: 3/14/2022

#  Date Last Modified:

import sys

# Keeps track of how many times a solution is made.
COUNT = 0


class Queens(object):
    def __init__(self, n=8):
        self.board = []
        self.n = n
        for i in range(self.n):
            row = []
            for j in range(self.n):
                row.append('*')
            self.board.append(row)

    # print the board
    def print_board(self):
        for i in range(self.n):
            for j in range(self.n):
                print(self.board[i][j], end=' ')
            print()
        print()

    # check if a position on the board is valid
    def is_valid(self, row, col):
        for i in range(self.n):
            if (self.board[row][i] == 'Q') or (self.board[i][col] == 'Q'):
                return False
        for i in range(self.n):
            for j in range(self.n):
                row_diff = abs(row - i)
                col_diff = abs(col - j)
                if (row_diff == col_diff) and (self.board[i][j] == 'Q'):
                    return False
        return True

    # do the recursive backtracking
    def recursive_solve(self, col):
        global COUNT
        if col == self.n:
            COUNT += 1
        else:
            for i in range(self.n):
                if self.is_valid(i, col):
                    self.board[i][col] = 'Q'
                    if self.recursive_solve(col + 1):
                        return True
                    self.board[i][col] = '*'
            return False

    # wrapper function for the recursive_solve 
    def solve(self):
        self.recursive_solve(0)
        print(COUNT)


def main():
    # read the size of the board
    line = sys.stdin.readline()
    line = line.strip()
    n = int(line)

    # create a chess board
    game = Queens(n)

    # place the queens on the board and count the solutions

    # print the number of solutions
    game.solve()


if __name__ == "__main__":
    main()
