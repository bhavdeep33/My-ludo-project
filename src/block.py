from defines import *

class Block:
    BLOCKS = []

    def __init__(self,type,x,y):
        self.__type = type
        self.__x = x
        self.__y = y
        self.players = []
        self.__next = None
        Block.BLOCKS.append(self)

    def __add__(self,direction):
        xOffset = direction[0]*Dimensions.BLOCKSIZE
        yOffset = direction[1]*Dimensions.BLOCKSIZE
        newBlock = Block.getBlockByDimensions(self.x+xOffset,self.y+yOffset)
        return newBlock
    
    @property
    def type(self):
        return self.__type
    
    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y
    
    @property
    def next(self):
        return self.__next
    
    @next.setter
    def next(self,value):
        self.__next = value
    
    @staticmethod
    def createBlocks(x,y,type):
        if(x,y) in Dimensions.DUMMY_BLOCKS:
            DummyBlock(type,x,y)
        if (x,y) in Dimensions.STARTING_POINT_BLOCKS:
            StartingPointBlock(type,x,y)
        elif (x,y) in Dimensions.SAFE_BLOCKS:
            SafeBlock(type,x,y)
        elif (x,y) in Dimensions.ENTRY_POINT_BLOCKS:
            EntryPointBlock(type,x,y)
        elif (x,y) in Dimensions.HOME_BLOCKS:
            HomeBlock(type,x,y)
        else:
            Block(type,x,y)

    @staticmethod
    def getBlockByDimensions(x,y):
        for block in Block.BLOCKS:
            if(block.x == x and block.y == y):
                return block
        return None
    
    def nextBlock(self,playerType):
        if(isinstance(self,EntryPointBlock) and playerType==self.type):
            return self.nextHomeBlock
        else:
            return self.next
    
    def isSafe(self):
        if(isinstance(self,SafeBlock) or len(self.players)>3):
            return True
        else:
            return False
    
    def getPlayersByType(self,type):
        players = []
        for player in self.players:
            if player.type == type:
                players.append(player)
        return players

class SafeBlock(Block):
    def __init__(self, type, x, y):
        super().__init__(type, x, y)

class StartingPointBlock(SafeBlock):
    StartingPointBlocks = []
    def __init__(self, type, x, y):
        super().__init__(type, x, y)
        StartingPointBlock.StartingPointBlocks.append(self)
    
    @staticmethod
    def getStartingPointBlockFor(type):
        for block in StartingPointBlock.StartingPointBlocks:
            if block.type == type:
                return block

class EntryPointBlock(Block):
    def __init__(self, type, x, y):
        super().__init__(type, x, y)
        self.nextHomeBlock = None

    def isEntryPointFor(self,type):
        if(self.type==type):
            return True
        return False

class HomeBlock(SafeBlock):
    def __init__(self, type, x, y):
        super().__init__(type, x, y)
    
class DummyBlock(Block):
    def __init__(self, type, x, y):
        super().__init__(type, x, y)