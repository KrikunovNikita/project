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
        self.is_flipped = False

    def load_frames(self, sprite_sheet, num_frames, frames_name):
        frames = []
        sprite_sheet = image.load(sprite_sheet)
        frame_width = sprite_sheet.get_width() / num_frames
        frame_height = sprite_sheet.get_height()
        for i in range(num_frames):
            frame = Surface((frame_width, frame_height))
            frame.blit(sprite_sheet, (0, 0),(i * frame_width, 0, frame_width, frame_height))
            frames.append(frame)
        self.all_frames[frames_name] = frames

    def update(self):
        self.frame_num += 0.1
        if self.frame_num >= len(self.all_frames[self.animation]):
            self.frame_num = 0
        else:
            if self.is_flipped:
                self.image = self.all_frames[self.animation][int(self.frame_num)]
                self.image = transform.flip(self.image, True, False)
            else:
                self.image = self.all_frames[self.animation][int(self.frame_num)]


    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))


class Player(Sprite):
    def __init__(self, sprite_sheet, x=0, y=0, w=0, h=0, speed=2):
        super().__init__(sprite_sheet, x, y, w, h, speed)
        self.load_frames("Gangsters_1/Run.png", 10, "run")
        self.load_frames("Gangsters_1/Shot.png", 4, "shoot")
        self.load_frames("Gangsters_1/Jump.png", 10, "jump")
        self.gravity = 0
        self.velocity = 0
        self.is_jumping = False
        self.is_shooting = False

    def update(self):
        mouse_buttons = mouse.get_pressed()
        keys = key.get_pressed()
        moving = False
        self.rect.x -= 4
        if keys[K_a]:
            self.rect.x -= self.speed
            moving = True
            self.is_flipped = True
        if keys[K_d]:
            self.rect.x += self.speed
            self.is_flipped = False
            moving = True
        if keys[K_w]:
            self.rect.y -= self.speed
        if keys[K_s]:
            self.rect.y += self.speed

        if keys[K_SPACE] and not self.is_jumping:
            self.is_jumping = True
            self.velocity = -20
            self.gravity = 0
            self.animation = "jump"
            self.frame_num = 0

        if mouse_buttons[0] and not self.is_shooting and not self.is_jumping and not moving:
            self.animation = "shoot"
            self.is_shooting = True
            self.frame_num = 0



        if self.rect.y >= 480 - 96 - self.rect.height:
            self.rect.y = 480 - 96 - self.rect.height
            self.gravity = 0
            self.is_jumping = False
        else:
            self.rect.y += self.velocity + self.gravity
            self.gravity += 1
            self.is_jumping = True

        self.animations(moving)
        super().update()

    def animations(self, moving):
        if self.is_shooting:
            if int(self.frame_num + 0.1)  >= len(self.all_frames["shoot"]):
                self.is_shooting = False
            else:
                self.is_shooting = True
            return

        if self.is_jumping:
            self.animation = "jump"
        elif moving:
            if self.animation != "run":
                self.animation = "run"
                self.frame_num = 0
        else:
            if self.animation != "idle":
                self.animation = "idle"
                self.frame_num = 0

class Background(sprite.Sprite):
    def __init__(self, sprite_img, x=0, y=0, w=0, h=0, speed=2):
        super().__init__()
        self.image = transform.scale(image.load(sprite_img), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def update(self):
        self.rect.x -= self.speed
        if self.rect.right <= 0:
            self.rect.x = 800

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

class Road(sprite.Sprite):
    def __init__(self, x=0, y=0, speed=2):
        super().__init__()
        self.roads = ["road1.png", "road2.png"]
        self.cur_image = "road1.png"
        self.image = image.load("road1.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def update(self):
        self.rect.x -= self.speed
        if self.rect.right <= 0:

            self.cur_image = choice(self.roads)
            self.image = image.load("road1.png")
            if self.cur_image == "road1.png":
                self.rect.x = 800
            else:
                self.rect.x = 1000

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))





WINDOW_WIDTH = 800
WINDOW_HEIGHT = 480
FPS = 60
SPEED = 4

window = display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
player = Player("Gangsters_1/Idle.png", 10, 300, 50, 100, 10)
backgrounds = sprite.Group()
backgrounds.add(Background("Final/Background_0.png", 0, 0, WINDOW_WIDTH, WINDOW_HEIGHT, 2))
backgrounds.add(Background("Final/Background_0.png", WINDOW_WIDTH, 0, WINDOW_WIDTH, WINDOW_HEIGHT, 2))

roads = sprite.Group()
roads.add(Road( 0, WINDOW_HEIGHT - 96, 4))
roads.add(Road(WINDOW_WIDTH, WINDOW_HEIGHT - 96, 4))


clock = time.Clock()

run = True

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    backgrounds.update()
    backgrounds.draw(window)

    roads.update()
    roads.draw(window)

    player.update()
    player.draw(window)

    display.update()
    clock.tick(FPS)
