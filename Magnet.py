from Shared.GameConstants import GameConstants
from Shared.GameObject import GameObject

class Magnet(GameObject):

    def __init__(self, position, sprite):
        super(Magnet, self).__init__(position, GameConstants.MAGNET_SIZE, sprite)

    def setPosition(self, position):

        newPosition = [position[0], position[1]]
        size = self.getSize()

        if newPosition[0] + size[0] > GameConstants.SCREEN_SIZE[0]:
            newPosition[0] = GameConstants.SCREEN_SIZE[0] - size[0]

        if newPosition[1] - size[1] >GameConstants.SCREEN_SIZE[1]:
            newPosition[1] = GameConstants.SCREEN_SIZE[1] - size[1]

        super(Magnet, self).setPosition(newPosition)

    def Rotate(self):
        pass