import math
import random

def minimax(board, depth, is_maximizing):
    if check_win(board, 'X'):
        return -10 + depth, None
    elif check_win(board, 'O'):
        return 10 - depth, None
    elif check_tie(board):
        return 0, None

    if is_maximizing:
        best_score = -math.inf
        best_move = None
        for move in get_available_moves(board):
            board[move] = 'O'
            score, _ = minimax(board, depth + 1, False)
            board[move] = '-'
            if score > best_score:
                best_score = score
                best_move = move
        return best_score, best_move
    else:
        best_score = math.inf
        best_move = None
        for move in get_available_moves(board):
            board[move] = 'X'
            score, _ = minimax(board, depth + 1, True)
            board[move] = '-'
            if score < best_score:
                best_score = score
                best_move = move
        return best_score, best_move

def check_win(board, player):
    win_states = [
        [board[0], board[1], board[2]],
        [board[3], board[4], board[5]],
        [board[6], board[7], board[8]],
        [board[0], board[3], board[6]],
        [board[1], board[4], board[7]],
        [board[2], board[5], board[8]],
        [board[0], board[4], board[8]],
        [board[2], board[4], board[6]]
    ]
    for state in win_states:
        if state == [player, player, player]:
            return True
    return False

def check_tie(board):
    return '-' not in board

def get_available_moves(board):
    return [i for i in range(len(board)) if board[i] == '-']

def print_board(board):
    for i in range(0, 9, 3):
        print(board[i:i+3])

board = ['-'] * 9
print_board(board)

ai_moves = 0  # keep track of number of moves by AI
while True:
    if random.choice([True, False]):
        _, move = minimax(board, 0, True)
        board[move] = 'O'
        ai_moves += 1
    else:
        move = random.choice(get_available_moves(board))
        board[move] = 'O'
        ai_moves += 1
    print_board(board)
    if check_win(board, 'O'):
        print('AI wins after', ai_moves, 'level!')
        break
    elif check_tie(board):
        print('Tie after!', ai_moves, 'levels!')
        break

    move = int(input('Enter move: '))
    board[move] = 'X'
    print_board(board)
    if check_win(board, 'X'):
        print('You winb after', ai_moves, 'levels!')
        break
    elif check_tie(board):
        print('Tie!')
        break