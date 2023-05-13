class Block:

  def __init__(self, x, y, w, m, v, xc):
    self.x = x
    self.y = y
    self.w = w
    self.v = v
    self.m = m
    self.xConstraint = xc

  def hitWall(self):
    return self.x <= 0

  def reverse(self):
    self.v *= -1

  def collide(self, other):
    return not (self.x + self.w < other.x or self.x > other.x + other.w)

  def bounce(self, other):
    sumM = self.m + other.m
    newV = (self.m - other.m) / sumM * self.v
    newV += (2 * other.m / sumM) * other.v
    return newV

  def update(self):
    self.x += self.v

  def show(self):
    rect = (self.x, self.y, self.w, self.w)
    fill = (0, 0, 0)
    return fill, rect
