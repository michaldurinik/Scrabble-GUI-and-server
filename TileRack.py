from Tile import Tile


class TileRack:

    def __init__(self, rack_size=0, rack_array=[Tile]):  # array of Tile objects
        self.rack_Size = rack_size
        self.rack_array = rack_array

        #   Size of tile rack will be always 7 while there are
        #   tiles remaining in TileBag.
        #   Tiles will be stored in array and we can access them by their index.

    def is_full(self):
        #   Check if the rack has all 7 tiles in it.
        return True

    def is_empty(self):
        #   Check if the rack is empty, if there are no tiles in the rack.
        return True

    def take_tile(position):  # index of Tile in rackArray
        #   When player play their tile onto the board, it will be
        #   removed from an array of tiles and
        #   the size of the rack will be reduced by 1.
        return Tile

    def refill_rack(self):
        #   Will be removing tiles out of tiles bag and placing them onto
        #   rack until the rack is full.
        return


def main():
    pass


if __name__ == "__main__":
    main()
