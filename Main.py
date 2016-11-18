import pygame

from Shared.GameConstants import GameConstants
from Magnet import Magnet
from Ball import Ball
from Target import Target
from Scenes.PlayingGameScene import PlayingGameScene
from Scenes.MenuScene import MenuScene
from Scenes.HitTargetScene import HitTargetScene


class Main:

    def __init__(self):
        self.__clock = pygame.time.Clock()
        self.__screen = pygame.display.set_mode(GameConstants.SCREEN_SIZE)
        self.__Magnet=Magnet((GameConstants.SCREEN_SIZE[0]/2, GameConstants.SCREEN_SIZE[1]/2), pygame.image.load(GameConstants.SPRITE_MAGNET).convert_alpha())
        self.__Ball = Ball((0,0), pygame.image.load(GameConstants.SPRITE_BALL).convert_alpha(), self)
        self.__Target = Target((400,600), pygame.image.load(GameConstants.SPRITE_TARGET).convert_alpha(), self)

        pygame.mouse.set_visible(0)

        pygame.init()
        pygame.display.set_caption("Simple Game Test")

        self.__scenes=(
            PlayingGameScene(self),
            MenuScene(self),
            HitTargetScene(self)
        )

        self.__currentScene = 2


    def start(self):
        while 1:
           self.__clock.tick(100)
           self.__screen.fill([250,250,250])

           currentScene = self.__scenes[self.__currentScene]
           currentScene.handleEvents(pygame.event.get())
           currentScene.render()

           pygame.display.update()


    def changeScene(self, scene):
        self.__currentScene= scene

    def getBalls(self):
        return self.__balls

    def getMagnet(self):
        return self.__Magnet

    def getTarget(self):
        return self.__Target

if __name__ == "__main__":
	Main().start()
