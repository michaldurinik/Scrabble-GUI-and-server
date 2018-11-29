from Tile import Tile


class Square(Tile):
    def __init__(self, letter="E", value=1, colour="white", tile_multiplier=0, word_multiplier=0, has_tile=None,
                 position=[0, 0]):
        super().__init__(letter, value)
        self.colour = colour
        self.tile_multiplier = tile_multiplier
        self.word_multiplier = word_multiplier
        self.hasTile = has_tile
        self.position = position

        #   Each individual square will be one of possible color types,
        #   has tile multiplier of at least 1, some x2 or x3,
        #   has word multiplier of at least 1, some x2 or x3.
        #   It will contain tile placed onto them
        #   position x, y coordinates.

    def get_colour(self):
        #   will return colour of square for GUI to display
        return self.colour

    def get_position(self):
        #   it will return x, y coordinates (position) of square in matrix
        return self.position

    def is_occupied(self):
        #   check if any of the tile is already placed on this square
        return self.has_tile is not None

    def get_tile(self):
        #   if square is occupied by tile, it will return tile object where we
        #   can access it's attributes
        return super()

    def place_tile(self):
        self.hasTile = Tile

    def get_letter_score(self):
        #   Will return total score for the square, ie.
        #   value of the tile placed multiplied by x1, x2 or x3.
        return super().check_value() * self.word_multiplier

    def get_word_multiplier(self):
        #   Return word multiplier x1, x2, x3, which will be used to
        #   multiply total score for the word.
        return self.word_multiplier

    def __str__(self):
        return ("colour: " + self.colour + "\n" +
                "t.mult: " + str(self.tile_multiplier) + "\n" +
                "w.mult: " + str(self.word_multiplier) + "\n" +
                "Tile: " + super().__str__() + "\n" +
                "Position: " + str(self.position[0]) + " " + str(self.position[1]))


def main():
    sq = Square()
    print(sq)


if __name__ == "__main__":
    main()
