import pygame
import keyboard
import time
from random import randrange
wid = 500
hei = 500
win = pygame.display.set_mode((wid, hei))
directions = {'right': [0.01, 0], 'left': [-0.01, 0]}
imgs = [
    pygame.image.load('flowey_1.png'),
    pygame.image.load('flowey_1_left.png'),
    pygame.image.load(
        'flowey_2.png'
    ),
    pygame.image.load('flowey_2_left.png'),
    pygame.image.load('flowey_3.png'),
    pygame.image.load('flowey_3_left.png')
]
count = 0
num = 0
no=0
haha = 2
blocknum = 0
suns = [pygame.image.load('sun_1.png'), pygame.image.load(
    'sun_2.png'), pygame.image.load('sun_1.png'), pygame.image.load('sun_2.png')]
bsuns = pygame.image.load('sun_1_no.png')
bats = [pygame.image.load('bat_down.png'), pygame.image.load(
    'bat_up.png'), pygame.image.load('bat_down.png'), pygame.image.load('bat_up.png')]
r_b = [pygame.image.load('racoon_1_left.png'), pygame.image.load('racoon_2_left.png'), pygame.image.load(
    'racoon_1_left.png'), pygame.image.load('racoon_2_left.png'), pygame.image.load('racoon_1_left.png'), pygame.image.load('racoon_2_left.png')]
l_b = [pygame.image.load('racoon_1.png'), pygame.image.load('racoon_2.png'), pygame.image.load(
    'racoon_1.png'), pygame.image.load('racoon_2.png'), pygame.image.load('racoon_1.png'), pygame.image.load('racoon_2.png')]
sl = pygame.image.load('racoon.png')
sr = pygame.image.load('racoon_left.png')
elephants = [[pygame.image.load('elephant_2.png'), pygame.image.load('elephant_1.png'), pygame.image.load
              ('elephant_3.png')], [pygame.image.load('elephant_2_right.png'), pygame.image.load
                                    ('elephant_1_right.png'), pygame.image.load('elephant_3_right.png')]]
elnum = 0
held = False
for l in elephants:
    for j in l:
        elephants[elephants.index(l)][l.index(
            j)] = pygame.transform.scale(j, (90, 60))

numy = 1

grasw = 40
grassh = 16


class player:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.mom = 0
        self.vel = 0
        self.grounded = True
        self.number = 0
        self.hp = 10
        self.max_hp = 10
        self.pot=2

    def move(self, val):
        global num
        self.mom += val[0]/5
        if val[0] > 0:
            num = 0
        elif val[0] < 0:
            num = 1


class block:
    def __init__(self, x, y, width=40, height=40, type1='grass'):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.sprite = []
        self.type = type1


class collectible:
    def __init__(self, x, y, type1, end=None, mom=0,width=None,height=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.type = type1
        self.mom = mom
        self.vel = 0
        self.loaded = False
        self.right = True
        self.left = True
        self.mommy = None
        self.end = end
        self.start = x
        self.ormom=mom
        if self.width==None:
            self.width=dimensions[type1][0]
            self.height=dimensions[type1][1]
    def collide(self, person):
        if (self.x > person.x and self.x< person.x+person.width) or (self.x < person.x and self.x+self.width > person.x):
            if (self.y >= person.y and self.y <= person.y+person.height) or (self.y <= person.y and self.y+self.height >= person.y):
                return True
            else:
                pass
        return False
dimensions={'sun':(50,50),'beaver':(82,42),'elephant':(90,60),'bat':(50,50)}
stuff = [collectible(430, 200, 'sun'), collectible(30, 100, 'sun'), collectible(630, 50, 'sun'), collectible(
    200, 200,'beaver'), collectible(700, 340, 'elephant', 900, -.1),collectible(900, 340, 'elephant', 700, .1),
    collectible(1000,100,'bat')]
blocks = [block(100, 320, 40, 40), block(100, 400, 1000, 20), block(
    500, 330, 70, 70, 'log'), block(430, 260, 70, 70, 'log'), block(410, 360, 10, 10)]
block__sprite = pygame.image.load('block.png')
log_sprite = pygame.image.load('log.png')
grassys = [pygame.image.load('grass_left.png'), pygame.image.load(
    'grass_middle.png'), pygame.image.load('grass_right.png')]
for i in blocks:
    if i.height == i.width:
        hurr = pygame.Surface(((i.width*0.9)//1, (i.height*0.9)//1))
    else:
        horny = i.width-(i.height*0.05*2)//1
        hurr = pygame.Surface((horny, (i.height*0.9)//1))
    if i.type == 'grass':
        hurr.fill((121, 85, 72))
        for offset in range(0, i.width+20, 20):
            hurr.blit(block__sprite, (offset, 0))
    else:
        for xset in range(0, i.width, 16):
            for yset in range(0, i.height, 16):
                hurr.blit(log_sprite, (xset, yset))
    extra = pygame.Surface((i.width, i.height))
    if i.height < i.width:
        extra.blit(hurr, ((i.height*0.05)//1, (i.height*0.05)//1))
    else:
        extra.blit(hurr, ((i.width*0.05)//1, (i.width*0.05)//1))
    data = [randrange(40, 100) for i in range(1000)]
    for grassy in grassys:
        datnum = 0
        omega = pygame.Surface((i.width, i.height+grassh))
        omega.fill((0, 16, 89))
        omega.blit(extra, (0, grassh))
        ohany = 0
        needed = data[0]
        for x in range(0, i.width):
            if x+16 > i.width or i.type != 'grass':
                break
            if x-ohany >= needed:
                ohany = x
                omega.blit(grassy, (x, 0))
                needed = data[datnum+1]
                datnum += 1
        i.sprite.append(omega)
rock = player(10, 20, 50, 50)
delay = 50
run = True
movemount = 0
camera = [0, 0]
tu = time.time()
c = 0
nom = 0.5
dell = 0
angle = 0
ppp = 1
hl = pygame.image.load('heart_left.png')
hr = pygame.image.load('heart_right.png')
nhl = pygame.image.load('heart_left_no.png')
nhr = pygame.image.load('heart_right_no.png')
y = 20
change = time.time()
for i in stuff:
    i.mommy = blocks[0]
invinc = time.time()-2
stuntime = time.time()-2
cropped = pygame.Surface((200, 50))
stun = 1
cropped.fill((0, 16, 89))
superr = True
full = pygame.image.load('full.png')
while run:
    if time.time()-stuntime >= 1 and stun == 0.125:
        stun = 1
        rock.mom = 0
    if True:
        x = 0
        cropped.fill((0, 16, 89))
        for i in range(3):
            dad = 50*(rock.number-i)
            cropped.blit(bsuns, (0+x, 0), (0, 0, 50, 50))
            if dad > 0:
                cropped.blit(suns[0], (0+x, 0), (0, 0, 50, (dad)//1))
            x += 60
        superr = False
    win.blit(cropped, (300, 50))
    if rock.number > 1:
        oldnum = rock.number
        rock.number -= 0.00005
        if oldnum//1 > rock.number//1:
            superr = True
    starttime = time.time()
    x = 20
    for i in range(rock.max_hp):
        if i < rock.hp:
            if i % 2 == 0:
                win.blit(hl, (x, y))
            else:
                win.blit(hr, (x, y))
        else:
            if i % 2 == 0:
                win.blit(nhl, (x, y))
            else:
                win.blit(nhr, (x, y))
        x += 18
    if rock.hp == 0:
        run = False
    if keyboard.is_pressed('space'):
        rock.vel = -0.5
    if keyboard.is_pressed('ctrl'):
        rock.mom *= 1.01
    if keyboard.is_pressed('alt'):
        rock.mom *= -1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if c % 2 == 0:
        for k, v in directions.items():
            if keyboard.is_pressed(k):
                rock.move(v)
                break
    c += 1
    on = False
    right = True
    left = True
    for blocky in blocks:
        if blocky.x+blocky.width-movemount < 0 or blocky.x > 500 or (blocky.y > rock.y+rock.height or blocky.y+blocky.height < rock.y):
            pass
        if rock.y//1 == blocky.y+blocky.height:
            if (rock.x < blocky.x and rock.x+rock.width-1 > blocky.x) or (rock.x < blocky.x+blocky.width and rock.x > blocky.x):
                rock.vel = .1
        if rock.y//1+rock.height == blocky.y//1:
            if (rock.x < blocky.x and rock.x+rock.width-1 > blocky.x) or (rock.x < blocky.x+blocky.width and rock.x > blocky.x):
                on = True
        if rock.x//1+rock.width == blocky.x:
            if (rock.y < blocky.y and rock.y+rock.height > blocky.y) or (rock.y > blocky.y and rock.y < blocky.y+blocky.height):
                right = False
        if rock.x//1 == blocky.x+blocky.width:
            if (rock.y+1 < blocky.y and rock.y+rock.height-1 > blocky.y) or (rock.y-1 > blocky.y and rock.y+1 < blocky.y+blocky.height):
                left = False
    if on:
        rock.grounded = True
        rock.vel = 0
    else:
        rock.grounded = False
    if rock.grounded:
        rock.mom *= 0.996
    else:
        rock.mom *= 0.9998
    if right and rock.mom >= 0:
        rock.x += (rock.mom+rock.mom*rock.number/20)*stun
    elif left and rock.mom <= 0:
        rock.x += (rock.mom+rock.mom*rock.number/20)*stun
    else:
        rock.mom = 0
    rock.vel += 0.0006
    if keyboard.is_pressed('up'):
        if rock.grounded and stun == 1:
            rock.vel = -0.4
            rock.grounded = False
            held = True
    else:
        if held and rock.vel < 0:
            held = False
            rock.vel *= 0.5
    if (not on) or rock.vel < 0:
        rock.y += rock.vel
    movemount = rock.x-(wid/2+rock.width/2)
    if movemount < 0:
        movemount = 0
    for blocky in blocks:
        if blocky.x+blocky.width-movemount < 0 or blocky.x > 500:
            continue
        hurr = blocky.x-movemount
        win.blit(blocky.sprite[blocknum], (hurr, blocky.y-grassh))
    if not(rock.mom < 0.01 and rock.mom > -0.01):
        win.blit(imgs[count+num], (rock.x-movemount, rock.y))
    else:
        win.blit(imgs[num], (rock.x-movemount, rock.y))
    for thing in stuff:
        if (thing.x+thing.width-movemount < 0 or thing.x-movemount > 500):
            if thing.type == 'bat' and thing.loaded == True:
                pass
            else:
                if thing.type=='elephant':
                    if thing.start+thing.width-movemount<0 or thing.start- movemount>500:
                        thing.x=thing.start
                        thing.mom=thing.ormom
                        continue
        thing.loaded = True
        if thing.collide(rock):
            if thing.type == 'sun':
                stuff.pop(stuff.index(thing))
                rock.number += 1
                continue
            else:
                if rock.y//1+rock.width-thing.y//1>-1 and rock.y//1+rock.width-thing.y//1<1 and rock.pot!=0:
                    if keyboard.is_pressed('up'):
                        rock.vel=-0.4
                    else:
                        rock.vel=-0.2
                    no=10
                    if rock.pot==3:
                        stuff.pop(stuff.index(thing))
                    if thing.type=='bat':
                        arr = bats
                    elif thing.type=='beaver':
                        if thing.mom < 0:
                            arr = l_b
                            old = 'l'
                        elif thing.mom > 0:
                            arr = r_b
                            old = 'r'
                    imgg = arr[count//2]
                    if thing.type == 'elephant':
                        imgg = arr[elnum]
                    if thing.type == 'beaver' and thing.mom < 0.1 and thing.mom > -0.1:
                        if old == 'r':
                            imgg = sr
                        elif old == 'l':
                            imgg = sl
                    win.blit(imgg, (thing.x-movemount, thing.y))
                    continue
                elif time.time()-invinc >= 2 and (no==0 or thing.y+thing.height<rock.y):
                    rock.hp -= 1
                    stuntime = time.time()
                    stun = 0.125
                    if rock.number - 1/8 > 0:
                        rock.number -= 1/8
                    else:
                        rock.number = 0
                    invinc = time.time()
        if thing.type == 'sun':
            arr = suns
        elif thing.type == 'bat':
            arr = bats
            if thing.x > rock.x:
                thing.mom -= 0.001
            else:
                thing.mom += 0.001
            if thing.y > rock.y:
                thing.vel -= 0.001
            else:
                thing.vel += 0.001
            if thing.vel > .35:
                thing.vel = .35
            if thing.vel < -.35:
                thing.vel = -.35
            if thing.mom > .35:
                thing.mom = .35
            if thing.mom < -.35:
                thing.mom = -.35
        elif thing.type == 'beaver':
            hello = False
            if not (thing.collide(thing.mommy) and thing.y//1+thing.height == pp.y//1 and ((thing.x//1 > thing.mommy.x//1 and thing.x//1 + 3 < thing.mommy.x//1+thing.mommy.width) or (thing.x//1 + 3 < thing.mommy.x//1 and thing.x//1+thing.width-3 > thing.mommy.x//1))):
                thing.right = True
                thing.left = True
                for pp in blocks:
                    if not (pp.x+pp.width-movemount < 0 or pp.x-movemount > 500 or pp.y+pp.height < thing.y):
                        if (thing.x//1> pp.x//1 and thing.x//1< pp.x//1+pp.width) or (thing.x//1 < pp.x//1 and thing.x//1+thing.width > pp.x//1):
                            if thing.y//1+thing.height == pp.y//1:
                                hello = True
                                thing.mommy = pp
                                break
            else:
                hello = True
                if thing.y//1+thing.height == thing.mommy.y:
                    pass
                elif thing.height+thing.y > thing.mommy.y and thing.height+thing.y < thing.mommy.y+3:
                    thing.y = thing.mommy.y-thing.height
                thing.right = True
                thing.left = True
            for pp in blocks:
                if not (pp.x+pp.width-movemount < 0 or pp.x-movemount > 500 or pp.y+pp.height < thing.y):
                    if (thing.y//1 > pp.y//1 and thing.y//1 < pp.y//1+pp.height) or (thing.y//1 < pp.y//1 and thing.y//1+thing.height > pp.y//1):
                        if thing.collide(pp):
                            thing.right = False
                        if thing.x//1 == pp.x//1+pp.width:
                            thing.left = False
            if not hello:
                thing.vel += 0.001
            else:
                thing.vel = 0
            if thing.x+thing.width < rock.x+rock.width:
                thing.mom = 0.4
            elif thing.x > rock.x:
                thing.mom = -0.4
            else:
                thing.mom = 0
            if rock.x-thing.x<100 and rock.x-thing.x>-100 and not rock.grounded:
                thing.mom/=4
            if thing.mom < 0:
                arr = l_b
                old = 'l'
            elif thing.mom > 0:
                arr = r_b
                old = 'r'
        elif thing.type == 'elephant':
            if thing.mom < 0:
                arr = elephants[0]
            else:
                arr = elephants[1]
            if thing.x//1 == thing.start or thing.x//1 == thing.end:
                thing.mom *= -1
                thing.x += thing.mom*10
            thing.x += thing.mom
        imgg = arr[count//2]
        if thing.type == 'elephant':
            imgg = arr[elnum]
        if (thing.mom < 0 and not thing.left) or (thing.mom > 0 and not thing.right):
            thing.mom = 0
        if thing.type == 'beaver' and thing.mom < 0.1 and thing.mom > -0.1:
            if old == 'r':
                imgg = sr
            elif old == 'l':
                imgg = sl
        thing.x += thing.mom
        thing.y += thing.vel
        win.blit(imgg, (thing.x-movemount, thing.y))
        if thing.type == 'beaver' and thing.y > hei:
            stuff.pop(stuff.index(thing))
    pygame.display.update()
    win.fill((0, 16, 89))
    if rock.mom > nom:
        rock.mom = nom
    if rock.mom < nom*-1:
        rock.mom = nom*-1
    dell += 1
    if time.time()-change >= 0.25:
        change = time.time()
        count += haha
        if count == 4 or count == 0:
            haha *= -1
        elnum += ppp
        blocknum += ppp
        if elnum == 2 or elnum == 0:
            ppp *= -1
        if rock.hp < rock.max_hp and rock.number > 2.5 and time.time()-invinc >= 1:
            rock.hp += 1
    if no!=0:
        no-=1