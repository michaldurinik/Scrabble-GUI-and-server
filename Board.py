from Square import Square
from Tile import Tile
from random import randint


class Board(Square):

    def __init__(self, size=15):
        super().__init__()
        self.size = size
        self.square_array = [[Square() for i in range(self.size)] for j in range(self.size)]

        #   Size of the board correspond to how many rows and columns it will have.
        #   All the squares will be held in an arrays, which will create a matrix.

    def __iter__(self):
        for row in self.square_array:
            for square in row:
                yield square

    def get_square(self, coords):
        #   Based on square's x, y coordinates it will return
        #   corresponding square.
        x = coords[0]
        y = coords[1]
        if x < self.size and y < self.size:
            return self.square_array[x][y]

    def place_tile(self, coords, tile):
        #   coords must be tuple or an array of length 2
        #   Based on square's x, y coordinates, it will place
        #   tile into correct position on the board.
        x = coords[0]
        y = coords[1]
        if x < self.size and y < self.size:
            self.square_array[x][y].place_tile(tile)

    def make_board(self):
        bonus_square_colours = ["light_blue", "dark_blue", "light_red", "dark_red"]
        double_letter = randint(15, 25)  # 20
        triple_letter = randint(9, 15)   # 12
        double_word =   randint(12, 20)  # 16
        triple_word =    randint(6, 10)  # 8

        for idx, num_of_bonus_squares in enumerate([double_letter, triple_letter, double_word, triple_word]):
            while num_of_bonus_squares:
                random_square = self.square_array[randint(0, self.size - 1)][randint(0, self.size - 1)]
                if random_square.colour == "default":
                    random_square.colour = bonus_square_colours[idx]
                    num_of_bonus_squares -= 1

    def __str__(self):
        output = ""
        line = ("----" * self.size + "-\n")
        for arr in self.square_array:
            output += line
            for sq in arr:
                if sq.is_occupied():
                    output += ("|" + sq.get_tile().__str__())
                else:
                    output += "|   "
            output += "|\n"
        output += line
        return output


def main():
    t1 = Tile("R", 1)
    t2 = Tile("X", 8)
    t3 = Tile("Q", 10)
    b = Board()
    print(b)

    b.place_tile((10, 10), t1)
    b.place_tile([5, 5], t2)
    b.place_tile([6, 6], t3)
    print(b)

    print(b.get_square([3, 3]))
    print(b.get_square([10, 10]))


if __name__ == "__main__":
    main()
