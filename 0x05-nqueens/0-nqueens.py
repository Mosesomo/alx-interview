#!/usr/bin/python3
'''N Queens'''
import sys


def is_safe(board, row, col, N):
    '''checks whether it's safe to place a queen
        at a given position on the board
    '''
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens(board, col, N, solutions):
    '''recursively tries to place queens on the board'''
    if col >= N:
        solution = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return True

    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1

            solve_n_queens(board, col + 1, N, solutions)

            board[i][col] = 0

    return False


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    N = int(sys.argv[1])

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []

    solve_n_queens(board, 0, N, solutions)

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
