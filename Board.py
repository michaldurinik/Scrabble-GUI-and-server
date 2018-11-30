from Square import Square


class Board(Square):

    def __init__(self, letter="E", value=1, colour="white", tile_multiplier=0, word_multiplier=0, has_tile=None,
                 position=[0, 0], size=15):
        super().__init__(letter="E", value=1, colour="white", tile_multiplier=0, word_multiplier=0, has_tile=None,
                 position=[0, 0])
        self.size = size
        self.square_array = [[Square] * self.size] * self.size
        #   Size of the board correspond to how many rows and
        #   columns it will have.
        #   All the squares will be held in an arrays, which will create a matrix.

    def get_square(self):
        #   Based on square's x, y coordinates it will return
        #   corresponding square.
        return

    def place_tile(self):
        #   Based on square's x, y coordinates it will place
        #   tile into correct position on the board.
        return

    def make_board(self):
        pass

    def __str__(self):
        output = ""
        for arr in self.square_array:
            for sq in arr:
                output += (sq.get_tile(self).get_letter() + ":" + str(sq.get_tile(self).get_value()) + " ")
            output += "\n"
        return output


def main():
    b = Board()
    print(b)


if __name__ == "__main__":
    main()
