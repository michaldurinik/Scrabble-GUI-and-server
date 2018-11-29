class Tile:

    def __init__(self, letter="E", value=1):
        self.letter = letter
        self.value = value

        # Tile class will hold numerical value of the tile
        # and it's actual corresponding letter.

    def check_value(self):
        # It will return numerical value of tile when requested.
        return self.value

    def check_letter(self):
        # It will return letter of tile when requested.
        return self.letter

    def __str__(self):
        return self.letter + ": " + str(self.value)


def main():
    t = Tile()
    print(t)


if __name__ == "__main__":
    main()