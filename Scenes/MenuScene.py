from Scenes.Scene import Scene
from Shared import *
import pygame, sys


class MenuScene(Scene):
    def __init__(self, game):
        super(MenuScene, self).__init__(game)

        self.addText("Main Menu", x=400, y= 50, size=50)
        self.addText("F1 - Start Game", x=300, y=200, size=30)

    def render(self):

        super(MenuScene, self).render()

    def handleEvents(self, events):
        super(MenuScene, self).handleEvents(events)

        for event in events:
            if event.type == pygame.QUIT: sys.exit()

            if event.key == pygame.K_F1:
                self.getGame().changeScene(GameConstants.PLAYING_SCENE)