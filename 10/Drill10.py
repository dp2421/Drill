from pico2d import *
import random

# Game object class here
class Ball():
    def __init__ (self):
        self.image = load_image('ball21x21.png')
        self.bigimage = load_image('ball41x41.png')
        self.x = random.randint(0, 800)
        self.y=599
    def draw(self):
        for i in range(10):
            self.image.draw(self.x, self.y)
        for i in range(10):
            self.bigimage.draw(self.x, self.y)
    def update_balls(self):
        if self.y < 70:
            self.y= 70
        self.y -= 10

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code


# game main loop code
open_canvas()
running =True
grass = load_image('grass.png')
character = load_image ('run_animation.png')
balls = Ball()
count = [Ball() for i in range(20)]

while running:
    for balls in count:
        balls.update_balls()
    clear_canvas()
    handle_events()
    grass.draw(400, 30)
    for balls in count:
        balls.draw()
    update_canvas()

# finalization code