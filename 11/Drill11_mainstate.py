import random
import json
import os

from pico2d import *

import Drill11_framework


from Drill11 import Boy
from Drill11_grass import Grass



name = "MainState"

boy = None
grass = None
font = None



def enter():
    global boy, grass
    boy = Boy()
    grass = Grass()


def exit():
    global boy, grass
    del boy
    del grass



def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            Drill11_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                Drill11_framework.quit()
        else:
            boy.handle_event(event)



def update():
    boy.update()

def draw():
    clear_canvas()
    grass.draw()
    boy.draw()
    update_canvas()






