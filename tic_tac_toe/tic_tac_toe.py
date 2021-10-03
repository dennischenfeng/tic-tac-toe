"""
Simple tic tac toe game, playable by 2 human players. Only includes basic functionality.
"""

from typing import List

# a winning chain is a chain of positions (e.g. 3 in a row) which constitutes a winning condition.
WINNING_CHAINS = (
    ((0, 0), (0, 1), (0, 2)),
    ((1, 0), (1, 1), (1, 2)),
    ((2, 0), (2, 1), (2, 2)),
    ((0, 0), (1, 0), (2, 0)),
    ((0, 1), (1, 1), (2, 1)),
    ((0, 2), (1, 2), (2, 2)),
    ((0, 0), (1, 1), (2, 2)),
    ((0, 2), (1, 1), (2, 0)),
)
DISPLAY_SYMBOLS = {0: " ", 1: "X", 2: "O"}


class Engine:
    """
    Game engine, handles computations of playing moves on board, determining whether board is in a winning state, etc.
    """

    def __init__(self):
        self.height = 3
        self.width = 3
        self.board = [[0 for _ in range(self.width)] for _ in range(self.height)]
        self.active_player = 1

    def play_move(self, row: int, col: int) -> bool:
        """
        Place a move (using active player), unless it is an invalid move. Return True if valid move, False otherwise.

        :param row: row of position
        :param col: column of position
        :return: whether move succeeded
        """
        if (0 <= row < self.height) and (0 <= col < self.width) and (self.board[row][col] == 0):
            self.board[row][col] = self.active_player
            self.active_player = 3 - self.active_player
            return True
        else:
            return False

    def visual_board(self) -> List[List[str]]:
        """
        Return board with visual symbols (X, O, spaces)

        :return: board (list of lists) with visual symbols
        """
        displayed_board = []
        for row_of_values in self.board:
            row_of_values_visual = list(map(lambda elem: DISPLAY_SYMBOLS[elem], row_of_values))
            displayed_board.append(row_of_values_visual)
        return displayed_board

    def compute_game_status(self) -> int:
        """
        Returns game status. 0 means ongoing, 1 means player 1 won, 2 means player 2 won, 3 means draw.
        Performs this by checking if either player has any of the winning chains.

        :return: integer representing status of game
        """
        for chain in WINNING_CHAINS:
            values_in_chain = set()
            for row, col in chain:
                values_in_chain.add(self.board[row][col])

            if (len(values_in_chain) == 1) and (0 not in values_in_chain):
                return values_in_chain.pop()

        # check if any 0's on board
        values = set()
        for row_of_values in self.board:
            values.update(row_of_values)

        if 0 in values:
            return 0
        else:
            return 3


class UserInterface:
    """
    User interface, which handles user inputs, and displaying game progression to user
    """

    def __init__(self):
        self.engine = Engine()

    def start_game(self) -> None:
        """
        Starts the game, where each round will ask for the player's move, which should be a tuple of integers
        representing the position of their move. If invalid, the game will ask to re-submit a move.

        After each move, the resultant board will be displayed. If game ends, it will display who won.

        :return: None
        """
        print("Starting a game of tic-tac-toe.")
        print(
            "Two players will play this game. At each turn, play a move (for the specified player) by inputting row "
            "and column separated by a comma, like '1,0'. If input is invalid, it will ask you to try again. When you "
            "play a valid move, it will display the resultant board. When game ends, it will display the end-game "
            "status."
        )
        print("Starting board: ")
        self.print_visual_board()

        while True:
            input_string = input(f"Please input your move (player {self.engine.active_player}): ")
            split = input_string.split(",")

            invalid_input_message = (
                "Invalid input. Input position must be within the board, and not already be occupied. "
                "Example of valid input: '1,2' (without the quotes)"
            )

            if len(split) != 2:
                print(invalid_input_message)
                continue

            try:
                row = int(split[0])
                col = int(split[1])
            except ValueError as e:
                print(invalid_input_message)
                print(f"Error message of invalid input: {str(e)}")
                continue

            success = self.engine.play_move(row, col)
            if not success:
                print(invalid_input_message)
                continue

            self.print_visual_board()

            status = self.engine.compute_game_status()
            if status in [1, 2]:
                print(f"Player {status} wins the game!")
                break
            elif status == 3:
                print(f"The game ends in a draw!")
                break

    def print_visual_board(self) -> None:
        """
        Prints the visual board, as a 3x3 grid.

        :return: None
        """
        visual_board = self.engine.visual_board()
        for row_values in visual_board:
            print(row_values)


if __name__ == "__main__":
    ui = UserInterface()
    ui.start_game()
