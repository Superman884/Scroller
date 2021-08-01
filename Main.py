import pygame
import keyboard
import time
from random import randrange
wid=500
hei=500
win=pygame.display.set_mode((wid,hei))
directions={'right':[0.01,0],'left':[-0.01,0]}
imgs=[pygame.image.load('flowey_1.png'),pygame.image.load('flowey_1_left.png'),pygame.image.load('flowey_2.png'),pygame.image.load('flowey_2_left.png'),pygame.image.load('flowey_3.png'),pygame.image.load('flowey_3_left.png')]
count=0
num=0
haha=2
suns=[pygame.image.load('sun_1.png'),pygame.image.load('sun_2.png'),pygame.image.load('sun_1.png'),pygame.image.load('sun_2.png')]
bats=[pygame.image.load('bat_down.png'),pygame.image.load('bat_up.png'),pygame.image.load('bat_down.png'),pygame.image.load('bat_up.png')]
l_b=[pygame.image.load('beaver_3_left.png'),pygame.image.load('beaver_2_left.png'),pygame.image.load('beaver_3_left.png'),pygame.image.load('beaver_3_left.png'),pygame.image.load('beaver_2_left.png'),pygame.image.load('beaver_3_left.png')]
r_b=[pygame.image.load('beaver_3.png'),pygame.image.load('beaver_2.png'),pygame.image.load('beaver_3.png'),pygame.image.load('beaver_3.png'),pygame.image.load('beaver_2.png'),pygame.image.load('beaver_3.png')]
sr=pygame.image.load('beaver_1.png')
sl=pygame.image.load('beaver_1_left.png')
elephants=[pygame.image.load('elephant_2.png'),pygame.image.load('elephant_1.png'),pygame.image.load('elephant_3.png')]
elnum=0
class player:
	def __init__(self,x,y,width,height):
		self.x=x
		self.y=y
		self.width=width
		self.height=height
		self.mom=0
		self.vel=0
		self.grounded=True
		self.number=0
	def move(self,val):
		global num
		self.mom+=val[0]/5
		if val[0]>0:
			num=0
		elif val[0]<0:
			num=1
class block:
	def __init__(self,x,y,width=40,height=40):
		self.x=x
		self.y=y
		self.width=width
		self.height=height
class collectible:
	def __init__(self,x,y,width,height,type1):
		self.x=x
		self.y=y
		self.width=width
		self.height=height
		self.type=type1
		self.mom=0
		self.vel=0
		self.loaded=False
		self.right=True
		self.left=True
		self.mommy=None
	def collide(self,person):
		if (self.x//1>person.x//1 and self.x//1<person.x//1+person.width) or (self.x//1<person.x//1 and self.x//1+self.width>person.x//1):
			if (self.y//1>=person.y//1 and self.y//1<=person.y//1+person.height) or (self.y//1<=person.y//1 and self.y//1+self.height>=person.y//1):
				return True
			else:
				pass
		return False
blocks=[block(100,320,40,40),block(100,400,1000,20),block(500,330,70,70),block(430,260,70,70),block(410,360,10,10)]
rock=player(10,20,50,50)
delay=50
run=True
movemount=0
camera=[0,0]
tu=time.time()
c=0
nom=0.5
dell=0
angle=0
ppp=1
stuff=[collectible(430,200,50,50,'sun'),collectible(1050,200,50,50,'bat'),collectible(200,200,82,42,'beaver')]
for i in stuff:
	i.mommy=blocks[0]
while run:
	win.blit(elephants[elnum],(0,0))
	if keyboard.is_pressed('space'):
		rock.vel=-0.5
	if keyboard.is_pressed('ctrl'):
		rock.mom*=1.01
	if keyboard.is_pressed('alt'):
		rock.mom*=-1
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			run=False
	if c%2==0:
		for k,v in directions.items():
			if keyboard.is_pressed(k):
				rock.move(v)
				break
	c+=1
	on=False
	right=True
	left=True
	for blocky in blocks:
		if blocky.x+blocky.width-movemount<0 or blocky.x>500 or (blocky.y>rock.y+rock.height or blocky.y+blocky.height<rock.y):
			pass
		if rock.y//1==blocky.y+blocky.height:
			if (rock.x<blocky.x and rock.x+rock.width-1>blocky.x) or (rock.x<blocky.x+blocky.width and rock.x>blocky.x):
				rock.vel=.1
		if rock.y//1+rock.height==blocky.y//1:
			if (rock.x<blocky.x and rock.x+rock.width-1>blocky.x) or (rock.x<blocky.x+blocky.width and rock.x>blocky.x):
				on=True
		if rock.x//1+rock.width==blocky.x:
			if (rock.y<blocky.y and rock.y+rock.height>blocky.y) or (rock.y>blocky.y and rock.y<blocky.y+blocky.height):
				right=False
		if rock.x//1==blocky.x+blocky.width:
			if (rock.y+1<blocky.y and rock.y+rock.height-1>blocky.y) or (rock.y-1>blocky.y and rock.y+1<blocky.y+blocky.height):
				left=False
	if on:
		rock.grounded=True
		rock.vel=0
	else:
		rock.grounded=False
	if rock.grounded:
		rock.mom*=0.996
	else:
		rock.mom*=0.9998
	if right and rock.mom>=0:
		rock.x+=(rock.mom+rock.mom*rock.number/20)
	elif left and rock.mom<=0:
		rock.x+=(rock.mom+rock.mom*rock.number/20)
	else:
		rock.mom=0
	rock.vel+=0.0006
	if keyboard.is_pressed('up') and rock.grounded:
		rock.vel=-0.4-0.4*rock.number/20
		rock.grounded=False
	if (not on) or rock.vel<0:
		rock.y+=rock.vel
	movemount=rock.x-(wid/2+rock.width/2)
	if movemount<0:
		movemount=0
	if not( rock.mom<0.01 and rock.mom>-0.01):
		win.blit(imgs[count+num],(rock.x-movemount,rock.y))
	else:
		win.blit(imgs[num],(rock.x-movemount,rock.y))
	for blocky in blocks:
		if blocky.x+blocky.width-movemount<0 or blocky.x>500:
			continue
		hurr=blocky.x-movemount
		durr=blocky.width
		if blocky.x-movemount<0 and blocky.x+blocky.width-movemount>0:
			hurr=0
			durr=blocky.width+(blocky.x-movemount)
		pygame.draw.rect(win,(255,255,255),((hurr),blocky.y,durr,blocky.height))
	for thing in stuff:
		if (thing.x+thing.width-movemount<0 or thing.x-movemount>500):
			if thing.type=='bat' and thing.loaded==True:
				pass
			else:
				continue
		thing.loaded=True
		if thing.collide(rock):
			if thing.type=='sun':
				stuff.pop(stuff.index(thing))
				rock.number+=1
				continue
			else:
				rock.x=0
				rock.y=0
		if thing.type=='sun':
			arr=suns
		elif thing.type=='bat':
			arr=bats
			if thing.x>rock.x:
				thing.mom-=0.001
			else:
				thing.mom+=0.001
			if thing.y>rock.y:
				thing.vel-=0.001
			else:
				thing.vel+=0.001
			if thing.vel>.35:
				thing.vel=.35
			if thing.vel<-.35:
				thing.vel=-.35
			if thing.mom>.35:
				thing.mom=.35
			if thing.mom<-.35:
				thing.mom=-.35
		else:
			hello=False
			if not thing.collide(thing.mommy):
				thing.right=True
				thing.left=True
				for pp in blocks:
					if not (pp.x+pp.width-movemount<0 or pp.x-movemount>500 or pp.y+pp.height<thing.y):
						if thing.collide(pp):
							if thing.y//1+thing.height==pp.y//1:
								hello=True
								thing.mommy=pp
								break
			else:
				hello=True
				if thing.y//1+thing.height==thing.mommy.y:
					pass
				elif thing.height+thing.y>thing.mommy.y and thing.height+thing.y<thing.mommy.y+3:
					thing.y=thing.mommy.y-thing.height
				thing.right=True
				thing.left=True
			for pp in blocks:
				if not (pp.x+pp.width-movemount<0 or pp.x-movemount>500 or pp.y+pp.height<thing.y):
					if (thing.y//1>pp.y//1 and thing.y//1<pp.y//1+pp.height) or (thing.y//1<pp.y//1 and thing.y//1+thing.height>pp.y//1):
						if thing.x//1+thing.width==pp.x//1:
							thing.right=False
						if thing.x//1==pp.x//1+pp.width:
							thing.left=False
			if not hello:
				thing.vel+=0.001
			else:
				thing.vel=0
			if thing.x+thing.width<rock.x+rock.width:
				thing.mom=0.2
			elif thing.x>rock.x:
				thing.mom=-0.2
			else:
				thing.mom=0
			if thing.mom<0:
				arr=l_b
				old='l'
			elif thing.mom>0:
				arr=r_b
				old='r'
		imgg=arr[count//2]
		if thing.type=='beaver' and thing.mom<0.1 and thing.mom>-0.1:
			if old=='r':
				imgg=sr
			elif old=='l':
				imgg=sl
		if (thing.mom<0 and not thing.left) or (thing.mom>0 and not thing.right):
			thing.mom=0
		thing.x+=thing.mom
		thing.y+=thing.vel
		win.blit(imgg,(thing.x-movemount,thing.y))
		if thing.type=='beaver' and thing.y>hei:
			stuff.pop(stuff.index(thing))
	pygame.display.update()
	win.fill((44,44,162))
	if rock.mom>nom:
		rock.mom=nom
	if rock.mom<nom*-1:
		rock.mom=nom*-1
	dell+=1
	if dell%200==0:
		count+=haha
		if count==4 or count==0:
			haha*=-1
		elnum+=ppp
		if elnum==2 or elnum==0:
			ppp*=-1