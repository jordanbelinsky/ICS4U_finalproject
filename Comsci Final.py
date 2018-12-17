import pygame
import random

rules = '''
    1. Any live cell with fewer than two live neighbours dies, as if caused by under-population.
    2. Any live cell with two or three live neighbours lives on to the next generation.
    3. Any live cell with more than three live neighbours dies, as if by overcrowding.
    4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.'''

#Initializations:

#CONSTANTS
#-------------------
gridSize = 100
size = 10
FPS = 100
WIDTH,HEIGHT = 1000,1000
generation = 0
#-------------------

#Define a 2D board (List containing lists)
board = [[False for i in range(gridSize)] for j in range(gridSize)]

#Set up colors for ease of use
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (211, 211, 211)

#Set up pygame
pygame.init()
font = pygame.font.SysFont("Ariel Black",30)
screen = pygame.display.set_mode((WIDTH,HEIGHT)) # Define the surface for the simulation to run on
pygame.display.set_caption('Conway\'s Game of Life')
screen.fill(WHITE) # Fill the screen white
pygame.display.update()
clock = pygame.time.Clock()

text_X = 10                             # initial coordinates
text_Y = 10
#Function for returning which row and column the mouse is in
def mousePos():
    x, y = pygame.mouse.get_pos()
    return (x//10, y//10)

#Function to find number of live neighbors
def findNeighbors(row, column):
    alive = 0

    #Horizontally adjacent
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

    #Diagonally adjacent
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

    #Return the final count (0-8)
    return alive

#Turn a space of the grid on
def giveLife(row, col):
    pygame.draw.rect(screen, BLACK, (row*10,col*10,size,size),0)

#Turn a space of the grid off
def killRuthlessly(row, col):
    pygame.draw.rect(screen, WHITE, (row*10,col*10,size,size),0)

def drawText(message):
    text = font.render(message, 1, BLACK) # put the font and the message together
    screen.blit(text,(text_X,text_Y))

def draw_grid():
    for i in range(0,HEIGHT,size):
        pygame.draw.line(screen,GREY,(i,0),(i,WIDTH),1)
    for i in range(0,WIDTH,size):
        pygame.draw.line(screen,GREY,(0,i),(HEIGHT,i),1)

def save_grid():
    if run == False:
        #name=input("Enter the name of the file you want to save")
        file_out = open('map','w')
        for i in range(len(board)):
            for j in range(len(board[i])):
                file_out.write(str(board[i][j])+' ')
            file_out.write('\n')
        file_out.close()

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

def save_shape():
    pass

def load_shape():
    pass

def place_spaceship():
    pass

def place_oscillator():
    pass

def place_stillLife():
    pass

# Main loop #
run = False
while True:
    
    # Draw the board as rectangles #
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col]:
                giveLife(row, col)
            if not board[row][col]:
                killRuthlessly(row, col)

    #Process Events            
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                break
            if event.key == pygame.K_RETURN:
                run = not run
            if event.key == pygame.K_s:
                save_grid()
            if event.key == pygame.K_l:
                newlst = load_grid()
                board=newlst
                



            if run == False:
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
                if event.key == pygame.K_LEFT:
                    '''TODO: Use the left key to navigate back 1 generation'''







                
            if event.key == pygame.K_c:
                if run == True:
                    run = not run
                generation = 0
                board = [[False for i in range(gridSize)] for j in range(gridSize)]

            if event.key == pygame.K_r:
                generation = 0
                possibilities = [False, False, True]
                for row in range(gridSize):
                    for col in range(gridSize):
                        board[row][col] = random.choice(possibilities)


    #RULES
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
        

    click = pygame.mouse.get_pressed()
    if click[0]:
        mouseX,mouseY = mousePos()
        board[mouseX][mouseY] = True
        if not run:
            generation = 0
    if click[2]:
        mouseX,mouseY = mousePos()
        board[mouseX][mouseY] = False
        if not run:
            generation = 0

        
    draw_grid()
    message=('Generation: '+str(generation))
    drawText(message)
    pygame.display.update()
