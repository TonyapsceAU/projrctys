import math
import random

puk = int(input('number: \n'))


def method11(n, acuracy):
  count = 0
  ld = 0
  g = (math.ceil(n / 2))
  k = (math.ceil(g / 2))
  g2 = g * g
  while (round(g2, acuracy) != n):
    print(g, g2, k)
    count += 1
    if (round(g2, acuracy) > n):
      if (ld == 2):
        k = k * 1.9
      elif (ld == 1):
        k = k * 0.5
      g = g - k
      ld = 1

    else:
      if (ld == 1):
        k = k * 0.1
      elif (ld == 2):
        k = k * 1.5
      g = g + k
      ld = 2
    g2 = g * g
  return g, count


def method12(n, acuracy):
  count = 0
  ld = 0
  g = (math.ceil(n / 2))
  k = (math.ceil(n / 3))
  g2 = g * g
  while (round(g2, acuracy) != n):
    print(g, g2, k)
    count += 1
    if (round(g2, acuracy) > n):
      if (ld == 2):
        k = k * 1.9  #can twike
      elif (ld == 1):
        k = k * 0.5
      g = g - k
      ld = 1

    else:
      if (ld == 1):
        k = k * 0.1  #can twike
      elif (ld == 2):
        k = k * 1.5
      g = g + k
      ld = 2
    g2 = g * g
  return g, count


def method3(start, end, target, acuracy, count):
  count += 1
  mid = start + math.ceil((end + start) / 2)
  if (round(mid * mid, acuracy) == target):
    return mid, count

  if (round(mid * mid, acuracy) < target):
    return method3(mid, end, target, acuracy, count)
  else:
    return method3(start, mid, target, acuracy, count)


# puk = int(random.randint(1, 100))
# for puk in range(1, 100):

acu = 1
a, c = method11(puk, acu)
# a, c = method3(0, puk / 2, puk, acu, 0)
print("n:", puk, "ans:", "{:.{}f}".format(a, acu), "count:", c)
