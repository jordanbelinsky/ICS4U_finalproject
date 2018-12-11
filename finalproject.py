"""
Names: Ritchie Dimaria, Jeremy Weisberg, Jordan Belinsky, Alex Giannoulis
Project: Conway's Game of Life
"""

"""
Testing that merging will work properly
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
    
    def checkNeighbors(self,other):
        pass                
    def draw(self,screen):
        x = self.x
        y = self.y
        size = self.size
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
    for i in range (100):
        matrix.append([])
        for j in range (100):
            cell = Cell(False,i*size,j*size)
            matrix[i].append(cell)
                                                                
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
  #  for i in range(len(matrix)):
   #     for j in range(len(matrix[0])):
    #        draw.cell()
    redraw_game_window()
