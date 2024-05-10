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
                        playerClicked.movePlayer(Dice.currentCount,game)

                        if playerClicked.canKill():
                            playerClicked.currentBlock.players[0].getKilled(game)

                else:
                    if(Dice.isDiceClicked(mouse_pos)):
                        Dice.rollDice(game.SCREEN)
                        if Dice.gotThreeSixInRow():
                            Dice.setToNextTurn()
                        else:    
                            movablePlayers = Player.movablePlayersAvailable()
                            if not movablePlayers:
                                Dice.setToNextTurn()

                            elif len(movablePlayers)==1:
                                player = movablePlayers[0]
                                player.movePlayer(Dice.currentCount,game)
                                if player.canKill():
                                    player.currentBlock.players[0].getKilled(game)
                   
        if Dice.availableTurns==0:
            Dice.setToNextTurn()
                
        game.blitObjects()
        
    pygame.quit()