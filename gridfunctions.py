# Import #
import pygame
WIDTH,HEIGHT = 1000,800
size = 10
GREY = (211, 211, 211)

# Draw Background Grid #
def draw_grid(screen):
    """
    Uses for loops to draw a grid within range of the screen both horizontallly and vertically
    """
    # Horizontal #
    for i in range(0,WIDTH,size):
        pygame.draw.line(screen,GREY,(i,0),(i,HEIGHT),1)
    # Vertical #
    for i in range(0,HEIGHT,size):
        pygame.draw.line(screen,GREY,(0,i),(WIDTH,i),1)

# Save Current Grid #
def save_grid(run,board):
    """
    Uses reading and writing to save the current grid into a text file
    """
    if run == False:
        #name=input("Enter the name of the file you want to save")
        file_out = open('map','w')
        for i in range(len(board)):
            for j in range(len(board[i])):
                file_out.write(str(board[i][j])+' ')
            file_out.write('\n')
        file_out.close()

# Load a Previously Saved Grid #
def load_grid(run):
    """
    Uses reading and writing to load a saved grid from a text file
    """
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
