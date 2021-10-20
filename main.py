from pico2d import *
import random



class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
    def draw(self):
        self.image.draw(400,30)



class Boy:
    global running_right
    global jump1
    def __init__(self):
        self.x, self.y = 100,90
        self.image=load_image('animation_sheet.png')
        self.frame=0
    def draw(self):
        if running_right:
            self.image.clip_draw(self.frame * 100, 100*1 , 100, 100, self.x, self.y)
        else:
            self.image.clip_draw(self.frame * 100, 100*0 , 100, 100, self.x, self.y)
    def update(self):
        self.x += dir
        if self.y<=390:
            self.y += jump1
        else:
            self.y -= jump1
        self.frame = (self.frame + 1) % 8

class Niddle:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 70
        self.image=load_image('niddle1.png')
    def draw(self):
        self.image.draw(self.x, self.y)






def handle_events():
    global running
    global dir
    global running_right
    global jump1
    running_right=dir>= 0
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
            dir += 1
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
            dir -= 1
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
            dir -= 1
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
            dir += 1
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_z):
            jump1+=300


open_canvas()
dir=0
jump1=0
niddle=Niddle()
grass=Grass()
boy=Boy()

running=True
running_right=True
while running:
    handle_events()
    boy.update()
    clear_canvas()
    grass.draw()
    boy.draw()
    niddle.draw()
    update_canvas()


close_canvas()
