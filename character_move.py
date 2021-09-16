from pico2d import *
from math import *
open_canvas()

grass=load_image('grass.png')
character=load_image('character.png')
x=0
y=90
while True:
    degree=-1.6
    while x<800:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x+=2
        delay(0.01)
    while y<600:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y+=2
        delay(0.01)
    while x>0:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x-=2
        delay(0.01)
    while y>90:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y-=2
        delay(0.01)
    while x<401:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x+=2
        delay(0.01)
    while degree<4.7:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(400+cos(degree)*200,300+sin(degree)*200)
        degree+=0.01
        delay(0.01)


    
        
    


    
delay(5)


close_canvas()
