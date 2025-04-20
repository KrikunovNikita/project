from random import randint, choice

from pygame import *


class Sprite(sprite.Sprite):
    def __init__(self, sprite_sheet, x=0, y=0, w=0, h=0, speed=2):
        super().__init__()
        self.all_frames = {}
        self.load_frames(sprite_sheet, 6, "idle")
        self.animation = "idle"
        self.image = self.all_frames[self.animation][0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.frame_num = 0


    def load_frames(self, sprite_sheet, num_frames, frames_name):
        frames = []
        sprite_sheet = image.load(sprite_sheet)
        frame_width = sprite_sheet.get_width() / num_frames
        frame_height = sprite_sheet.get_height()
        for i in range(num_frames):
            frame = Surface((frame_width, frame_height))
            frame.blit(sprite_sheet, (i * frame_width, 0, frame_width, frame_height))
            frames.append(frame)
        self.all_frames[name] = frames

    def update(self):
        self.frame_num += 0.1
        if self.frame_num >= 10:
            self.frame_num = 0
        else:
            self.image = self.frames[self.frame_num]

    def draw(self, screen):
        screen.blit(self.image, (self.rectrect.x, self.rect.y))



class Player(Sprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a]:
            self.rect.x -= self.speed
        if key[K_d]:
            self.rect.x += self.speed
        if key[K_w]:
            self.rect.y -= self.speed
        if key[K_s]:
            self.rect.y += self.speed



WINDOW_WIDTH = 720
WINDOW_HEIGHT = 480
FPS = 60
SPEED = 4

window = display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
Player = Player("Gangsters_1/Idle.png",10,400,50, 100,30)


clock = time.Clock()

run = True

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
            
    Player.update()
    Player.drow()

    display.update()
    clock.tick(FPS)
