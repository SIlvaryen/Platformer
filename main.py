import pygame as pg
import random
from settings import *
from sprites import *

class Game():
    def __init__(self):
        #initialize game
        pg.init()
        pg.mixer.init()

        self.running = True

        self.surface = pg.display.set_mode(screenSize)
        pg.display.set_caption(title)

    def new(self):
        #makes a new Game
        self.allSprites = pg.sprite.LayeredUpdates()

        self.platforms = pg.sprite.Group()
        self.player = Player()
        self.allSprites.add(self.player)
        for plat in platformList:
            p = Platform(*plat)
            self.allSprites.add(p)
            self.platforms.add(p)
    def run(self):
        #Runs the game permanently until self.running not is equal to True
        self.playing = True
        while self.playing:
            #Declaring the Delay
            clock.tick(FPS)
            self.events()
            self.update()
            self.render()

    def update(self):
        #Updates all Sprites
        self.allSprites.update()
        self.player.inAir = True

        for pl in self.platforms:
            if self.player.topEdge.colliderect(pl.bottomEdge):
                self.player.rect.top = pl.rect.bottom
                self.player.vely = 0
            elif self.player.bottomEdge.colliderect(pl):
                self.player.rect.bottom = pl.rect.top
                self.player.vely = 0
                self.player.inAir = False
            elif self.player.leftEdge.colliderect(pl):
                self.player.rect.left = pl.rect.right
                self.player.velx = 0
            elif self.player.rightEdge.colliderect(pl):
                self.player.rect.right = pl.rect.left
                self.player.velx = 0

    def events(self):
        #Tracks all events and reacts on 'em'
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.playing = False
                self.running = False
            if event.type == pg.KEYUP:
                if event.key == pg.K_ESCAPE:
                    self.showPauseScreen()

    def render(self):
        #Render all sprites
        self.surface.fill(black)
        self.allSprites.draw(self.surface)
        pg.display.update()

    def showGOScreen(self):
        #Show Game Over Screen
        pass

    def showStartScreen(self):
        #Show Start Screen
        pass

    def showPauseScreen(self):
        #Show Pause Screen
        self.playing = False
        self.running = False

game = Game()
game.showStartScreen()
while game.running:
    game.new()
    game.run()
    game.showGOScreen()

pg.quit()
