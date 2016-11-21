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

            if event.type == pygame.KEYDOWN:
                for magnet in self.getGame().getMagnet():
                    positionx, positiony = GameObject.getPosition(magnet)[0], GameObject.getPosition(magnet)[1]
                    if event.key == pygame.K_d and positionx + GameConstants.MAGNET_SIZE[0] < GameConstants.SCREEN_SIZE[0]:
                        positionx += 6
                    else:
                        positionx = 0
                    if event.key == pygame.K_a and positionx > 0:
                        positionx -= 6
                    if event.key == pygame.K_s and positiony + GameConstants.MAGNET_SIZE[1] < GameConstants.SCREEN_SIZE[1]:
                        positiony += 6
                    else:
                        positiony = 0
                    if event.key == pygame.K_w and positiony > 0:
                        positiony -= 6
            if event.type == pygame.KEYUP:
                for magnet in self.getGame().getMagnet():
                    positionx, positiony = GameObject.getPosition(magnet)[0], GameObject.getPosition(magnet)[1]
                    if event.key == pygame.K_d:
                        positionx = 0
                    if event.key == pygame.K_a:
                        positionx = 0
                    if event.key == pygame.K_w:
                        positiony = 0
                    if event.key == pygame.K_s:
                        positiony = 0


