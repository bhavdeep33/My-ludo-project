from defines import Dimensions
from dice import Dice
from block import HomeBlock,StartingPointBlock
import pygame
import time

class Player:
    Players = []

    def __init__(self,type,rect_x,rect_y,img):
        self.type = type
        self.currentBlock = None
        self.isInsideHome = False
        # self.isOutsideBase = True
        self.initialImgRect = pygame.Rect(rect_x,rect_y,Dimensions.BLOCKSIZE,Dimensions.BLOCKSIZE)
        self.imgRect = self.initialImgRect.copy()
        self.img = img
        Player.Players.append(self)

    def blitPlayer(self,SCREEN):
        imgX = self.imgRect.x
        imgY = self.imgRect.y - Dimensions.B/2
        SCREEN.blit(self.img,(imgX,imgY))

    @staticmethod
    def blitPlayers(SCREEN):
        for player in Player.Players:
            player.blitPlayer(SCREEN)

    @staticmethod
    def playerClicked(type,mouse_pos):
        for player in Player.Players:
            if(player.type==type and player.imgRect.collidepoint(mouse_pos)):
                    #print("Clicked on image!")
                    return player
        return None

    def isMovable(self):
        if self.currentBlock is None:
            if(Dice.currentCount==6):
                return True
            else:
                return False
        else:
            #print("Player is not outside")
            count = Dice.currentCount
            currentBlock = self.currentBlock
            while count!=0 and not isinstance(currentBlock,HomeBlock):
                #print(currentBlock)
                currentBlock = currentBlock.nextBlock(currentBlock.type)
                count -= 1
            return True if count==0 else False
        
    def movablePlayersAvailable():
        movablePlayers = []
        for player in Player.Players:
            if player.type==Dice.currentTurn and player.isMovable():
                movablePlayers.append(player)
        return movablePlayers

    def getPlayers():
        pass

    def adjust():
        pass

    def setDefaultSize():
        pass
    
    def canKill(self):
        playersAtBlock = self.currentBlock.players
        if len(playersAtBlock)==2 and not self.currentBlock.isSafe() and (playersAtBlock[0].type!=self.type):
            return True
        return False

    def getKilled(self,game):
        print(self,"is Getting killed")
        self.currentBlock.players.remove(self)
        self.currentBlock = None
        self.imgRect = self.initialImgRect
        Dice.availableTurns += 1

    def movePlayer(self,currentCount,game):
        if self.currentBlock is None:
            targetBlock = StartingPointBlock.getStartingPointBlockFor(self.type)
            self.imgRect.topleft = (targetBlock.x,targetBlock.y)
            self.currentBlock = targetBlock
        else:
            self.currentBlock.players.remove(self)
            count = currentCount
            while count!=0:
                nextBlock = self.currentBlock.nextBlock(self.type)
                self.imgRect.topleft = (nextBlock.x,nextBlock.y)
                self.currentBlock = nextBlock
                game.blitObjects()
                time.sleep(0.1)
                count -= 1
        self.currentBlock.players.append(self)
        Dice.isRolled = False
        Dice.currentCount = 0
        Dice.availableTurns -= 1