"""
Tic Tac Toe Project
Lenny
Day 3 and 4
"""


class Board:
    """
    Represents the Tic Tac Toe board.
    """

    def __init__(self):
        """
        Initializes an empty 3x3 Tic Tac Toe board.
        """
        self.board = [[" ", " ", " "],
                      [" ", " ", " "],
                      [" ", " ", " "]]

    def display(self):
        """
        Displays the current state of the board.
        """
        print("      0     1     2")
        n = 0
        for row in self.board:
            print(f"{n}   {row}")
            n += 1

    def row_win(self):
        """
        Checks for a win in any row.

        Returns:
        bool: True if there is a row win, False otherwise.
        """
        for row in self.board:
            if row[0] == row[1] == row[2] != " ":
                return True
        return False

    def col_win(self):
        """
        Checks for a win in any column.

        Returns:
        bool: True if there is a column win, False otherwise.
        """
        for i in range(3):
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != " ":
                return True
        return False

    def diag_win(self):
        """
        Checks for a win in any diagonal.

        Returns:
        bool: True if there is a diagonal win, False otherwise.
        """
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return True
        return False

    def check_win(self):
        """
        Checks for any win (row, column, or diagonal).

        Returns:
        bool: True if there is any win, False otherwise.
        """
        return self.row_win() or self.col_win() or self.diag_win()


class Player:
    """
    Represents a player in the Tic Tac Toe game.
    """

    def __init__(self, name, symbol):
        """
        Initializes a player with a name and a symbol.

        Parameters:
        name (str): The name of the player.
        symbol (str): The symbol of the player (e.g., 'X' or 'O').
        """
        self.name = name
        self.symbol = symbol

    def play(self, board):
        """
        Allows the player to make a move on the board.

        Parameters:
        board (Board): The Tic Tac Toe board.

        Returns:
        bool: True if the move is valid, False otherwise.
        """
        print(f"{self.name}'s turn")
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter column (0-2): "))
        try:
            if board.board[row][col] != " ":
                print("Invalid move. Try again.")
                return False

            board.board[row][col] = self.symbol
            return True
        except IndexError:
            print("Invalid move. Try again.")
            return False

# Initialize the Tic Tac Toe board and players.
tictactoe = Board()
p1 = Player(input("Player 1, What is your name: "), "X")
p2 = Player(input("Player 2, what is your name: "), "O")
print(f"Welcome to Tic Tac Toe!\n{p1.name} is {p1.symbol} and {p2.name} is {p2.symbol}")

# Display the initial state of the board.
current_player = p1
tictactoe.display()

# Main game loop.
while True:
    while not current_player.play(tictactoe):
        pass
    tictactoe.display()
    if tictactoe.check_win():
        print(f"{current_player.name} wins!")
        break
    if all([x != " " for row in tictactoe.board for x in row]):
        print("It's a tie!")
        break
    current_player = p2 if current_player == p1 else p1
