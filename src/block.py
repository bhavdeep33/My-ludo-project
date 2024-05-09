from defines import *

class Block:
    Blocks = []
    def __init__(self,type,x,y):
        self.type = type
        self.x = x
        self.y = y
        self.havePlayers = []
        self.next = None
        Block.Blocks.append(self)

    def getSafeBlocks():
        pass

    def getHomeEntryBlocks():
        pass
    
    def getHomeBlocks():
        pass

    def addPlayers():
        pass

    def removePlayers():
        pass
    
    def __add__(self,direction):
        xOffset = direction[0]*Dimensions.BLOCKSIZE
        yOffset = direction[1]*Dimensions.BLOCKSIZE
        newBlock = Block.getBlockByDimensions(self.x+xOffset,self.y+yOffset)
        return newBlock

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
        for block in Block.Blocks:
            if(block.x == x and block.y == y):
                return block
        return None
    
    def nextBlock(self,playerType):
        if(isinstance(self,EntryPointBlock) and playerType==self.type):
            return self.nextHomeBlock
        else:
            return self.next
    
    def isSafe(self):
        if(isinstance(self,SafeBlock) or len(self.havePlayers)>2):
            return True
        else:
            return False

class SafeBlock(Block):
    def __init__(self, type, x, y):
        super().__init__(type, x, y)

class StartingPointBlock(SafeBlock):
    StartingPointBlocks = []
    def __init__(self, type, x, y):
        super().__init__(type, x, y)
        StartingPointBlock.StartingPointBlocks.append(self)
    
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