import os
import pygame
pygame.init()

class GameConstants:
    SCREEN_SIZE = [800, 600]
    BALL_SIZE = [22, 22]
    MAGNET_SIZE = [100, 25]
    TARGET_SIZE = [25, 25]

    SPRITE_BALL = os.path.join( "Assets","Ball.png")
    SPRITE_MAGNET = os.path.join( "Assets","Magnet.png")
    SPRITE_TARGET = os.path.join( "Assets","Target.png")

    MagnetPosition = [400,300]
    TargetPosition = [700,500]

    PLAYINGGAMESCENE = 0
    HITTARGETSCENE = 1
    MENUSCENE = 2