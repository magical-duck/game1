#!/usr/bin/env python3
"""
Simple Tic-Tac-Toe playable in terminal.
"""
import sys

def print_board(b):
    for i in range(3):
        row = ' | '.join(b[i*3:(i+1)*3])
        print(' ' + row)
        if i < 2:
            print('---+---+---')

def check_winner(b):
    lines = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    for a,bidx,c in lines:
        if b[a] == b[bidx] == b[c] and b[a] != ' ':
            return b[a]
    if ' ' not in b:
        return 'Draw'
    return None

def valid_move(b, pos):
    return 0 <= pos < 9 and b[pos] == ' '

def main():
    board = [' '] * 9
    player = 'X'
    print("Tic-Tac-Toe\nPositions are 1-9 starting top-left to bottom-right.")
    while True:
        print('\nCurrent board:')
        print_board(board)
        move = input(f"Player {player}, enter position (1-9) or 'q' to quit: ").strip()
        if move.lower() in ('q','quit','exit'):
            print('Goodbye')
            sys.exit(0)
        if not move.isdigit():
            print('Invalid input, enter a number 1-9.')
            continue
        pos = int(move) - 1
        if not valid_move(board, pos):
            print('Invalid move, try again.')
            continue
        board[pos] = player
        winner = check_winner(board)
        if winner:
            print_board(board)
            if winner == 'Draw':
                print("It's a draw!")
            else:
                print(f'Player {winner} wins!')
            break
        player = 'O' if player == 'X' else 'X'

if __name__ == '__main__':
    main()
