def initBlocks(self):
    B = BLOCKSIZE
    #Creating red blocks
    for i in range(3):
        y = RED_PLAYBASE.Y + i*BLOCKSIZE
        for j in range(7):
            x = RED_PLAYBASE.X + j*BLOCKSIZE
            if(i==0 and j==1):
                Block(RED,x,y,isSafeBlock=True,isEntryPointFor=True)
            elif(i==2 and j==2):
                Block(RED,x,y,isSafeBlock=True)
            elif(i==1 and j==0):
                Block(RED,x,y,isHomeEntry=True)
            elif(i==1 and j==6):
                Block(RED,x,y,isHomeBlock=True)
            else:
                Block(RED,x,y)

    for i in range(7):
        y = 2*b + i*b
        for j in range(3):
            x = 6*b + j*b
            if(i==1 and j==2):
                Block(GREEN,x,y,isSafeBlock=True,isEntryPointFor=True)
            elif(i==2 and j==0):
                Block(GREEN,x,y,isSafeBlock=True)
            elif(i==0 and j==1):
                Block(GREEN,x,y,isHomeEntry=True)
            elif(i==6 and j==1):
                Block(GREEN,x,y,isHomeBlock=True)
            else:
                Block(GREEN,x,y)

    for i in range(3):
        y = 8*b + i*b
        for j in range(7):
            x = 8*b + j*b
            if(i==2 and j==5):
                Block(YELLOW,x,y,isSafeBlock=True,isEntryPointFor=True)
            elif(i==0 and j==4):
                Block(YELLOW,x,y,isSafeBlock=True)
            elif(i==1 and j==6):
                Block(YELLOW,x,y,isHomeEntry=True)
            elif(i==1 and j==0):
                Block(YELLOW,x,y,isHomeBlock=True)
            else:
                Block(YELLOW,x,y)
    
    for i in range(7):
        y = 10*b + i*b
        for j in range(3):
            x = 6*b + j*b
            if(i==5 and j==0):
                Block(BLUE,x,y,isSafeBlock=True,isEntryPointFor=True)
            elif(i==4 and j==2):
                Block(BLUE,x,y,isSafeBlock=True)
            elif(i==6 and j==1):
                Block(BLUE,x,y,isHomeEntry=True)
            elif(i==0 and j==1):
                Block(BLUE,x,y,isHomeBlock=True)
            else:
                Block(BLUE,x,y)
 