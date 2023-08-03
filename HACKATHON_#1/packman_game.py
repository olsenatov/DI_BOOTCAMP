import pygame
from board import board
import math

#basic settings for the game - variables
pygame.init()

SCREENHEIGHT = 950
SCREENWIDTH = 900

screen = pygame.display.set_mode([SCREENWIDTH, SCREENHEIGHT])

timer = pygame.time.Clock()
fps = 60

font = pygame.font.Font('assets/RobotoMono-Medium.ttf', 20)

level = board
color = 'green'

PI = math.pi

player_images = []
for i in range(1,3):
    player_images.append(pygame.transform.scale(pygame.image.load(f'assets/player_images/{i}.png'), (45, 45)))

#draw_board
def draw_board():
    num1 = ((SCREENHEIGHT - 50) // 32)
    num2 = (SCREENWIDTH // 30)
# 0 = empty black rectangle, 1 = dot, 2 = big dot, 
# 3 = vertical line  4 = horizontal line
# 5 = top right corner, 6 = top left corner, 
# 7 = bottom left corner, 8 = bottom right corner
# 9 = gate
    
    for i in range(len(level)):
        for j in range(len(level[i])):
            if level[i][j] == 1:
                pygame.draw.circle(screen, 'white', (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1)), 4)
            if level[i][j] == 2:
                pygame.draw.circle(screen, 'white', (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1)), 10)  
            if level[i][j] == 3:    
                 pygame.draw.line(screen, color, (j * num2 +(0.5 * num2), i * num1), (j * num2 +(0.5 * num2), i * num1 + num1), 3)
                 
            if level[i][j] == 4: 
                pygame.draw.line(screen, color, (j * num2, i * num1 +(0.5 * num1)), (j * num2 + num2, i * num1 + (0.5 * num1)), 3)
                 
            if level[i][j] == 5: 
               pygame.draw.arc(screen, color, [(j * num2 - (num2 * 0.5)), (i * num1 + (0.5 * num1)), num2, num1], 0, PI / 2, 3)
                  
            if level[i][j] == 6: 
                pygame.draw.arc(screen, color, [(j * num2 + (num2 * 0.5)), (i * num1 + (0.5 * num1)), num2, num1], PI / 2, PI, 3)
                
            if level[i][j] == 7: 
                pygame.draw.arc(screen, color, [(j * num2 + (num2 * 0.5)), (i * num1 - (0.5 * num1)), num2, num1], PI, 3*PI / 2, 3)
                               
            if level[i][j] == 8: 
                 pygame.draw.arc(screen, color, [(j * num2 - (num2 * 0.5)), (i * num1 - (0.5 * num1)), num2, num1], 3*PI / 2, 2*PI, 3)
                
            if level[i][j] == 9: 
                pygame.draw.line(screen, 'white', (j * num2, i * num1 +(0.5 * num1)), (j * num2 + num2, i * num1 + (0.5 * num1)), 3)
                  
# def draw_player():
    

run = True
while run:
    timer.tick(fps)
    screen.fill("black")
    draw_board()
    draw_player()
    
   
    
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            run = False
        
    pygame.display.flip()

pygame.quit()
            