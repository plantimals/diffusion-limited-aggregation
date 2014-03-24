#!/usr/bin/env python

import random

class RandomWalk:
  def __init__(self, x, y):
    self.p_x = x
    self.p_y = y
    self.count = 0
    self.reset_location()

  def iterate(self):
    if random.random() > 0.5:
      self.y = self.y + 1 if random.random() > 0.5 else self.y - 1
    else:
      self.x = self.x + 1 if random.random() > 0.5 else self.x - 1
    self.count += 1
    if self.out_of_bounds():
      self.reset_location()

  def point(self):
    return (self.x, self.y)

  def reset_location(self):
    self.x = random.randrange(0,self.p_x)
    self.y = random.randrange(0,self.p_y)

  def out_of_bounds(self):
    if self.x < 0 or self.x > self.p_x:
      return True
    if self.y < 0 or self.y > self.p_y:
      return True
    return False
