import configparser
from collections import deque
import os 

os.chdir("D:/Desktop/My work/prj")

config = configparser.ConfigParser()
config.read('config/config.ini')

EXITGAME = False
RESTARTGAME = True
RED = "Red"
BLUE = "Blue"
GREEN = "Green"
YELLOW = "Yellow"
DUMMY = "Dummy"
CAPTION = config['caption']['caption']
INITIAL_DICE_COUNT = 6

class Directions:
    RIGHT = (1,0)
    LEFT = (-1,0)
    UP = (0,-1)
    DOWN = (0,1)
    RIGHTUP = (1,-1)
    RIGHTDOWN = (1,1)
    LEFTUP = (-1,-1)
    LEFTDOWN = (-1,1)

    @staticmethod
    def getNextDirection(direction):
        nextdirection  = {Directions.RIGHT:Directions.DOWN,
                          Directions.DOWN:Directions.LEFT,
                          Directions.LEFT:Directions.UP,
                          Directions.UP:Directions.RIGHT,
                          Directions.RIGHTUP:Directions.UP,
                          Directions.RIGHTDOWN:Directions.RIGHT,
                          Directions.LEFTUP:Directions.LEFT,
                          Directions.LEFTDOWN:Directions.DOWN,
                         }
        return nextdirection[direction]

    @staticmethod
    def getNextCornerBlockDirection(direction):
        cornerBlockDirection  = {Directions.RIGHT:Directions.RIGHTUP,
                                 Directions.DOWN:Directions.RIGHTDOWN,
                                 Directions.LEFT:Directions.LEFTDOWN,
                                 Directions.UP:Directions.LEFTUP
                                }
        return cornerBlockDirection[direction]

    @staticmethod
    def defineMovingDirections():
        from block import Block,DummyBlock,EntryPointBlock,HomeBlock
        B = Dimensions.BLOCKSIZE
        currentDirection = Directions.RIGHT
        currentBlock = Block.getBlockByDimensions(0,8*B)
        
        while not currentBlock.next:
            nextBlock = currentBlock + currentDirection
            if nextBlock:
                if isinstance(nextBlock,DummyBlock):
                    cornerBlockDirection = Directions.getNextCornerBlockDirection(currentDirection)
                    currentBlock.next = currentBlock + cornerBlockDirection
                    currentDirection = Directions.getNextDirection(cornerBlockDirection)
                else:
                    currentBlock.next = currentBlock + currentDirection
            else:
                currentDirection = Directions.getNextDirection(currentDirection)
                currentBlock.next = currentBlock + currentDirection

            if isinstance(currentBlock,EntryPointBlock):
                homeDirection = Directions.getNextDirection(currentDirection)
                currentBlock.nextHomeBlock = currentBlock+homeDirection
                newCurrentBlock = currentBlock.nextHomeBlock
                while not isinstance(newCurrentBlock,HomeBlock):
                    newCurrentBlock.next = newCurrentBlock + homeDirection
                    newCurrentBlock = newCurrentBlock.next

            currentBlock = currentBlock.next
     
class Dimensions:
    BLOCKSINROW = 15
    BLOCKSINCOLUMN = 19
    SCREENHEIGHT = int(config['screenDimentions']['height'])
    SCREENWIDTH = int(config['screenDimentions']['width'])
    BLOCKSIZE = SCREENWIDTH/BLOCKSINROW
    B = BLOCKSIZE
    PLAYERWIDTH = BLOCKSIZE
    PLAYERHEIGHT = 1.5*BLOCKSIZE
    DICEHEIGHT = 2*BLOCKSIZE
    DICEWIDTH = 2*BLOCKSIZE
    BANNERWIDTH = 11*BLOCKSIZE
    BANNERHEIGHT = 2*BLOCKSIZE

    class Object:
        def __init__(self,x,y):
            self.X = x
            self.Y = y
            
    RED_PLAYBASE = Object(0,8*B)
    GREEN_PLAYBASE = Object(6*B,2*B)
    YELLOW_PLAYBASE = Object(9*B,8*B)
    BLUE_PLAYBASE = Object(6*B,11*B)

    STARTING_POINT_BLOCKS = [None,None,None,None]
    STARTING_POINT_BLOCKS[0] = (RED_PLAYBASE.X + B, RED_PLAYBASE.Y)
    STARTING_POINT_BLOCKS[1] = (GREEN_PLAYBASE.X + 2*B, GREEN_PLAYBASE.Y + B)
    STARTING_POINT_BLOCKS[2] = (YELLOW_PLAYBASE.X + 4*B, YELLOW_PLAYBASE.Y + 2*B)
    STARTING_POINT_BLOCKS[3] = (BLUE_PLAYBASE.X , BLUE_PLAYBASE.Y + 4*B)

    SAFE_BLOCKS = [None,None,None,None]
    SAFE_BLOCKS[0] = (RED_PLAYBASE.X + 2*B, RED_PLAYBASE.Y + 2*B)
    SAFE_BLOCKS[1] = (GREEN_PLAYBASE.X , GREEN_PLAYBASE.Y + 2*B)
    SAFE_BLOCKS[2] = (YELLOW_PLAYBASE.X + 3*B, YELLOW_PLAYBASE.Y)
    SAFE_BLOCKS[3] = (BLUE_PLAYBASE.X + 2*B, BLUE_PLAYBASE.Y + 3*B)

    ENTRY_POINT_BLOCKS = [None,None,None,None]
    ENTRY_POINT_BLOCKS[0] = (RED_PLAYBASE.X , RED_PLAYBASE.Y + B)
    ENTRY_POINT_BLOCKS[1] = (GREEN_PLAYBASE.X + B, GREEN_PLAYBASE.Y)
    ENTRY_POINT_BLOCKS[2] = (YELLOW_PLAYBASE.X + 5*B, YELLOW_PLAYBASE.Y + B)
    ENTRY_POINT_BLOCKS[3] = (BLUE_PLAYBASE.X + B, BLUE_PLAYBASE.Y + 5*B)

    HOME_BLOCKS = [None,None,None,None]
    HOME_BLOCKS[0] = (RED_PLAYBASE.X + 6*B , RED_PLAYBASE.Y + B)
    HOME_BLOCKS[1] = (GREEN_PLAYBASE.X + B, GREEN_PLAYBASE.Y + 6*B)
    HOME_BLOCKS[2] = (YELLOW_PLAYBASE.X - B, YELLOW_PLAYBASE.Y + B)
    HOME_BLOCKS[3] = (BLUE_PLAYBASE.X + B, BLUE_PLAYBASE.Y - B)

    DUMMY_BLOCKS = [None,None,None,None]
    DUMMY_BLOCKS[0] = (RED_PLAYBASE.X + 6*B , RED_PLAYBASE.Y)
    DUMMY_BLOCKS[1] = (GREEN_PLAYBASE.X + 2*B, GREEN_PLAYBASE.Y + 6*B)
    DUMMY_BLOCKS[2] = (YELLOW_PLAYBASE.X - B, YELLOW_PLAYBASE.Y + 2*B)
    DUMMY_BLOCKS[3] = (BLUE_PLAYBASE.X, BLUE_PLAYBASE.Y - B)

    PLAYERS_INITIAL_RECT_POS = [(RED,1.5*B,3.3*B),(GREEN,10.5*B,3.3*B),(YELLOW,10.5*B,12.3*B),(BLUE,1.5*B,12.3*B)]
    PLAYERS_INITIAL_POS_SPACINGS = 2*B
    POP_PLAYERS_SPACING = 0.3*B
    dicePositions = deque([(0,0),(SCREENWIDTH-2*B,0),(SCREENWIDTH-2*B,SCREENHEIGHT-2*B),(0,SCREENHEIGHT-2*B)])
    BANNER_POS = [(2*B,0),(2*B,SCREENHEIGHT-2*B)]

    @staticmethod
    def defineBlockDimensions():
        from block import Block
        B = Dimensions.BLOCKSIZE
        for i in range(3):
            y = Dimensions.RED_PLAYBASE.Y + i*B
            for j in range(7):
                x = Dimensions.RED_PLAYBASE.X + j*B
                Block.createBlocks(x,y,RED)

        for i in range(7):
            y = Dimensions.GREEN_PLAYBASE.Y + i*B
            for j in range(3):
                x = Dimensions.GREEN_PLAYBASE.X + j*B
                Block.createBlocks(x,y,GREEN)

        for i in range(3):
            y = Dimensions.YELLOW_PLAYBASE.Y + i*B
            for j in range(7):
                x = Dimensions.YELLOW_PLAYBASE.X + (j-1)*B
                Block.createBlocks(x,y,YELLOW)

        for i in range(7):
            y = Dimensions.BLUE_PLAYBASE.Y + (i-1)*B
            for j in range(3):
                x = Dimensions.BLUE_PLAYBASE.X + j*B
                Block.createBlocks(x,y,BLUE)

        Directions.defineMovingDirections()