from defines import Dimensions
from dice import Dice
from block import HomeBlock,StartingPointBlock,SafeBlock
import pygame
import time

class Player:
    PLAYERS = []

    @classmethod
    def resetClass(cls):
        for player in cls.PLAYERS:
            del player
        cls.PLAYERS.clear()

    def __init__(self,type,rect_x,rect_y,img):
        self.__type = type
        self.__initialImgRect = pygame.Rect(rect_x,rect_y,Dimensions.BLOCKSIZE,Dimensions.BLOCKSIZE)
        self.currentBlock = None
        self.imgRect = self.initialImgRect.copy()
        self.img = img
        self.x,self.y = self.getPlayersAttrWRTrect()
        Player.PLAYERS.append(self)

    @property
    def type(self):
        return self.__type

    @property
    def initialImgRect(self):
        return self.__initialImgRect
    
    @staticmethod
    def getPlayersByType(type):
        players = []
        for player in Player.PLAYERS:
            if player.type==type:
                players.append(player)
        return players

    @staticmethod
    def blitPlayers(SCREEN):
        sortedPlayers = sorted(Player.PLAYERS,key=lambda player:player.y)
        for player in sortedPlayers:
            SCREEN.blit(player.img,(player.x,player.y))

    @staticmethod
    def playerClicked(type,mousePos):
        for player in Player.PLAYERS:
            if(player.type==type and player.imgRect.collidepoint(mousePos)):
                    return player
        return None
    
    @staticmethod
    def movablePlayersAvailable():
        movablePlayers = []
        players = Player.getPlayersByType(Dice.currentTurn)
        for player in players:
            if player.isMovable():
                movablePlayers.append(player)
        return movablePlayers

    @staticmethod
    def allPlayersAtSameBlock(movablePlayers):
        rectPos = movablePlayers[0].imgRect
        for player in movablePlayers:
            if not player.imgRect.colliderect(rectPos):
                return False
        return True

    @staticmethod
    def groupPlayersAt(block,game):
        if not block or len(block.players)==0:
            return
        factor = len(block.players)
        newPlayerHeight = Dimensions.PLAYERHEIGHT/factor
        newPlayerWidth = Dimensions.PLAYERWIDTH/factor

        shrinkedHeight = Dimensions.PLAYERHEIGHT - newPlayerHeight

        firstBlockX,firstBlockY = block.players[0].getPlayersAttrWRTrect()
        initialX = firstBlockX
        initialY = firstBlockY + shrinkedHeight/1.5

        for i,player in enumerate(block.players):
            player.img = game.resizeImg(f"Images/{player.type}.png",newPlayerWidth,newPlayerHeight)
            player.x = initialX + i*newPlayerWidth
            player.y = initialY

    @staticmethod
    def popPlayersAtBlock(block,type):
        currentTypePlayers = block.getPlayersByType(type)

        offsetPerPlayer = Dimensions.POP_PLAYERS_SPACING * (len(currentTypePlayers)-1)/len(currentTypePlayers)
        currentTypePlayers[0].x = currentTypePlayers[0].x - offsetPerPlayer
        previousX = currentTypePlayers[0].x
        for player in currentTypePlayers[1:]:
            player.x = previousX + Dimensions.POP_PLAYERS_SPACING
            previousX = player.x
    
    @staticmethod
    def popAllMovablePlayers(movablePlayers,game):
        blocksToPop = set()
        for player in movablePlayers:
            if player.currentBlock:
                player.resetToDefaultSize(game)
                blocksToPop.add(player.currentBlock)
        
        for block in blocksToPop:
            Player.popPlayersAtBlock(block,movablePlayers[0].type)

    def getPlayersAttrWRTrect(self):
        x = self.imgRect.x
        y = self.imgRect.y - Dimensions.B/2
        return x,y
    
    def setAttributes(self,x,y):
        self.imgRect.topleft = (x,y)
        self.x,self.y = self.getPlayersAttrWRTrect()
    
    def resetToDefaultSize(self,game):
        self.x,self.y = self.getPlayersAttrWRTrect()
        self.img = game.resizeImg(f"Images/{self.type}.png",Dimensions.PLAYERWIDTH,Dimensions.PLAYERHEIGHT)

    def regroupAllPlayersOfCurrentType(self,game):
        players = Player.getPlayersByType(self.type)
        for player in players:
            Player.groupPlayersAt(player.currentBlock,game)

    def isMovable(self):
        if self.currentBlock is None:
            if(Dice.currentCount==6):
                return True
            else:
                return False
        else:
            count = Dice.currentCount
            currentBlock = self.currentBlock
            while count!=0 and not isinstance(currentBlock,HomeBlock):
                currentBlock = currentBlock.nextBlock(currentBlock.type)
                count -= 1
            return True if count==0 else False
    
    def allPlayersReachedHome(self):
        for player in Player.PLAYERS:
            if player.type==self.type and not isinstance(player.currentBlock,HomeBlock):
                return False
        return True
    
    def reachedHome(self):
        if isinstance(self.currentBlock,HomeBlock):
            return True
        return False
    
    def canKill(self):
        playersAtBlock = self.currentBlock.players
        if len(playersAtBlock)==2 and not self.currentBlock.isSafe() and (playersAtBlock[0].type!=self.type):
            return True
        return False

    def getKilled(self,game):
        Player.KILL_SOUND.play()
        for player in self.currentBlock.players:
            player.resetToDefaultSize(game)
        self.currentBlock.players.remove(self)
        self.currentBlock = None
        self.setAttributes(self.initialImgRect.x,self.initialImgRect.y)
        Dice.availableTurns += 1

    def movePlayer(self,currentCount,game):
        if self.currentBlock is None:
            targetBlock = StartingPointBlock.getStartingPointBlockFor(self.type)
            self.setAttributes(targetBlock.x,targetBlock.y)
            self.currentBlock = targetBlock
        else:
            self.currentBlock.players.remove(self)
            self.resetToDefaultSize(game)
            Player.groupPlayersAt(self.currentBlock,game)
            self.regroupAllPlayersOfCurrentType(game)
            count = currentCount
            while count!=0:
                nextBlock = self.currentBlock.nextBlock(self.type)
                self.setAttributes(nextBlock.x,nextBlock.y)
                self.currentBlock = nextBlock
                game.blitObjects()
                Player.JUMP_SOUND.play()
                time.sleep(0.1)
                count -= 1
        self.currentBlock.players.append(self)
        if self.reachedHome():
            Player.REACHED_HOME_SOUND.play()
        elif(isinstance(self.currentBlock,SafeBlock)):
            Player.HOME_SOUND.play()

        Player.groupPlayersAt(self.currentBlock,game)
        Dice.isRolled = False
        Dice.currentCount = 0
        Dice.availableTurns -= 1