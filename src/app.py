from initialize import Game
from player import Player
from dice import Dice
import pygame
from defines import *

if __name__ == "__main__":
    
    game = Game()

    while not game.exitGame:
        for event in pygame.event.get():  # For Loop
            if event.type == pygame.QUIT:
                game.exitGame = True

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if(Dice.isRolled):
                    playerClicked = Player.playerClicked(Dice.currentTurn,mouse_pos)
                    if(playerClicked and playerClicked.isMovable()):
                        #print("Player is movable")
                        playerClicked.movePlayer(Dice.currentCount,game)

                        currentBlock = playerClicked.currentBlock
                        if currentBlock.havePlayers and not currentBlock.isSafe():
                            currentBlock.havePlayers[0].getKilled()
                        else:
                            pass
                            #print("Player is safe")
                        
                        Dice.setToNextTurn()
                else:
                    if(Dice.isDiceClicked(mouse_pos)):
                        Dice.rollDice(game.SCREEN)
                        if Dice.sixCount<3:
                           Dice.availableTurns+=1
                        else:
                            Dice.setToNextTurn()
        
        if(Dice.isRolled):
            if not Player.isMovablePlayersAvailable():
                #print("No movable players are available")
                Dice.setToNextTurn()
        game.blitObjects()
        
    pygame.quit()