"""
Names: Ritchie Dimaria, Jeremy Weisberg, Jordan Belinsky, Alex Giannoulis
Project: Conway's Game of Life
"""

########################
# Import and Variables #
########################
import pygame
gameOn = False

WHITE = (255,255,255)
BLACK = (  0,  0,  0)
GREY = ( 50, 50, 50)
HEIGHT = 640
WIDTH = 480
size = 10
gridSize=100
matrix=[]
###########
# Objects #
###########
class Cell(object):
    def __init__(self, alive = False, x=0, y=0 ,size = 10):
        self.alive = alive
        self.x = x
        self.y = y
        self.size = size
    def __str__(self):
        return (str(self.alive)+','+str(self.x)+','+str(self.y))

    def isAlive(self):
        '''
        (self) -> (bool)
        A function that is able to return the dead or alive value of a cell'''
        if self.alive==True:
            return True
        else:
            return False
    
    def checkNeighbors(self):
        '''
        (self) -> (int)
        A Function which checks the amount of alive neighboring cells around each individual cells'''
        count = 0
        for i in (matrix):
            for j in (matrix):
                if matrix[i][j-1].isAlive():
                    count +=1
        print (count)
        return count
                    
    def draw(self,screen,x,y,size):
        pygame.draw.rect(screen,WHITE,(x,y,size,size),0)

class Grid(object):
    def __init__(self):
        pass
        
#############
# Functions #
#############

def draw_grid():
    for i in range(0,HEIGHT,size):
        pygame.draw.line(screen,BLACK,(i,0),(i,WIDTH),1)
    for i in range(0,WIDTH,size):
        pygame.draw.line(screen,BLACK,(0,i),(HEIGHT,i),1)

def makeArray():
    '''
    None -> (int)
    A function which creates the initial array of cells in a 100x100 size grid'''
    count=0
    for i in range (100):
        matrix.append([])
        for j in range (100):
            cell = Cell(False,i*size,j*size)
            matrix[i].append(cell)
        print(matrix)
    return matrix
            
    

def checkArray(matrix):
    if matrix[i][j-1].isAlive():
        count +=1
    print(count)
    
def redraw_game_window():
    screen.fill(GREY)
    draw_grid()
    pygame.display.update()

#############
# Main Game # 
#############
pygame.init()
screen=pygame.display.set_mode((HEIGHT,WIDTH))
for event in pygame.event.get():                    #Main Pygame Loop
    makeArray()
    if event.type == pygame.KEYDOWN:                #Check if a key is pressed
        if event.key == pygame.K_SPACE:             #If space is pressed, turn gameOn, meaning the simulation is on
            gameOn=True                             #Space is to be pressed after user selects all alive cells
while gameOn==True:
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            draw.cell()
    checkArray(matrix)
    redraw_game_window()
    
    
