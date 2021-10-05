from pico2d import *
import random

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def handle_events():
	global running
	global x, y
	global x2, y2
	events= get_events()

	for event in events:
		if event.type==SDL_MOUSEBUTTONDOWN:
			x, y=random.randrange(0,KPU_WIDTH),random.randrange(0,KPU_HEIGHT-1-y)
			x2, y2=random.randrange(0,KPU_WIDTH),random.randrange(0,KPU_HEIGHT-1-y)
		elif event.type == SDL_KEYDOWN and event.key==SDLK_ESCAPE:
			running=False



open_canvas(KPU_WIDTH,KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image("animation_sheet.png")
mouse=load_image('hand_arrow.png')
running=True
frame=0
x, y=random.randrange(0,KPU_WIDTH),random.randrange(0,KPU_HEIGHT)
while running:
	clear_canvas()
	kpu_ground.draw(KPU_WIDTH//2, KPU_HEIGHT//2)
	character.clip_draw(frame*100, 100*1, 100, 100, x-30, y+30)
	mouse.draw(x,y)
	
	update_canvas()
	frame=(frame + 1)% 8
	delay(0.01)
	handle_events()
	

close_canvas()

