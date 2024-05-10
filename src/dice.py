from defines import *
import random
import pygame
import time

#from collections import deque #-------
#seq  = deque([6,6,6,2]) #----------

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
    
    def gotThreeSixInRow():
        Dice.sixCount +=1 if Dice.currentCount==6 else 0
        print("Dice sixcount: ",Dice.sixCount)
        if Dice.sixCount<3:
            return False
        else:
            Dice.availableTurns = 0
            return True

    def setToNextTurn():
        Dice.img = Dice.imgList[6]
        Dice.imgRect.topleft = Dice.getDiceNextTurnDimensions()
        SEQUENCE.rotate(-1)
        Dice.currentTurn = SEQUENCE[0]
        Dice.isRolled = False
        Dice.availableTurns = 1
        Dice.sixCount = 0

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

        # seq.rotate(-1) #------------
        # count = seq[0] #----------------
        # Dice.img = Dice.imgList[count] #----------------
        # Dice.blitDice(SCREEN) #----------------
        # pygame.display.update() #----------------
        
        Dice.currentCount = count
        Dice.isRolled = True
        if Dice.currentCount==6:
            Dice.availableTurns += 1