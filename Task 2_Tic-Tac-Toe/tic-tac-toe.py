import math

# ─────────────────────────────────────────────
#  Tic-Tac-Toe AI — CodSoft AI Internship
#  Task 2: Tic-Tac-Toe with Minimax Algorithm
# ─────────────────────────────────────────────

HUMAN = "X"
AI    = "O"
EMPTY = " "


def create_board():
    return [EMPTY] * 9


def print_board(board):
    print("\n")
    for row in range(3):
        cells = board[row*3 : row*3+3]
        print(f"  {cells[0]} | {cells[1]} | {cells[2]} ")
        if row < 2:
            print("  --|---|--")
    print("\n")


def print_position_guide():
    print("  Position guide:")
    for row in range(3):
        cells = [str(row*3 + col + 1) for col in range(3)]
        print(f"  {cells[0]} | {cells[1]} | {cells[2]} ")
        if row < 2:
            print("  --|---|--")
    print()


def get_winner(board):
    wins = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # columns
        [0,4,8], [2,4,6]             # diagonals
    ]
    for a, b, c in wins:
        if board[a] == board[b] == board[c] != EMPTY:
            return board[a]
    return None


def is_draw(board):
    return EMPTY not in board and get_winner(board) is None


def is_terminal(board):
    return get_winner(board) is not None or is_draw(board)


def get_empty_cells(board):
    return [i for i, cell in enumerate(board) if cell == EMPTY]


# ── Minimax Algorithm ──────────────────────────────────────────
def minimax(board, depth, is_maximizing, alpha, beta):
    winner = get_winner(board)
    if winner == AI:
        return 10 - depth
    if winner == HUMAN:
        return depth - 10
    if is_draw(board):
        return 0

    if is_maximizing:
        best = -math.inf
        for i in get_empty_cells(board):
            board[i] = AI
            score = minimax(board, depth + 1, False, alpha, beta)
            board[i] = EMPTY
            best = max(best, score)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = math.inf
        for i in get_empty_cells(board):
            board[i] = HUMAN
            score = minimax(board, depth + 1, True, alpha, beta)
            board[i] = EMPTY
            best = min(best, score)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best


def best_move(board):
    best_score = -math.inf
    move = None
    for i in get_empty_cells(board):
        board[i] = AI
        score = minimax(board, 0, False, -math.inf, math.inf)
        board[i] = EMPTY
        if score > best_score:
            best_score = score
            move = i
    return move


# ── Game Flow ──────────────────────────────────────────────────
def human_turn(board):
    while True:
        try:
            pos = int(input("  Your move (1-9): ")) - 1
            if pos < 0 or pos > 8:
                print("  Please enter a number between 1 and 9.")
            elif board[pos] != EMPTY:
                print("  That cell is already taken. Try again.")
            else:
                board[pos] = HUMAN
                break
        except ValueError:
            print("  Invalid input. Please enter a number.")


def ai_turn(board):
    print("  AI is thinking...")
    move = best_move(board)
    board[move] = AI
    print(f"  AI played at position {move + 1}.")


def play_game():
    print("=" * 40)
    print("   Tic-Tac-Toe AI  |  CodSoft Task 2")
    print("   You = X   |   AI = O")
    print("=" * 40)
    print_position_guide()

    board = create_board()

    # Let the user choose who goes first
    while True:
        choice = input("  Do you want to go first? (y/n): ").strip().lower()
        if choice in ("y", "n"):
            human_first = choice == "y"
            break
        print("  Please enter 'y' or 'n'.")

    current = HUMAN if human_first else AI

    while not is_terminal(board):
        print_board(board)
        if current == HUMAN:
            human_turn(board)
            current = AI
        else:
            ai_turn(board)
            current = HUMAN

    print_board(board)

    winner = get_winner(board)
    if winner == HUMAN:
        print("  🎉 Congratulations! You won!")
    elif winner == AI:
        print("  🤖 AI wins! Better luck next time.")
    else:
        print("  🤝 It's a draw!")


def main():
    while True:
        play_game()
        again = input("\n  Play again? (y/n): ").strip().lower()
        if again != "y":
            print("\n  Thanks for playing! Goodbye 👋")
            break
        print("\n" + "=" * 40)


if __name__ == "__main__":
    main()