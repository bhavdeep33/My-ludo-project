from defines import Dimensions
from dice import Dice
from block import HomeBlock

class Player:
    Players = []

    def __init__(self,type,initial_x,initial_y,img,rectImg):
        self.type = type
        self.currentBlock = None
        self.isInsideHome = False
        # self.isOutsideBase = True
        # self.isMovable = False
        self.initial_x = initial_x
        self.initial_y = initial_y
        # self.x = initial_x
        # self.y = initial_y
        # self.width = None
        # self.Height = None
        self.img = rectImg
        self.img_rect = self.img.get_rect()
        self.img_rect.topleft = (initial_x, initial_y)
        self.img = img
        Player.Players.append(self)

    @staticmethod
    def blitPlayers(SCREEN):
        for player in Player.Players:
            SCREEN.blit(player.img,player.img_rect)

    @staticmethod
    def playerClicked(type,mouse_pos):
        for player in Player.Players:
            if(player.type==type and player.img_rect.collidepoint(mouse_pos)):
                    print("Clicked on image!")
                    return player
        return None

    def isMovable(self):
        if self.currentBlock is None:
            if(Dice.currentCount==6):
                return True
            else:
                return False
        else:
            count = Dice.currentCount
            currentBlock = self.currentBlock
            while count!=0 and isinstance(currentBlock,HomeBlock):
                currentBlock = currentBlock.nextBlock(currentBlock.type)
                count -= 1
            return True if count==0 else False
        
    def isMovablePlayersAvailable():
        for player in Player.Players:
            if player.isMovable():
                return True
        return False

    def getPlayers():
        pass

    def adjust():
        pass

    def setDefaultSize():
        pass

    def getKilled():
        Dice.availableTurns += 1

    def movePlayer(self,count):
        from block import StartingPointBlock
        if self.currentBlock is None and count==6:
            targetBlock = StartingPointBlock.getStartingPointBlockFor(self.type)
            self.img_rect.topleft = (targetBlock.x,targetBlock.y)
            self.currentBlock = targetBlock
            targetBlock.havePlayers.append(self)
        #move players by count
        Dice.isRolled = False
