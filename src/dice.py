from defines import *
import random

class Dice:
    isRolled = False
    currentCount = 0
    # x = None
    # y = None
    currentTurn = RED
    sixCount = 0
    imgList = [None]
    img = None
    img_rect = None
    availableTurns = 1

    def blitDice(SCREEN):
        SCREEN.blit(Dice.img,Dice.img_rect)

    def getDiceNextTurnDimensions():
        Dimensions.DICE_POSITIONS.rotate(-1)
        return  Dimensions.DICE_POSITIONS[0]
    
    def setToNextTurn():
        print("Setting dice to next turn")
        if(Dice.availableTurns):
            return
        else:
            Dice.img = Dice.imgList[6]
            Dice.img_rect.topleft = Dice.getDiceNextTurnDimensions()
            SEQUENCE.rotate(-1)
            Dice.currentTurn = SEQUENCE[0]
            Dice.isRolled = False
            Dice.availableTurns = 1

    def isDiceClicked(mouse_pos):
        if Dice.img_rect.collidepoint(mouse_pos):
            print("Clicked on Dice!")
            return True
        return False
    
    def rollDice(SCREEN):
        print("Rolling dice")
        import pygame
        import time
        count= 0
        for i in range(50):
            count = random.randint(1,6)
            Dice.img = Dice.imgList[count]
            print(Dice.img)
            Dice.blitDice(SCREEN)
            pygame.display.update()
            time.sleep(0.01)
        Dice.currentCount = count
        Dice.isRolled = True
        Dice.availableTurns -= 1
        Dice.sixCount += 1