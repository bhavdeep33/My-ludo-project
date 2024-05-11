from defines import *
import random
import pygame
import time

class Dice:
    isRolled = False
    currentCount = 0
    currentTurn = RED
    sixCount = 0
    IMGLIST = [None]
    img = None
    imgRect = None
    availableTurns = 1

    @staticmethod
    def blitDice(SCREEN):
        SCREEN.blit(Dice.img,Dice.imgRect)

    @staticmethod
    def isDiceClicked(mousePos):
        if Dice.imgRect.collidepoint(mousePos):
            return True
        return False
    
    @staticmethod
    def getDiceNextTurnDimensions():
        Dimensions.dicePositions.rotate(-1)
        return  Dimensions.dicePositions[0]
    
    @staticmethod
    def gotThreeSixInRow():
        Dice.sixCount +=1 if Dice.currentCount==6 else 0
        if Dice.sixCount<3:
            return False
        else:
            return True

    @staticmethod
    def setToNextTurn():
        Dice.img = Dice.IMGLIST[6]
        Dice.imgRect.topleft = Dice.getDiceNextTurnDimensions()
        sequence.rotate(-1)
        Dice.currentTurn = sequence[0]
        Dice.isRolled = False
        Dice.availableTurns = 1
        Dice.sixCount = 0
    
    @staticmethod
    def rollDice(SCREEN):
        Dice.DICE_SOUND.play()
        count= 0
        for i in range(50):
            count = random.randint(1,6)
            Dice.img = Dice.IMGLIST[count]
            Dice.blitDice(SCREEN)
            pygame.display.update()
            time.sleep(0.01)

        Dice.currentCount = count
        Dice.isRolled = True
        if Dice.currentCount==6:
            Dice.availableTurns += 1

    @staticmethod
    def removeFromSequence(type):
        sequence.remove(type)
        dicePosToBeRemoved = Dimensions.dicePositions[-1]
        Dimensions.dicePositions.remove(dicePosToBeRemoved)