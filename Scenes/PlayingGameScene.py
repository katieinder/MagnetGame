import pygame
from Shared import *
from Scenes.Scene import Scene
import sys

class PlayingGameScene(Scene):

    def __init__(self, game):
         super(PlayingGameScene, self).__init__(game)

    def render(self):
        super(PlayingGameScene, self).render()

        game = self.getGame()

        ball=game.getBalls

        magnet=game.getMagnet

        target=game.getTarget

        if ball.intersects(magnet):
            ball.changeDirection(magnet)

        ball.updatePosition()

        game.screen.blit(ball.getSprite(), ball.getPosition())

        magnet.setPosition((GameConstants.MagnetPosition[0], GameConstants.MagnetPosition[1]))
        game.screen.blit(magnet.getSprite(), magnet.getPosition())

        target.setPosition((GameConstants.TargetPosition[0], GameConstants.TargetPosition[1]))
        game.screen.blit(target.getSprite(), target.getPosition())

    def handleEvents(self, events):
        super(PlayingGameScene, self).handleEvents(events)

        for event in events:
            if event.type == pygame.QUIT:sys.exit()

