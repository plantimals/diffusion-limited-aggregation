#!/usr/bin/env python

import png
import randomwalk
import itertools
import random

p_x = 300
p_y = 300
on_square = 255

def is_near(point, platten):
  x,y = point
  if x < 1 or x >= p_x - 1 or y < 1 or y >= p_y - 1:
    return False
  right = platten[x + 1][y] == on_square
  up = platten[x][y + 1] == on_square
  left = platten[x - 1][y] == on_square
  down = platten[x][y - 1] == on_square
  return right or up or left or down

def get_start():
  x = random.randrange(-p_x,2*p_x)
  y = random.randrange(-p_y,2*p_y)

def get_grey(x):
  return 255 if x == 1 else 0

def write_png(platten):
  f = open('dla.png', 'wb')      # binary mode is important
  w = png.Writer(p_x, p_y, greyscale=True)
  w.write(f, platten)
  f.close()

platten = []
for _ in range(p_y):
  platten.append(list(itertools.repeat(0,p_x)))
platten[int(p_x/2)][int(p_y/2)]=on_square

for n in range(100000):
  x,y = get_start()
  rw = randomwalk.RandomWalk(x,y)
  while rw.count < 1000:
    rw.iterate()
    if is_near((rw.x,rw.y), platten):
      platten[rw.x][rw.y] = on_square
      break
  #print "{0}, {1}".format(rw.x, rw.y)


#for row in platten:
#  print "".join([str(x) for x in row])

write_png(platten)
