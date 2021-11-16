from pico2d import *
import random
import game_framework

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14

class Birds:
    def __init__(self):
        self.image = load_image('bird100x100x14.png')
        self.frame= 0
        self.x = random.randrange(0, 1600-1)
        self.y = 300

    def update(self):
        self.frame = (self.frame + 1) % 14
        # self.frame = (int(self.frame) + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14
        pass

    def do(self):
        # self.frame = (self.frame + 1) % 14
        self.frame = (int(self.frame) + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14

    def draw(self):
        # self.image.draw(600, 300)
        self.image.clip_draw(int(self.frame) * 100, 0, 100, 100, self.x, self.y)
        # self.image.clip_draw(int(self.frame) * 100, 100, 100, 100,600, 300)
        # fill here


    # fill here
    def get_bb(self):
        return 0, 0, 0, 0