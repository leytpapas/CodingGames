# author = Lefteris Papadomanolakis
# e-mail = leytpapas@hotmail.com
# Puzzle-url = https://www.codingame.com/ide/puzzle/shadows-of-the-knight-episode-1

# Description: 
# Find a random cell from a random starting point in a grid, 
# while given directions on its position relative to x0, y0
import sys
import math,random
import time
import datetime
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]


print("Width:"+str(w)+" Height:"+str(h), file=sys.stderr)
print("Starting at pos:"+str(x0)+" "+str(y0), file = sys.stderr)

x_new = x0
y_new = y0

top = 0
bottom = h-1
left = 0
right = w-1

    
# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    print(bomb_dir, file=sys.stderr)
    
    if bomb_dir=="U":
        right = x0
        left = x0
        bottom = y0-1 
        
        x_new = x0 
        y_new = y0 - int((bottom - top)/2) - 1
        
    elif bomb_dir == "UR":
        left = x0 + 1
        bottom = y0 - 1
        
        x_new = x0 + int((right - left)/2) + 1
        y_new = y0 - int((bottom - top)/2) - 1
        
    elif bomb_dir == "R":
        
        top = y0
        bottom = y0
        left = x0 + 1
        
        x_new = x0 + int((right - left)/2) + 1
        y_new = y0
        #x_new = x0 + (int(w-x0)/(2+step_x))
    elif bomb_dir == "DR":
        top = y0 +1
        left = x0 + 1
        
        x_new = x0 + int((right - left)/2) + 1 
        y_new = y0 + int((bottom - top)/2) + 1
        
    elif bomb_dir == "D":
        
        right = x0
        left = right
        top = y0 + 1
        
        x_new = x0
        y_new = y0 + int((bottom - top)/2) + 1
        
    elif bomb_dir == "DL":
        top = y0 +1
        right = x0 - 1
        
        x_new = x0 - int((right - left)/2) - 1
        y_new = y0 + int((bottom - top)/2) + 1
       
    elif bomb_dir == "L":
        top = y0
        bottom = y0
        right = x0 - 1
        
        x_new = x0 - int((right - left)/2) - 1
        y_new = y0 
       
    elif bomb_dir == "UL":
        bottom = y0 -1
        right = x0 -1
        
        x_new = x0 - int((right - left)/2) - 1
        y_new = y0 - int((bottom - top)/2) - 1
    print("TOP:",top,"BOTTOM:",bottom,"\nLEFT:",left,"RIGHT:",right,file=sys.stderr)
    y0=y_new
    x0=x_new
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)


    # the location of the next window Batman should jump to.
    print(str(int(x_new))+" "+ str(int(y_new)))
