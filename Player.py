from Tile import Tile


class Player:

    def __init__(self, ID="", name="", score=0, active=True):
        self.ID = ID
        self.name = name
        self.score = score
        self.active = active

        #   Class will hold information about player,
        #   their unique ID, name and their score.
        #   If player decide to quit then game, his active status
        #   will be updated.
        #   Server will know to not assign next turn to the player.

    def confirm_move(self):
        #   Information about tiles placed on the board during
        #   player move will be send to the game class then to server.
        return

    def skip_turn(self):
        #   Player can forfeit their turn and information will
        #   be send to the game class and then to the server.
        return

    def join_lobby(self):
        #   When the game start, player will join the lobby
        #   where he will wait until 3 other players are found,
        #   server will then start the game.
        return

    def quit_game(self):
        #   Option to quit the game, game class will be notified.
        #   Current player will no longer be given turn to play,
        #   but his score will be displayed to others.
        return

    def get_tiles(self):
        #   Requests tiles from the tiles bag and populate tile rack.
        return [Tile]  # array of Tile objects

    def place_tile(self, Tile):
        #   Tile from tile rack will be removed and placed onto board.
        return

    def swap_tile(self, Tile):
        #   Up to 4 tiles can be swapped out of tile rack from tile bag per turn.
        #   It will count as finishing turn move.
        return

    def get_score(self):
        #   Return player score.
        return 0


def main():
    pass


if __name__ == "__main__":
    main()