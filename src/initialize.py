import pygame
from PIL import Image
from player import Player
from dice import Dice
from block import Block
from defines import *
from tkinter import messagebox

class Game:
    SCREEN = None
    FPSCLOCK = None
    exitGame = False
    GAME_START_SOUND = None
    sequence  = deque([RED,GREEN,YELLOW,BLUE])

    @classmethod
    def resetClass(cls):
        cls.sequence  = deque([RED,GREEN,YELLOW,BLUE])

    def __init__(self):
        Dimensions.defineBlockDimensions()
        self.initGameWindow()
        self.initSounds()
        self.initPlayers()
        self.initDice()
        Game.GAME_START_SOUND.play()

    @staticmethod
    def restartGame():
        pygame.quit()
        Game.resetClass()
        Block.resetClass()
        Dice.resetClass()
        Player.resetClass()
        
    def initGameWindow(self):
        pygame.init()
        self.SCREEN = pygame.display.set_mode((Dimensions.SCREENWIDTH,Dimensions.SCREENHEIGHT))
        self.FPSCLOCK = pygame.time.Clock()
        pygame.display.set_caption(CAPTION)

    def initSounds(self):
        Player.KILL_SOUND = pygame.mixer.Sound('Sounds/killed.wav')
        Dice.DICE_SOUND = pygame.mixer.Sound('Sounds/Dice.wav')
        Player.JUMP_SOUND = pygame.mixer.Sound('Sounds/Jump.wav')
        Player.HOME_SOUND = pygame.mixer.Sound('Sounds/Home.wav')
        Player.REACHED_HOME_SOUND = pygame.mixer.Sound('Sounds/Reached_home.wav')
        Game.GAME_START_SOUND = pygame.mixer.Sound('Sounds/Game_started.wav')

    def initPlayers(self):
        for entry in Dimensions.PLAYERS_INITIAL_RECT_POS:
            type,rectX,rectY = entry[0],entry[1],entry[2]
            playerImage = f"Images/{type}.png"
            P = Dimensions.PLAYERS_INITIAL_POS_SPACINGS
            
            resizedPlayer = self.resizeImg(playerImage,Dimensions.PLAYERWIDTH,Dimensions.PLAYERHEIGHT)
            
            Player(type,rectX,rectY,resizedPlayer)
            Player(type,rectX + P,rectY,resizedPlayer)
            Player(type,rectX,rectY + P,resizedPlayer)
            Player(type,rectX + P,rectY + P,resizedPlayer)

    def initDice(self):
        for i in range(1,7):
            resizedDice = self.resizeImg(f"Images/{i}.png",Dimensions.DICEHEIGHT,Dimensions.DICEWIDTH)
            Dice.IMGLIST.append(resizedDice)
        Dice.img = Dice.IMGLIST[6]
        Dice.imgRect = Dice.img.get_rect()
        initialPos = Dimensions.dicePositions[0]
        Dice.imgRect.topleft = (initialPos[0],initialPos[1])

    def resizeImg(self,path,newWidth,newHeight):
        image = Image.open(path)
        size = (int(newWidth), int(newHeight))
        resizedImg = image.resize(size, resample=Image.LANCZOS)
        # # create a pygame surface from the byte string
        resizedImg = pygame.image.fromstring(resizedImg.tobytes(), resizedImg.size, resizedImg.mode)
        return resizedImg

    def blitObjects(self):
        self.blitBase()
        Dice.blitDice(self.SCREEN)
        self.blitBanner()
        Player.blitPlayers(self.SCREEN)
        pygame.display.update()
        self.FPSCLOCK.tick(60)

    def blitBase(self):
        resizedBase = self.resizeImg('Images/Base.png',Dimensions.SCREENWIDTH,Dimensions.SCREENHEIGHT)
        self.SCREEN.blit(resizedBase,(0,0))

    def blitBanner(self):
        resizedBanner = self.resizeImg('Images/Banner.png',Dimensions.BANNERWIDTH,Dimensions.BANNERHEIGHT)
        self.SCREEN.blit(resizedBanner,Dimensions.BANNER_POS[0])
        self.SCREEN.blit(resizedBanner,Dimensions.BANNER_POS[1])

    def isGameOver(self):
        if len(self.sequence)==1:
            return True
        return False
    
    def wantToPlayAgain(self):
        choice = messagebox.askyesno("Game Over", "Game over, do you want to play again?")
        if choice:
            return True
        else:
            return False