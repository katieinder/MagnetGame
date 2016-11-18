import pygame, sys
from Scenes.Scene import Scene
from Shared import *

class HitTargetScene(Scene):

    def __init__(self, game):
        super(HitTargetScene, self).__init__(game)


    def render(self):

        self.clearText()
        self.addText("You Win", 300, 200, size=30)
        super(HitTargetScene, self).render()

    def handleEvents(self, events):
        super(HitTargetScene, self).handleEvents(events)

        for event in events:
            if event.type == pygame.QUIT: sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game = self.getGame()
                    game.reset()
                if event.key == pygame.K_F1:
                    self.getGame().reset()
                    self.getGame().changeScene(GameConstants.PLAYING_SCENE)