# Import #
import pygame
import random
import time
# Rules List #
rules = '''
        1. Any live cell with fewer than two live neighbours dies, as if caused by under-population.
        2. Any live cell with two or three live neighbours lives on to the next generation.
        3. Any live cell with more than three live neighbours dies, as if by overcrowding.
        4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
        '''

# Constants #
gridSize = 100
size = 10
FPS = 100
WIDTH,HEIGHT = 1000,1000
generation = 0
count = 0

# 2D Board #
board = [[False for i in range(gridSize)] for j in range(gridSize)]

# Colors #
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (211, 211, 211)
coolGrey = (130,130,130)
RED = (255,0,0)

# Pygame Setup #
pygame.init()
font = pygame.font.SysFont("Ariel Black",30)
typeFont = pygame.font.SysFont("Ariel Black",20)
screen = pygame.display.set_mode((WIDTH,HEIGHT)) # Define the surface for the simulation to run on
pygame.display.set_caption('Conway\'s Game of Life')
smallGlide = font.render('Small glider', False, (0, 0, 0))

screen.fill(WHITE) # Fill the screen white
pygame.display.update()
clock = pygame.time.Clock()

saveShapeText=''

loadShapeText=''

name=''

saveShapeBool=False
saveTypeBox=pygame.Rect(450,450,100,50)
loadShapeBool=False
loadTypeBox=pygame.Rect(450,450,100,50)


typing=False


# Coordinates #
initialCoord = None
timer=0


# Preset Menu #
extendo = False # Pullout menu starts closed
smallGlider = False # Drag/Dropping smallGlider
gliderGun = False

# Mouse Position #
def mousePos():
    x, y = pygame.mouse.get_pos()
    return (x//10, y//10)

# Find Live Neighbours #
def findNeighbors(row, column):
    alive = 0
    
    # Horizontally adjacent #
    if row > 0:
        if board[row-1][column]:
            alive += 1
    if column > 0:
        if board[row][column-1]:
            alive += 1
    if row < gridSize-1:
        if board[row+1][column]:
            alive += 1
    if column < gridSize-1:
        if board[row][column+1]:
            alive += 1

    # Diagonally adjacent #
    if row > 0 and column > 0:
        if board[row-1][column-1]:
            alive += 1
    if row < gridSize-1 and column < gridSize-1:
        if board[row+1][column+1]:
            alive += 1
    if row > 0 and column < gridSize-1:
        if board[row-1][column+1]:
            alive += 1
    if row < gridSize-1 and column > 0:
        if board[row+1][column-1]:
            alive += 1

    # Return the final count (0-8)
    return alive

# Activate a Grid Space #
def giveLife(row, col):
    board[row][col] = True

# Deactivate a Grid Space #
def killRuthlessly(row, col):
    board[row][col] = False

# Draw Temporary Rectangle #
def drawTempRect(row,col):
    pygame.draw.rect(screen,coolGrey, (row*10,col*10,size,size),0)

# Shape Preset - Small Glider #
def drawSmallGlider(row,col):
    global smallGlider
    drawTempRect(row,col)
    drawTempRect(row-1,col)
    drawTempRect(row-2,col)
    drawTempRect(row,col-1)
    drawTempRect(row-1,col-2)
    if click[0]:
        giveLife(row,col)
        giveLife(row-1,col)
        giveLife(row-2,col)
        giveLife(row,col-1)
        giveLife(row-1,col-2)
    if click[2]:
        smallGlider = False

def drawGliderGun(row,col):
    global gliderGun
    drawTempRect(row,col)
    drawTempRect(row+1,col)
    drawTempRect(row,col-1)
    drawTempRect(row+1,col-1)
    drawTempRect(row+10,col)
    drawTempRect(row+10,col+1)
    drawTempRect(row+10,col-1)
    drawTempRect(row+11,col-2)
    drawTempRect(row+11,col+2)
    drawTempRect(row+12,col+3)
    drawTempRect(row+12,col-3)
    drawTempRect(row+13,col+3)
    drawTempRect(row+13,col-3)
    drawTempRect(row+14,col)
    drawTempRect(row+16,col)
    drawTempRect(row+17,col)
    drawTempRect(row+16,col+1)
    drawTempRect(row+16,col-1)
    drawTempRect(row+15,col+2)
    drawTempRect(row+15,col-2)
    drawTempRect(row+20,col-1)
    drawTempRect(row+20,col-2)
    drawTempRect(row+20,col-3)
    drawTempRect(row+21,col-1)
    drawTempRect(row+21,col-2)
    drawTempRect(row+21,col-3)
    drawTempRect(row+22,col)
    drawTempRect(row+22,col-4)
    drawTempRect(row+24,col)
    drawTempRect(row+24,col+1)
    drawTempRect(row+24,col-4)
    drawTempRect(row+24,col-5)
    drawTempRect(row+34,col-2)
    drawTempRect(row+34,col-3)
    drawTempRect(row+35,col-2)
    drawTempRect(row+35,col-3)
    

    if click[0] and mouseX<65 and mouseY<97:
        giveLife(row,col)
        giveLife(row+1,col)
        giveLife(row,col-1)
        giveLife(row+1,col-1)
        giveLife(row+10,col)
        giveLife(row+10,col+1)
        giveLife(row+10,col-1)
        giveLife(row+11,col-2)
        giveLife(row+11,col+2)
        giveLife(row+12,col+3)
        giveLife(row+12,col-3)
        giveLife(row+13,col+3)
        giveLife(row+13,col-3)
        giveLife(row+14,col)
        giveLife(row+16,col)
        giveLife(row+17,col)
        giveLife(row+16,col+1)
        giveLife(row+16,col-1)
        giveLife(row+15,col+2)
        giveLife(row+15,col-2)
        giveLife(row+20,col-1)
        giveLife(row+20,col-2)
        giveLife(row+20,col-3)
        giveLife(row+21,col-1)
        giveLife(row+21,col-2)
        giveLife(row+21,col-3)
        giveLife(row+22,col)
        giveLife(row+22,col-4)
        giveLife(row+24,col)
        giveLife(row+24,col+1)
        giveLife(row+24,col-4)
        giveLife(row+24,col-5)
        giveLife(row+34,col-2)
        giveLife(row+34,col-3)
        giveLife(row+35,col-2)
        giveLife(row+35,col-3)
    elif click[0] and mouseX>65 or mouseY>=97:
        killRuthlessly(row,col)
        
    if click[2]:
        gliderGun = False
    
# Setup GUI #
def checkGui(mouseX,mouseY):
    global extendo,smallGlider,gliderGun
    if (mouseX > 97 and mouseY>40 and mouseY<49):
        extendo = True
    if extendo == True:
        if (mouseX>82 and mouseX<98 and mouseY > 2 and mouseY <18):
            smallGlider = True

        if (mouseX>82 and mouseX<98 and mouseY > 20 and mouseY <36):
            gliderGun = True
            
        if mouseX>77 and click[0]:
            killRuthlessly(mouseX,mouseY)
        
        if mouseX>77 and mouseX<80 and mouseY>40 and mouseY<49:
            extendo=False
        
# Display GUI #
def drawGui():
    global extendo
    if extendo == True:
        pygame.draw.rect(screen,coolGrey,(800,0,200,HEIGHT),0)
        pygame.draw.rect(screen,BLACK,(800,1,199,HEIGHT-2),3)
        pygame.draw.rect(screen,WHITE,(820,20,160,160),0)
        pygame.draw.rect(screen,WHITE,(820,200,160,160),0)
        pygame.draw.rect(screen,WHITE,(820,380,160,160),0)
        pygame.draw.rect(screen,WHITE,(820,560,160,160),0)
        pygame.draw.rect(screen,BLACK,(777,402,24,86),0)
        pygame.draw.rect(screen,coolGrey,(780,405,19,80),0)
        pygame.draw.polygon(screen,WHITE,[(785,419),(785,429),(795,424)],0)
        pygame.draw.polygon(screen,WHITE,[(785,439),(785,449),(795,444)],0)
        pygame.draw.polygon(screen,WHITE,[(785,459),(785,469),(795,464)],0)
        screen.blit(smallGlide,(820,25))
    else:
        pygame.draw.rect(screen,BLACK,(980,405,50,80),3)
        pygame.draw.rect(screen,coolGrey,(980,405,50,80),0)
        pygame.draw.polygon(screen,WHITE,[(995,419),(995,429),(985,424)],0)
        pygame.draw.polygon(screen,WHITE,[(995,439),(995,449),(985,444)],0)
        pygame.draw.polygon(screen,WHITE,[(995,459),(995,469),(985,464)],0)

# Display Text #
def drawText(message,text_X,text_Y):
    text = font.render(message, 1, BLACK) # put the font and the message together
    screen.blit(text,(text_X,text_Y))

# Display Grid #
def draw_grid():
    for i in range(0,WIDTH,size):
        pygame.draw.line(screen,GREY,(i,0),(i,HEIGHT),1)
    for i in range(0,HEIGHT,size):
        pygame.draw.line(screen,GREY,(0,i),(WIDTH,i),1)

# Save Grid File #
def save_grid():
    if run == False:
        saveGridBool=True
        typing=True
        file_out = open('map','w')
        for i in range(len(board)):
            for j in range(len(board[i])):
                file_out.write(str(board[i][j])+' ')
            file_out.write('\n')
        file_out.close()

# Load Grid File #
def load_grid():
    if run == False:
        loadGridBool=True
        typing=True
        newlst=[]
        file_in = open('map','r')
        lines = file_in.readlines()
        for line in lines:
            line = line.split()
            newlst.append([True if word == 'True' else False for word in line])
        file_in.close()
        return newlst

# Enable Drag and Drop #
def dragdrop(inital,x,y):
    startx,starty = inital
    pygame.draw.polygon(screen,(255,0,0),((startx*10, starty*10), (startx*10,y*10),(x*10,y*10),(x*10,starty*10)),3)


# Save Shape File #
def save_shape(name,startx,starty,x,y):
    print('*'*100)
    file_out = open(name,'w')
    for i in range(len(board)):
        for j in range(len(board[i])):
            if (starty <= j <= y) and (startx <= i <= x):
                file_out.write(str(board[i][j])+' ')
        file_out.write('\n')
    file_out.close()
    
# Load Shape File #
def load_shape(name):
    newlst=[]
    file_in = open(name,'r')
    lines = file_in.readlines()
    for line in lines:
        line = line.split()
        newlst.append([True if word == 'True' else False for word in line])
    file_in.close()
    list2=[x for x in newlst if x!= []]
    return list2


# Main Loop #
genCount = 0
mouse_mode=True
run = False

while True:
    mouseX,mouseY = mousePos()
    # Draw the board as rectangles #
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col]:
                pygame.draw.rect(screen, BLACK, (row*10,col*10,size,size),0)
            if not board[row][col]:
                pygame.draw.rect(screen, WHITE, (row*10,col*10,size,size),0)
                
    # Process Events #    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                break

            if typing == True:
                    
                if loadShapeBool:
                    name=loadShapeText
                    
                if saveShapeBool:
                    name=saveShapeText
                    
                if event.unicode.isalpha() or event.unicode.isdigit():
                    name+=event.unicode
                elif event.key == pygame.K_BACKSPACE:
                    name=name[:-1]
                elif event.key == pygame.K_RETURN:
                    typing=False
                
                if loadShapeBool:
                    loadShapeText=name
                    
                if saveShapeBool:
                    saveShapeText=name
                    
               
            if typing ==False:
                # Run #
                if event.key == pygame.K_SPACE:
                    run = not run
                    
                # Save #
                if event.key == pygame.K_s:
                    save_grid()
                    
                # Load Grid #
                if event.key == pygame.K_l:
                    newlst = load_grid()
                    board=newlst
                    
                if event.key == pygame.K_f:
                    mouse_mode = not mouse_mode
                    
                # Load Shape #
                if event.key == pygame.K_k:
                    loadShapeBool=True
                    typing=True
                    
                    
                # Clear Screen #
                if event.key == pygame.K_c:
                    if run == True:
                        run = not run
                    generation = 0
                    board = [[False for i in range(gridSize)] for j in range(gridSize)]
                    
                # Random #
                if event.key == pygame.K_r:
                    generation = 0
                    possibilities = [False, False, True]
                    for row in range(gridSize):
                        for col in range(gridSize):
                            board[row][col] = random.choice(possibilities)


                
                                    
                        
                # Next Generation #
                if event.key == pygame.K_RIGHT:
                    tempboard = [[False for i in range(gridSize)] for j in range(gridSize)]
                    for row in range(len(board)):
                        for col in range(len(board)):
                            neighborcount = findNeighbors(row, col)
                            if board[row][col]: #any live cell
                                if neighborcount < 2:
                                    tempboard[row][col] = False #dies
                                if neighborcount > 3: #With more than three live neighbors
                                    tempboard[row][col] = False #dies
                                if neighborcount == 2 or neighborcount == 3:
                                    tempboard[row][col] = True #lives on to the next generation 
                            elif not board[row][col]: #any dead cell
                                if neighborcount == 3: #with exactly three live neighbors
                                    tempboard[row][col] = True #becomes a live cell
                    board = tempboard
                    generation += 1
                    run = False
                    
                

    # Rules #
    if run:
        tempboard = [[False for i in range(gridSize)] for j in range(gridSize)]
        for row in range(len(board)):
            for col in range(len(board)):
                neighborcount = findNeighbors(row, col)
                if board[row][col]: #any live cell
                    if neighborcount < 2:
                        tempboard[row][col] = False #dies
                    if neighborcount > 3: #With more than three live neighbors
                        tempboard[row][col] = False #dies
                    if neighborcount == 2 or neighborcount == 3:
                        tempboard[row][col] = True #lives on to the next generation 
                elif not board[row][col]: #any dead cell
                    if neighborcount == 3: #with exactly three live neighbors
                        tempboard[row][col] = True #becomes a live cell
        board = tempboard
        generation += 1
        genCount = 1

    # User Input (Drawing) #
    
    click = pygame.mouse.get_pressed()
    if mouse_mode:
        if click[0]:
            mouseX,mouseY = mousePos()
            board[mouseX][mouseY] = True
            checkGui(mouseX,mouseY)
            if not run:
                generation = 0
        if click[2]:
            mouseX,mouseY = mousePos()
            board[mouseX][mouseY] = False
            if not run:
                generation = 0
                
    if not mouse_mode:
            if click[0]:
                mouseX,mouseY = mousePos()
                if initialCoord == None:
                    initialCoord = (mouseX,mouseY)
                dragdrop(initialCoord,mouseX,mouseY)
            else:
                if initialCoord != None:
                    saveShapeBool=True
                    typing=True
                    run=False
                    print(saveShapeBool,typing)
                    initialCoord2 = initialCoord
                    initialCoord = None
                    
    if saveShapeBool == True and typing == False:
        run=False
        startx,starty = initialCoord2
        save_shape(saveShapeText,startx,starty,mouseX,mouseY)
        saveShapeBool=False
        run=False
                        

    if loadShapeBool==True and typing==False:
        try:
            list2=load_shape(loadShapeText)
            if mouseX<(100-(len(list2))) and mouseY<(100-(len(list2[0]))):
                for x in range(mouseX, mouseX+len(list2)):
                    for y in range(mouseY,mouseY+len(list2[0])):
                        if list2[x-mouseX][y-mouseY] == True:
                            giveLife(x,y)
        except:
            errorMsg=('Name does not exist!')
            drawText(errorMsg,400,450)
            pygame.display.update()
            pygame.time.delay(800)
        loadShapeBool=False
        run=False

    # Redraw Screen #
    
    draw_grid()
    drawGui()
    if smallGlider:
        drawSmallGlider(mouseX,mouseY)
        
    if gliderGun:
        drawGliderGun(mouseX,mouseY)
        
    message=('Generation: '+str(generation))
    drawText(message,10,10)
    if not mouse_mode:
        mode=('Selection Mode')
        drawText(mode,10,40)
        
    if saveShapeBool:
        pygame.draw.rect(screen,WHITE,saveTypeBox)
        saveType = typeFont.render(saveShapeText, False, (0, 0, 0))
        screen.blit(saveType,[450,450])

    if loadShapeBool:
        pygame.draw.rect(screen,WHITE,loadTypeBox)
        loadType = typeFont.render(loadShapeText, False, (0, 0, 0))
        screen.blit(loadType,[450,450])
   
    pygame.display.update()
