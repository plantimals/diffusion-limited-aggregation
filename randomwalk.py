#!/usr/bin/env python

import random

class RandomWalk:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.count = 0

  def iterate(self):
    if random.random() > 0.5:
      self.y = self.y + 1 if random.random() > 0.5 else self.y - 1
    else:
      self.x = self.x + 1 if random.random() > 0.5 else self.x - 1
    self.count += 1

  def point(self):
    return (self.x, self.y)
