import pygame
import keyboard
wid=500
hei=100
win=pygame.display.set_mode((wid,hei))
class player:
	def __init__(self,x,y,width,height):
		self.x=x
		self.y=y
		self.width=width
		self.height=height
	def move(self):
		self.x+=5
rock=player(10,20,10,10)
hammer=player(100,50,10,10)
delay=50
run=True
movemount=0
while run:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			run=False
	if delay==0:
		if keyboard.is_pressed('space'):
			rock.move()
			if rock.x>=245:
				movemount+=5
			delay=50
	else:
		delay-=1
	pygame.draw.rect(win,(255,255,255),((rock.x-movemount),rock.y,rock.width,rock.height))
	pygame.draw.rect(win,(255,255,255),((hammer.x-movemount),hammer.y,hammer.width,hammer.height))
	pygame.display.update()
	win.fill((0,0,0))