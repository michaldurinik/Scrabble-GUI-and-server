from Square import Square
from Tile import Tile
from copy import deepcopy

class Board(Square):

    def __init__(self, colour="white", tile_multiplier=0, word_multiplier=0, has_tile=None,
                 position=[0, 0], size=15):
        super().__init__(colour="white", tile_multiplier=0, word_multiplier=0, has_tile=None,
                 position=[0, 0])
        self.size = size
        self.square_array = [[Square() for i in range(self.size)] for j in range(self.size)]

        sq = self.square_array[0][0]
        #print("empty square:", sq.get_tile())

        t = Tile()
        sq.place_tile(t)
        t2 = Tile("Q", 10)
        self.square_array[5][11].place_tile(t2)

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
        line = ("----" * self.size + "-\n")
        for arr in self.square_array:
            output += line
            for sq in arr:
                if sq.is_occupied():
                    value = str(sq.get_tile().get_value())
                    if len(value) == 1:
                        value = " " + value
                    output += ("|" + sq.get_tile().get_letter() + value)
                else:
                    output += "|   "
            output += "|\n"
        output += line
        return output


def main():
    b = Board()
    print(b)


if __name__ == "__main__":
    main()
