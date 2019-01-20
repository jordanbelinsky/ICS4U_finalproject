import pygame
import random
import pygame.midi
rules = '''
        1. Any live cell with fewer than two live neighbours dies, as if caused by under-population.
        2. Any live cell with two or three live neighbours lives on to the next generation.
        3. Any live cell with more than three live neighbours dies, as if by overcrowding.
        4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
        '''

#Initializations:

#CONSTANTS
#-------------------
gridSize = 100
size = 10
FPS = 100
WIDTH,HEIGHT = 1000,800
generation = 0
count = 0
#-------------------

#Define a 2D board (List containing lists)
board = [[False for i in range(gridSize)] for j in range(gridSize)]

#Set up colors for ease of use
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (211, 211, 211)
coolGrey = (130,130,130)
RED = (255,0,0)


# COPY #
#states
rules = False
rules_2 = False
main_game = True
########

#Set up pygame
pygame.init()
pygame.midi.init()

#Setting up midi
player = pygame.midi.Output(0)
player.set_instrument(120)

# COPY #
font = pygame.font.SysFont("Ariel Black",30)
header = pygame.font.SysFont("Ariel Black",38) 
screen = pygame.display.set_mode((WIDTH,HEIGHT)) # Define the surface for the simulation to run on
pygame.display.set_caption('Conway\'s Game of Life')
smallGlide = font.render('Small glider', False, (0, 0, 0))
rules_text = font.render('Rules', False, (0, 0, 0))
screen.fill(WHITE) # Fill the screen white
pygame.display.update()
clock = pygame.time.Clock()
########

initialCoord = None # Coordinates for drag&drop
timer=0
text_X = 10                             # initial coordinates
text_Y = 10

extendo = False # Pullout menu starts closed
currentShape = -1 # Current shape on mouse starts as nothing
#Function for returning which row and column the mouse is in
def drawTempRect(row,col):
    pygame.draw.rect(screen,coolGrey, (row*10,col*10,10,10),0)
class Shape(object):
    def __init__(self, shapelist):
        self.shapelist = shapelist

    def rotate(self):
        list_of_tuples = zip(*self.shapelist[::-1])
        rotatedShape= [list(i) for i in list_of_tuples]
        self.shapelist = rotatedShape
    def drawtempShape(self,row,col):
        for i in range(len(self.shapelist)):
            for j in range(len(self.shapelist[0])):
                if self.shapelist[i][j]:
                    drawTempRect(row-j,col-i)
                    
    def addShape(self,row,col):
        for i in range(len(self.shapelist)):
            for j in range(len(self.shapelist[0])):
                if self.shapelist[i][j]:
                    giveLife(row-j,col-i)

smallglider = Shape([[False,True,False],
                      [False,False,True],
                      [True,True,True]])

allShapes = [smallglider]
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
    board[row][col] = True

def rotateShape(shapelist):
    list_of_tuples = zip(*shapelist[::-1])
    return [list(i) for i in list_of_tuples]

#Turn a space of the grid off
def killRuthlessly(row, col):
    board[row][col] = False

def drawcurrentshape(row,col,currentShape):
    allShapes[currentShape].drawtempShape(row,col)
    if click[0]:
        killRuthlessly(row,col)
        allShapes[currentShape].addShape(row,col)
    if click[2]:
        currentShape = None
    if click[1]:
        allShapes[currentShape].rotate()
        pygame.time.delay(40)
# COPY #
def checkGui(mouseX,mouseY):
    global extendo,currentShape,rules,main_game
    if (mouseX > 97 and mouseY>40 and mouseY<49):
        extendo = True
    if extendo == True:
        if (mouseX > 82 and mouseX < 98 and mouseY > 2 and mouseY < 10):
            currentShape=0
        if (mouseX > 82 and mouseX < 98 and mouseY > 69 and mouseY < 77):
            rules = True
            run = False
        if mouseX > 77:
            killRuthlessly(mouseX,mouseY)
        if mouseX > 77 and mouseX < 80 and mouseY > 40 and mouseY < 49:
            extendo = False
########

# COPY #
def drawGui():# COPY #
    global extendo
    if extendo == True:
        pygame.draw.rect(screen,coolGrey,(800,0,200,HEIGHT),0)
        pygame.draw.rect(screen,BLACK,(800,1,199,HEIGHT-2),3)
        pygame.draw.rect(screen,WHITE,(820,50,160,80),0)    # small glider
        pygame.draw.rect(screen,WHITE,(820,165,160,80),0)   # shape 2
        pygame.draw.rect(screen,WHITE,(820,280,160,80),0)   # shape 3
        pygame.draw.rect(screen,WHITE,(820,395,160,80),0)   # shape 4
        pygame.draw.rect(screen,WHITE,(820,690,160,80),0)   # rules
        pygame.draw.rect(screen,BLACK,(777,402,24,86),0)
        pygame.draw.rect(screen,coolGrey,(780,405,19,80),0)
        pygame.draw.polygon(screen,WHITE,[(785,419),(785,429),(795,424)],0)
        pygame.draw.polygon(screen,WHITE,[(785,439),(785,449),(795,444)],0)
        pygame.draw.polygon(screen,WHITE,[(785,459),(785,469),(795,464)],0)
        screen.blit(smallGlide,(820,25))    # small glider
        screen.blit(smallGlide,(820,140))   # shape 2
        screen.blit(smallGlide,(820,255))   # shape 3
        screen.blit(smallGlide,(820,370))   # shape 4
        screen.blit(rules_text,(870,720))
    else:
        pygame.draw.rect(screen,BLACK,(980,405,50,80),3)
        pygame.draw.rect(screen,coolGrey,(980,405,50,80),0)
        pygame.draw.polygon(screen,WHITE,[(995,419),(995,429),(985,424)],0)
        pygame.draw.polygon(screen,WHITE,[(995,439),(995,449),(985,444)],0)
        pygame.draw.polygon(screen,WHITE,[(995,459),(995,469),(985,464)],0)
########

def drawText(message):
    text = font.render(message, 1, BLACK) # put the font and the message together
    screen.blit(text,(text_X,text_Y))

# COPY #
# Draw Rules #
def draw_rules_page_one():
    title = header.render("Conway's Game Of Life", 1, BLACK)
    description_1 = font.render('This is a game where you draw set patterns of squares on the screen,', 1, BLACK)
    description_2 = font.render('which are then animated and react to the rules below, forming a living ecosystem.', 1, BLACK) 
    rule_1 = font.render('1. Any live cell with fewer than two live neighbours dies, as if caused by under-population.', 1, BLACK)
    rule_2 = font.render('2. Any live cell with two or three live neighbours lives on to the next generation.', 1, BLACK)
    rule_3 = font.render('3. Any live cell with more than three live neighbours dies, as if by overcrowding.', 1, BLACK)
    rule_4 = font.render('4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.', 1, BLACK)
    names = font.render('By: Jordan Belinsky, Ritchie DiMaria, Alex Giannoulis, and Jeremy Weisberg', 1, BLACK)
    escape =  font.render('Press E to return to the main game', 1, BLACK)
    screen.blit(title, (350, 50))
    screen.blit(description_1, (150, 125))
    screen.blit(description_2, (95, 175))
    screen.blit(rule_1, (50, 275))
    screen.blit(rule_2, (100, 340))
    screen.blit(rule_3, (100, 415))
    screen.blit(rule_4, (50, 490))
    screen.blit(names, (105, 585))
    screen.blit(escape, (335, 700))
    pygame.draw.rect(screen, BLACK, (380,750,100,30), 0)
    pygame.draw.rect(screen, coolGrey, (530,750,100,30), 0)

def draw_rules_page_two():
    title = header.render("Conway's Game Of Life", 1, BLACK)
    description_1 = font.render('This is a game where you draw set patterns of squares on the screen,', 1, BLACK)
    description_2 = font.render('which are then animated and react to the rules below, forming a living ecosystem.', 1, BLACK)
    key_title = font.render('Keyboard Shortcuts:', 1, BLACK)
    key_enter = font.render('Enter: Start/Pause Game', 1, BLACK)
    key_s = font.render('S: Save Map', 1, BLACK)
    key_l = font.render('L: Load Map', 1, BLACK)
    key_f = font.render('F: Enable/Disable Drag Select', 1, BLACK)
    key_k = font.render('K: Load Shape', 1, BLACK)
    key_r = font.render('R: Random Map', 1, BLACK)
    key_c = font.render('C: Clear Map', 1, BLACK)
    key_right = font.render('Right Arrow: Fast Forward', 1, BLACK)
    escape =  font.render('Press E to return to the main game', 1, BLACK)
    screen.blit(title, (350, 50))
    screen.blit(description_1, (150, 125))
    screen.blit(description_2, (95, 175))
    screen.blit(key_title, (400, 275))
    screen.blit(key_enter, (380, 320))
    screen.blit(key_s, (440, 355))
    screen.blit(key_l, (440, 390))
    screen.blit(key_f, (355, 425))
    screen.blit(key_k, (435, 460))
    screen.blit(key_r, (435, 495))
    screen.blit(key_c, (440, 530))
    screen.blit(key_right, (375, 565))
    screen.blit(escape, (335, 700))
    pygame.draw.rect(screen, coolGrey, (380,750,100,30), 0)
    pygame.draw.rect(screen, BLACK, (530,750,100,30), 0)
########

def draw_grid():
    for i in range(0,WIDTH,size):
        pygame.draw.line(screen,GREY,(i,0),(i,HEIGHT),1)
    for i in range(0,HEIGHT,size):
        pygame.draw.line(screen,GREY,(0,i),(WIDTH,i),1)

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

def dragdrop(inital,x,y):
    startx,starty = inital
    pygame.draw.polygon(screen,RED,((startx*10, starty*10), (startx*10,y*10),(x*10,y*10),(x*10,starty*10)),3)
   
def save_shape(startx,starty,x,y):
    if run == False:
        #name=input("Enter the name of the file you want to save")
        file_out = open('shape','w')
        for i in range(len(board)):
            for j in range(len(board[i])):
                if (starty <= j <= y) and (startx <= i <= x):
                    file_out.write(str(board[i][j])+' ')
            file_out.write('\n')
        file_out.close()

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

def place_spaceship():
    pass

def place_oscillator():
    pass

def place_stillLife():
    pass


#Main loop
genCount = 0
mouse_mode = True
run = False
while main_game == True:
    mouseX,mouseY = mousePos()
    #Draw the board as rectangles
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col]:
                pygame.draw.rect(screen, BLACK, (row*10,col*10,size,size),0)
            if not board[row][col]:
                pygame.draw.rect(screen, WHITE, (row*10,col*10,size,size),0)
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
            if event.key == pygame.K_f:
                mouse_mode = not mouse_mode
            if event.key == pygame.K_k:
                newlst=load_shape()
            # COPY #
            if rules:
                if event.key == pygame.K_RIGHT:
                    rules = False
                    rules_2 = True
                if event.key == pygame.K_e:
                    rules = False
                    run = False
            if rules_2:
                if event.key == pygame.K_LEFT:
                    rules = True
                    rules_2 = False
                if event.key == pygame.K_e:
                    rules_2 = False
                    run = False
            ########

                
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
                                if board[row][col] == False and tempboard[row][col]:
                                    player.note_on(row+5, 75)
                        board = tempboard
                        generation += 1
                        run = False       
                

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
                if board[row][col] == False and tempboard[row][col] == True:
                    player.note_on(row+5, 75)
        board = tempboard
        generation += 1
        genCount = 1

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



    # COPY #       
    draw_grid()
    drawGui()
    if currentShape>-1:
        drawcurrentshape(mouseX,mouseY,currentShape)
    message=('Generation: '+str(generation))
    drawText(message)
    if rules:
        screen.fill(WHITE)
        draw_rules_page_one()
    if rules_2:
        screen.fill(WHITE)
        draw_rules_page_two()
    pygame.display.update()
    ########
