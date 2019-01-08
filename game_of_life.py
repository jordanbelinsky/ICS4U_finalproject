# Import #
import pygame
import random

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
screen = pygame.display.set_mode((WIDTH,HEIGHT)) # Define the surface for the simulation to run on
pygame.display.set_caption('Conway\'s Game of Life')
smallGlide = font.render('Small glider', False, (0, 0, 0))
screen.fill(WHITE) # Fill the screen white
pygame.display.update()
clock = pygame.time.Clock()

# Coordinates #
initialCoord = None
timer=0
text_X = 10                     
text_Y = 10

# Preset Menu #
extendo = False # Pullout menu starts closed
smallGlider = False # Drag/Dropping smallGlider

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

# Setup GUI #
def checkGui(mouseX,mouseY):
    global extendo,smallGlider
    if (mouseX > 97 and mouseY>40 and mouseY<49):
        extendo = True
    if extendo == True:
        if (mouseX>82 and mouseX<98 and mouseY > 2 and mouseY <18):
            smallGlider = True
            
        if mouseX>77:
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
def drawText(message):
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
        #name=input("Enter the name of the file you want to save")
        file_out = open('map','w')
        for i in range(len(board)):
            for j in range(len(board[i])):
                file_out.write(str(board[i][j])+' ')
            file_out.write('\n')
        file_out.close()

# Load Grid File #
def load_grid():
    if run == False:
        #fname=input("Enter the filename of the map you'd like to open")
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
    print(str(startx)+' '+str(starty)+' '+str(x)+' '+str(y))
    pygame.draw.polygon(screen,RED,((startx*10, starty*10), (startx*10,y*10),(x*10,y*10),(x*10,starty*10)),3)

# Save Shape File #
def save_shape(startx,starty,x,y):
    if run == False:
        #name=input("Enter the name of the file you want to save")
        file_out = open('shape','w')
        for i in range(len(board)):
            for j in range(len(board[i])):
                if (starty <= i <= y) and (startx <= j <= x):
                    file_out.write(str(board[i][j])+' ')
            file_out.write('\n')
        file_out.close()

# Load Shape File #
def load_shape():
    if run == False:
        #fname=input("Enter the filename of the map you'd like to open")
        newlst=[]
        file_in = open('shape','r')
        lines = file_in.readlines()
        for line in lines:
            line = line.split()
            newlst.append([True if word == 'True' else False for word in line])
        file_in.close()
        return newlst

# Place Spaceship #
def place_spaceship():
    pass

# Place Oscillator #
def place_oscillator():
    pass

# Place StillLife #
def place_stillLife():
    pass

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
            # Run #
            if event.key == pygame.K_RETURN:
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
                newlst=load_shape()
            # Next Generation #
            if event.key == pygame.K_RIGHT:
                for x in range(1):
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
                startx,starty = initialCoord
                save_shape(startx,starty,mouseX,mouseY)
            initialCoord = None

    # Redraw Screen #
    draw_grid()
    drawGui()
    if smallGlider:
        drawSmallGlider(mouseX,mouseY)
    message=('Generation: '+str(generation))
    drawText(message)
    pygame.display.update()
