from defines import *
import random
import pygame
import time

class Dice:
    isRolled = False
    currentCount = 0
    currentTurn = RED
    sixCount = 0
    imgList = [None]
    img = None
    imgRect = None
    availableTurns = 1

    def blitDice(SCREEN):
        SCREEN.blit(Dice.img,Dice.imgRect)

    def getDiceNextTurnDimensions():
        Dimensions.DICE_POSITIONS.rotate(-1)
        return  Dimensions.DICE_POSITIONS[0]
    
    def isMoreTurnsAvailable():
        pass

    def setToNextTurn():
        Dice.img = Dice.imgList[6]
        Dice.imgRect.topleft = Dice.getDiceNextTurnDimensions()
        SEQUENCE.rotate(-1)
        Dice.currentTurn = SEQUENCE[0]
        Dice.isRolled = False
        Dice.availableTurns = 1

    def isDiceClicked(mouse_pos):
        if Dice.imgRect.collidepoint(mouse_pos):
            #print("Clicked on Dice!")
            return True
        return False
    
    def rollDice(SCREEN):
        count= 0
        for i in range(50):
            count = random.randint(1,6)
            Dice.img = Dice.imgList[count]
            Dice.blitDice(SCREEN)
            pygame.display.update()
            time.sleep(0.01)

        Dice.currentCount = count
        Dice.isRolled = True
        Dice.availableTurns -= 1

        Dice.sixCount +=1 if Dice.currentCount==6 else 0