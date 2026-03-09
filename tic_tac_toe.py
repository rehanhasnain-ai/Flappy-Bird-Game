#!/usr/bin/env python3
"""
Terminal Tic-Tac-Toe game.
Supports two-player local and single-player vs CPU (minimax).
"""

import random

WIN_COMBINATIONS = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
]


def print_board(board):
    symbols = [c if c is not None else " " for c in board]
    print()
    print(f" {symbols[0]} | {symbols[1]} | {symbols[2]} ")
    print("---+---+---")
    print(f" {symbols[3]} | {symbols[4]} | {symbols[5]} ")
    print("---+---+---")
    print(f" {symbols[6]} | {symbols[7]} | {symbols[8]} ")
    print()


def check_winner(board):
    for a, b, c in WIN_COMBINATIONS:
        if board[a] and board[a] == board[b] == board[c]:
            return board[a]
    if all(cell is not None for cell in board):
        return "Tie"
    return None


def available_moves(board):
    return [i for i, v in enumerate(board) if v is None]


def minimax(board, ai_symbol, human_symbol, maximizing):
    winner = check_winner(board)
    if winner == ai_symbol:
        return 1, None
    if winner == human_symbol:
        return -1, None
    if winner == "Tie":
        return 0, None

    if maximizing:
        best_score = -float("inf")
        best_move = None
        for move in available_moves(board):
            board[move] = ai_symbol
            score, _ = minimax(board, ai_symbol, human_symbol, False)
            board[move] = None
            if score > best_score:
                best_score = score
                best_move = move
        return best_score, best_move
    else:
        best_score = float("inf")
        best_move = None
        for move in available_moves(board):
            board[move] = human_symbol
            score, _ = minimax(board, ai_symbol, human_symbol, True)
            board[move] = None
            if score < best_score:
                best_score = score
                best_move = move
        return best_score, best_move


def cpu_move(board, ai_symbol, human_symbol):
    # If board empty, pick center or corner for variety
    if len(available_moves(board)) == 9:
        return random.choice([0, 2, 4, 6, 8])
    _, move = minimax(board, ai_symbol, human_symbol, True)
    return move


def player_move(board, symbol):
    moves = available_moves(board)
    while True:
        try:
            choice = input(f"Enter position (1-9) for {symbol}: ").strip()
            pos = int(choice) - 1
            if pos in moves:
                return pos
            print("Invalid move. Position taken or out of range.")
        except ValueError:
            print("Please enter a number between 1 and 9.")


def play_game(single_player=False):
    board = [None] * 9
    current = "X"
    if single_player:
        human_symbol = "X"
        while True:
            choice = input("Play as X or O? (X goes first) [X/O]: ").strip().upper()
            if choice in ("X", "O"):
                human_symbol = choice
                break
            print("Please enter X or O.")
        ai_symbol = "O" if human_symbol == "X" else "X"
    else:
        human_symbol = None
        ai_symbol = None

    print("Positions are numbered 1-9 as:")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")

    while True:
        print_board(board)
        winner = check_winner(board)
        if winner:
            if winner == "Tie":
                print("It's a tie!")
            else:
                print(f"{winner} wins!")
            break

        if single_player and current == ai_symbol:
            print("CPU is making a move...")
            move = cpu_move(board, ai_symbol, human_symbol)
        else:
            move = player_move(board, current)

        board[move] = current
        current = "O" if current == "X" else "X"


def main():
    print("Tic-Tac-Toe")
    print("1) Two players")
    print("2) Single player vs CPU")
    choice = input("Select mode [1/2]: ").strip()
    if choice == "2":
        play_game(single_player=True)
    else:
        play_game(single_player=False)


if __name__ == "__main__":
    main()
