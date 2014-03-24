#!/usr/bin/env python

import png
import randomwalk
import itertools
import random

p_x = 1000
p_y = 1000
on_square = 255

def is_near(point, platten):
  x,y = point
  if x < 1 or x >= p_x - 1 or y < 1 or y >= p_y - 1:
    return False
  right = platten[x + 1][y] == on_square
  up = platten[x][y + 1] == on_square
  left = platten[x - 1][y] == on_square
  down = platten[x][y - 1] == on_square
  q1 = platten[x + 1][y + 1] == on_square
  q2 = platten[x - 1][y + 1] == on_square
  q3 = platten[x - 1][y - 1] == on_square
  q4 = platten[x + 1][y - 1] == on_square
  return right or up or left or down or q1 or q2 or q3 or q4

def get_start():
  x = random.randrange(0,p_x)
  y = random.randrange(0,p_y)
  return (x,y)

def get_grey(x):
  return 255 if x == 1 else 0

def write_png(platten):
  f = open('dla.png', 'wb')      # binary mode is important
  w = png.Writer(p_x, p_y, greyscale=True)
  w.write(f, platten)
  f.close()

platten = []
for _ in range(p_y):
  f = on_square if _ == p_y - 1 else 0
  platten.append(list(itertools.repeat(f,p_x)))

for n in range(10000):
  rw = randomwalk.RandomWalk(p_x,p_y)
  while not is_near((rw.x,rw.y), platten):
    rw.iterate()
  platten[rw.x][rw.y] = on_square
  #print "{0}, {1}".format(rw.x, rw.y)


#for row in platten:
#  print "".join([str(x) for x in row])

write_png(platten)
