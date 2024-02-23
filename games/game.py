from player import Player
from board import Board


class Game:

    def __init__(self):
        print("Start spel")
        name_x = input("Enter your Player name 1 who will play with token X: ")
        p1 = Player(name_x, "X")
        name_y = input("Enter your Player name 2 who will play with token O: ")
        p2 = Player(name_y, "O")

        # print(p1)
        # print(p2)

        board = Board(7, 6)
        board.print_board()

        won = False
        while not won:
            selection = input(
                f"Please select the number of the column you want to drop a token into: ")
            if not selection.isnumeric:
                print("Wrong selection. Please try again!")
                continue

            column = int(selection) - 1
            if not board.is_valid_column(column):
                print("Wrong column. Please try again!")
                continue

            row = board.empty_row_for_column(column)
            if row == -1:
                print("Row is full. Try again!")
                continue

            board.add_token(row, column, "X")
            board.print_board()


game = Game()
