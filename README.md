# My-ludo-project

This is a ludo game project created in python with pygame and help of other supporting python libraries. 
Apart from building just a game, this project also focuses on implementing core python concepts. This project contains almost all features which typical ludo game have. 

So, let's Dive into the world of PyLudo and experience the joy of rolling the dice, moving your tokens, and competing against friends!

## Game features:

Just like typical ludo game, this project include following features:
- Rolling dice and moving players
- Killing other players
- Auto detecting movable players according to dice count and auto moving players
- Grouping players if more than one players are in same block
- Popping up movable players when dice is rolled
- Displaying game over window when game is over and allowing user to replay the game if he wants to play again
- Other basic features

## Python concepts covered:

Apart from gaming it covers almost all core python concepts which is helpful in understanding the practical implementation of each concepts. Below are the major concepts which are covered in this project:
 - Project structure
 - Basic concepts like control statements, loops,functions and lists etc.
 - Reading files and working with ini files
 - Basic use of deque data structure
 - Working with python libraries like pygame,tkinter, random, time, PIL
 - Core oops concepts like:
     - Creating and destroying objects
     - Use of abstraction by creating constructors and object methods
     - Use of encapsulation by making critical variables private 
     - Using getters and setters for private variables
     - Use of single and multilevel inheritance for representing different types of ludo blocks
     - Use of different types of methods like object methods, static methods and class methods
     - Operator overloading
     
## Project overview:

### 1. /Bin:
- This folder contains the final exe file for our project which allow us to run our game on any system without python installed.

### 2. /Config:
- This folder contains the configuration file for our project. We are free to configure screen dimentions and game caption by modifying this file.

### 3. /Images: 
- This folder contains all necessary PNGs which are required for our game.

### 4. /Sounds: 
- THis folder contains all game sound effects which will be played during game.

### 5. /src: 
- This folder contains our source code of game. we have divided this source code in 6 different files to well define our code structure and to avoid complexity in our code.
- Each of these file deals with different sections of games.

    **defines.py**
    
    - Our ludo game has various components which needs to be defined or calculate manually and cannot be programmed. For example, size of each block, size of player etc will have to be defined manually and  Safe block positions,Home block positions, Initial player positions, moving directions, Each block positions, etc will have to be calculated manually. This file contains all of this defining and calculative stuff to directly use these variables in other files avoid complexity in other files.
    
    **app.py**
    
    - This is the driver file of our game and from this file our game begins to run. This file imports classes and methods from other files which provides easy way to drive our game without any complexity.
    
    **initialize.py**
    
     - This is the file which represents our game. This file have class named Game which is responsible for initializing our game by creating game window, initializing players, Dice, Sounds etc. It also prompts when game is over and restarts the game if user wants to play again.
    
    **block.py**
    
     - This file deals with blocks and contains the block class which contains all block objects present in our game. Each block object contains all information about that block like type of block(red,green,yellow,blue), block's x and y coordinates, players which is present at that block, pointer to the next block etc. 
     
     - This block class also contains methods related to the blocks like getting next block, if block is safe or not, get players by type on particular block etc.
    
    **dice.py**
    
     - This file deals with dice and contains the dice class which contains information about dice's current state like,if dice is rolled or not, Dice's current count, current turn etc. This class also have some static methods like setting dice to next turn, rolling dice, checking if player got three times in row etc.
    
    **player.py**
     - This file deals with the core component of the game which are players. It contains the player class which contains all the player objects present in our game. Each player object contains all information about that player like type of player, current block, current coordinates, initial position etc. 
     - Player class also contains methods related to the players like getting players by type, blitting players, getting movable players, grouping players, popping movable players, killing players, moving players etc.
