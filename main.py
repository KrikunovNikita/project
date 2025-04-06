from random import randint, choice

from pygame import *

class Sprite(sprite.Sprite):
    def __init__(self, sprite_sheet, x=0, y=0, w=0, h=0, speed=2):
        self.image = image.load(sprite_sheet)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.frame_num = 0
    
    def load_frames(self, sprite_sheet, num_frames):
        frames = []
        sprite_sheet = image.load(sprite_sheet)
        frame_width = sprite_sheet.get_width() / num_frames
        frame_height = sprite_sheet.get_height()
        for i in range(num_frames):
            frame = Surface((frame_width, frame_height))
            frame.blit(sprite_sheet, (i * frame_width, 0, frame_width, frame_height))
            frames.append(frame)
        return frames
        
    def update(self):
        self.frame_num += 0.1
        if self.frame_num >= 10:
            self.frame_num = 0
        else:
            self.image = self.framse []
    def draw(self, screen):
        screen.blit(self.image, (self.rectrect.x, self.rect.y))

class Player(Sprite):


WINDOW_WIDTH = 720
WINDOW_HEIGHT = 480
FPS= 60
SPEED = 4


window = display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

clock = time.Clock()

run = True

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    display.update()
    clock.tick(FPS)
