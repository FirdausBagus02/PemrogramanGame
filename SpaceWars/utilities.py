import pygame
import colors

class Character:
    '''
    posX, posY -> (x, y) cords
    widht, height -> (width, height) of character
    '''

    def __init__(self, posX, posY, width, height, character_img):
        self.posX = posX
        self.posY = posY
        self.width = width
        self.height = height
        self.Img = character_img
        self.score = 0

    def move_right(self, dx=0.1):
        self.posX += dx

    def move_left(self, dx=0.1):
        self.posX -= dx

    def move_up(self, dy=0.1):
        self.posY -= dy

    def move_down(self, dy=0.1):
        self.posY += dy

    def move(self, dx, dy):
        self.posX += dx
        self.posY += dy

    def increase_score(self, pnt=1):
        self.score+=pnt
    
    def show_score(self):
        return self.score

class Enemy:
    import random
    import math
    '''
    posX, posY -> (x, y) cords
    widht, height -> (width, height) of character
    character_img -> image of character (python.pygame image object)
    Hrange, Vrange -> horizontal and vertical range where enemy can roam
    '''

    def __init__(self, width, height, character_img, Hrange, Vrange):
        self.posX = (self.random.randint(width, Hrange-width)//width)*width
        self.posY = (self.random.randint(0, Vrange)//height)*height
        self.width = width
        self.height = height
        self.Img = character_img
        self.Hrange = Hrange
        self.Vrange = Vrange
        self.dx = self.random.randint(5, 10)/10
        self.dy = self.math.floor(self.width)

    def move(self):
        # Horizontal movement logic
        # print(self.posX, self.posY)
        if self.posX+self.width > self.Hrange or self.posX <= 0:
            self.dx *= -1
            self.posY += self.dy
        self.posX += self.dx


class Bullet(Character):
    '''
    posX, posY -> (x, y) cords
    widht, height -> (width, height) of character
    character_img -> image of character (python.pygame image object)
    Hrange, Vrange -> horizontal and vertical range where enemy can roam
    state -> `to be defined later`
    '''

    def __init__(self, posX, posY, width, height, character_img, dy=1, state=None):
        Character.__init__(self, posX, posY, width, height, character_img)
        self.state = state
        self.dy = dy

class Button:
    def __init__(self,color, posX, posY, width, height, text='',size=32, left_offet=0, top_offset=0):
        self.posX = posX
        self.posY = posY
        self.width = width
        self.height = height
        self.text = text
        self.color = color
        self.left_offet  = left_offet
        self.top_offset = top_offset
    
    def draw(self,screen, outline_color=None):
        if outline_color:
            pygame.draw.rect(screen, outline_color, (self.posX-2, self.posY-2, self.width+4, self.height+4))
        
        pygame.draw.rect(screen, self.color, (self.posX, self.posY, self.width, self.height))

        if self.text!='':
            font = pygame.font.SysFont(None, 32)
            text = font.render(self.text, 1, colors.Black)
            screen.blit(text, (self.posX+self.left_offet, self.posY+self.top_offset))
    
    def ishover(self, pos):
        ''' pos -> mouse position '''
        if pos[0]>=self.posX and pos[0]<=self.posX+self.width:
            if pos[1]>=self.posY and pos[1]<=self.posY+self.height:
                return True
        return False
    
        