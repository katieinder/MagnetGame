from Shared.GameObject import GameObject
from Shared.GameConstants import GameConstants

class Target(GameObject):

    def __init__(self, position, sprite, game):
        self.__game =game
        super(Target, self).__init__(position, GameConstants.TARGET_SIZE, sprite)


    def getGame(self):
        return self.__game
