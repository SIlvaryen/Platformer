import pygame, os

black    = (   0,   0,   0)
white    = ( 255, 255, 255)
red      = ( 255,   0,   0)
lime     = (   0, 255,   0)
blue     = (   0,   0, 255)
yellow   = ( 255, 255,   0)
cyan     = (   0, 255, 255)
magenta  = ( 255,   0, 255)
silver   = ( 192, 192, 192)
gray     = ( 128, 128, 128)
darkred  = ( 128,   0,   0)
olive    = ( 128, 128,   0)
green    = (   0, 128,   0)
purple   = ( 128,   0, 128)
darkaqua = (   0, 128, 128)
navyblue = (   0,   0, 128)

screenSize = (480, 640)
title = 'Platformer'

clock = pygame.time.Clock()

FPS = 60

gameFolder = os.path.dirname(__file__)
imgFolder = os.path.join(gameFolder, 'img')
sndFolder = os.path.join(gameFolder, 'snd')

#Player Properties

playerAcc = 0.5
playerFriction = -0.12
gravity = 0.981

#platforms

platformList = [(0, screenSize[1] - 40, screenSize[0], 40),
                (0, screenSize[1] - 150, 100, 20),
                (screenSize[0] / 2 - 50, screenSize[1] - 200, 100, 20),
                (screenSize[0] - 100, screenSize[1] - 230, 100, 20)]

def waitForPlayerImput():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYUP:
                return

def terminate():
    pygame.quit()
    sys.exit()

def drawText(text, color, x, y, pos, size = 32):
    font = pygame.font.match_font('arial')
    font = pygame.font.Font(font, size)

    textobj = font.render(text, True, color)
    textRect = textobj.get_rect()

    if pos == 'topleft':
        textRext.topleft = (x,y)
    elif pos == 'topright':
        textRect.topright = (x,y)
    elif pos == 'topmid':
        textRect.centerx = x
        textRect.top = y
    elif pos == 'bottomleft':
        textRect.bottomleft = (x,y)
    elif pos == 'bottomright':
        textRext.bottomright = (x,y)
    elif pos == 'bottommid':
        textRect.centerx = x
        textRect.bottom = y
    elif pos == 'midleft':
        textRect.left = x
        textRect.centery = y
    elif pos == 'center':
        textRect.center = (x,y)
    elif pos == 'midright':
        textRect.centery = y
        textRect.right = x
    else:
        print('something went wrong! your input was ' + pos)

    surface.blit(textobj, textRect)
