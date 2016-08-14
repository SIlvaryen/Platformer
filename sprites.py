import pygame as pg
from settings import *
vec = pg.math.Vector2

class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface((30,30))
        self.image.fill(darkred)
        self.rect = self.image.get_rect()

        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.pos = vec(screenSize[0] / 2,screenSize[1] / 2)

        self.rect.midbottom = self.pos

        self.inAir = True

        self.topEdge = pg.Rect(self.rect.left + 1, self.rect.top, self.rect.width - 2, 1)
        self.bottomEdge = pg.Rect(self.rect.left + 1, self.rect.bottom, self.rect.width - 2, 1)
        self.leftEdge = pg.Rect(self.rect.left, self.rect.top + 1, 1, self.rect.height - 2)
        self.rightEdge = pg.Rect(self.rect.right, self.rect.top + 1, 1, self.rect.height - 2)

    def update(self):
        self.acc = vec(0,0)

        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.acc.x = -playerAcc
        elif keys[pg.K_RIGHT]:
            self.acc.x = playerAcc
        if keys[pg.K_SPACE]:
            self.jump()

        self.acc.y = gravity
        self.acc.x = self.vel.x * playerFriction
        
        self.vel += self.acc
        self.pos += self.vel

        self.rect.midbottom = self.pos

        if self.rect.bottom > screenSize[1]:
            self.rect.top = 0

        self.topEdge = pg.Rect(self.rect.left + 1, self.rect.top, self.rect.width - 2, 1)
        self.bottomEdge = pg.Rect(self.rect.left + 1, self.rect.bottom, self.rect.width -2, 1)
        self.leftEdge = pg.Rect(self.rect.left, self.rect.top + 1, 1, self.rect.height - 2)
        self.rightEdge = pg.Rect(self.rect.right, self.rect.top + 1, 1, self.rect.height - 2)

    def jump(self):
        if not self.inAir:
            self.vely = -40

    def render(self, surface):
        pg.draw.rect(surface, yellow, (self.leftEdge))
        pg.draw.rect(surface, yellow, (self.rightEdge))
        pg.draw.rect(surface, yellow, (self.topEdge))
        pg.draw.rect(surface, yellow, (self.bottomEdge))

class Platform(pg.sprite.Sprite):
    def __init__(self,x,y,w,h):
        super().__init__()
        self.image = pg.Surface((w,h))
        self.image.fill(green)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.topEdge = pg.Rect(self.rect.left + 1, self.rect.top, self.rect.width - 2, 1)
        self.bottomEdge = pg.Rect(self.rect.left + 1, self.rect.bottom, self.rect.width - 2, 1)
        self.leftEdge = pg.Rect(self.rect.left, self.rect.top + 1, 1, self.rect.height - 2)
        self.rightEdge = pg.Rect(self.rect.right, self.rect.top + 1, 1, self.rect.height - 2)
