import pygame
from PIL import Image
from player import Player
from dice import Dice
from defines import *

class Game:
    SCREEN = None
    FPSCLOCK = None
    exitGame = False

    def __init__(self):
        Dimensions.defineBlockDimensions()
        self.initGameWindow()
        self.initPlayers()
        self.initDice()

    def initGameWindow(self):
        pygame.init()
        self.SCREEN = pygame.display.set_mode((Dimensions.SCREENWIDTH,Dimensions.SCREENHEIGHT))
        self.FPSCLOCK = pygame.time.Clock()
        pygame.display.set_caption(CAPTION)

    def initPlayers(self):
        for entry in Dimensions.PLAYERS_INITIAL_POS_BASE_DEMENSIONS:
            type,base_x,base_y = entry[0],entry[1],entry[2]
            playerImage = f"Images/{type}.png"
            P = Dimensions.PLAYERS_INITIAL_POS_SPACINGS

            rectPlayer = self.resizeImg(playerImage,Dimensions.BLOCKSIZE,Dimensions.BLOCKSIZE)
            resizedPlayer = self.resizeImg(playerImage,Dimensions.PLAYERWIDTH,Dimensions.PLAYERHEIGHT)

            Player(type,base_x,base_y,resizedPlayer,rectPlayer)
            Player(type,base_x + P,base_y,resizedPlayer,rectPlayer)
            Player(type,base_x,base_y + P,resizedPlayer,rectPlayer)
            Player(type,base_x + P,base_y + P,resizedPlayer,rectPlayer)

    def initDice(self):
        for i in range(1,7):
            resizedDice = self.resizeImg(f"Images/{i}.png",Dimensions.DICEHEIGHT,Dimensions.DICEWIDTH)
            Dice.imgList.append(resizedDice)
        Dice.img = Dice.imgList[6]
        Dice.img_rect = Dice.img.get_rect()
        initial_pos = Dimensions.DICE_POSITIONS[0]
        Dice.img_rect.topleft = (initial_pos[0],initial_pos[1])

    #Resizing image according to the screen dimentions
    def resizeImg(self,path,new_width,new_height):
        image = Image.open(path)
        size = (int(new_width), int(new_height))
        resized_img = image.resize(size, resample=Image.LANCZOS)
        # # create a pygame surface from the byte string
        resized_img = pygame.image.fromstring(resized_img.tobytes(), resized_img.size, resized_img.mode)
        return resized_img

    def blitObjects(self):
        self.blitBase()
        Player.blitPlayers(self.SCREEN)
        Dice.blitDice(self.SCREEN)
        pygame.display.update()
        self.FPSCLOCK.tick(60)

    def blitBase(self):
        resized_base = self.resizeImg('Images/Base.png',Dimensions.SCREENWIDTH,Dimensions.SCREENHEIGHT)
        self.SCREEN.blit(resized_base,(0,0))