import math
import random


def print_2darray(arrs):
  for arr in arrs:
    print(arr)


def strech(encode):
  data = encode[0]
  for i in range(1, len(encode)):
    for j in range(0, len(encode[i])):
      data.append(encode[i][j])
  return data


def calculate_range(big_range, small_ranges, correct):
  # print("calculate_range")
  bf, bt = big_range
  new_range = []

  if correct:
    for small_range in small_ranges:
      sf, st = small_range
      if bf[0] <= sf[0] and bt[0] >= st[0]:
        # print("a")
        if (bf[0] == sf[0]):
          # print("1")
          new_range = [[st[0] + 1, bf[1]], [bt[0], bt[1]]]
          break
        else:
          # print("2")
          new_range = [[bf[0], bf[1]], [sf[0] - 1, bt[1]]]
          break

      if bf[1] <= sf[1] and bt[1] >= st[1]:
        # print("b")
        if (bf[1] == sf[1]):
          # print("1")
          new_range = [[bf[0], st[1]] + 1, [bt[0], bt[1]]]
          break
        else:
          # print("2")
          new_range = [[bf[0], bf[1]], [bt[0], sf[1] - 1]]
          break

  else:
    for small_range in small_ranges:
      sf, st = small_range
      if bf[0] <= sf[0] and bt[0] >= st[0]:
        new_range = [[sf[0], bf[1]], [st[0], bt[1]]]
        break
      if bf[1] <= sf[1] and bt[1] >= st[1]:
        new_range = [[bf[0], sf[1]], [bt[0], st[1]]]
        break

  return new_range


def set_range(range, x, y, n, correct):
  # print("set_range")
  incorrect_range = []
  # print(range, x, y, correct)
  if (y == 0):
    gap = x
    nx = x
    while nx < n:
      from_cell = [nx, 0]
      to_cell = [nx + gap - 1, n - 1]
      incorrect_range.append([from_cell, to_cell])
      nx += gap * 2
  else:
    gap = y
    nx = y
    while nx < n:
      from_cell = [0, nx]
      to_cell = [n - 1, nx + gap - 1]
      incorrect_range.append([from_cell, to_cell])
      nx += gap * 2
  # print(incorrect_range)
  range = calculate_range(range, incorrect_range, correct)
  return range


def check_paraty_bit(x, y, encode):
  # print("check_paraty_bit")
  n = len(encode)

  even = 1
  if (x == 0 and y == 0):
    for i in range(0, n):
      for j in range(0, n):
        if (encode[i][j] == 1):
          even *= -1

    if (even == 1):
      return True
    else:
      return False

  else:
    if y == 0:
      gap = x
      nx = x
      while nx < n:
        for j in range(0, gap):
          for i in range(0, n):
            # print(i, nx, j, encode)
            if (encode[i][nx + j] == 1):
              even *= -1
        nx += gap * 2
    else:
      gap = y
      nx = y
      while nx < n:
        for j in range(0, gap):
          for i in range(0, n):
            if (encode[nx + j][i] == 1):
              even *= -1
        nx += gap * 2

    if (even == 1):
      return True
    else:
      return False


def set_paraty_bit(x, y, encode):
  n = len(encode)
  if (x == 0 and y == 0):
    lc = int(((5 + (math.log2(n) - 2) * 2) - 1) / 2)
    even = 1
    for i in range(0, lc):
      j = int(pow(2, i))
      if (encode[0][j] == 1):
        even *= -1
      if (encode[j][0] == 1):
        even *= -1

    if (even == 1):
      encode[y][x] = 1
    else:
      encode[y][x] = 0

  else:
    even = [1, 1]
    gap = x
    nx = x
    while nx < n:
      for j in range(0, gap):
        for i in range(0, n):
          # print(i, x + j)
          if (encode[i][nx + j] == 1):
            even[0] *= -1
          if (encode[nx + j][i] == 1):
            even[1] *= -1
      # print("even:", even)
      nx += gap * 2

    if (even[0] == 1):
      encode[y][x] = 0
    else:
      encode[y][x] = 1

    if (even[1] == 1):
      encode[x][y] = 0
    else:
      encode[x][y] = 1

  return encode


def encode(data):
  # initialize
  data_size = len(data)
  k = 0
  while (data_size > (pow(2, 2 * k) - (5 + (k - 2) * 2))):
    k += 1

  n = pow(2, k)
  size = pow(n, 2)
  paraty_bit_amount = 5 + (k - 2) * 2
  # print("k:", k, "n:", n, "size:", size, "paraty_bit_amount:",
  #       paraty_bit_amount)

  # fill data
  while (data_size < (size - paraty_bit_amount)):
    data.append(0)
    data_size = len(data)
  # print("expanded data:", data)

  # make 2d array
  encode = []
  for i in range(0, n):
    temp = []
    for j in range(0, n):
      temp.append(0)
    encode.append(temp)

  # print("empty 2d arr:")
  # print_2darray(encode)

  # load data
  count = 0
  for y in range(0, n):
    for x in range(0, n):
      if (x == 0 and y == 0):
        pass
      elif (x == 0 and math.log2(y) == int(math.log2(y))):
        pass
      elif (y == 0 and math.log2(x) == int(math.log2(x))):
        pass
      else:
        encode[y][x] = data[count]
        count += 1
  # print("fill in data:")
  # print_2darray(encode)

  # set_paraty_bit
  i = int(paraty_bit_amount / 2) - 1
  while (i >= 0):
    pbp = int(pow(2, i))
    # print("set paraty bit:")
    encode = set_paraty_bit(pbp, 0, encode)
    # print_2darray(encode)
    i -= 1
  # print("set paraty bit:")
  encode = set_paraty_bit(0, 0, encode)

  return strech(encode)


def decode(data):
  n = int(math.sqrt(len(data)))
  # print("n:", n)
  # turn 1d to 2d
  encode = []
  for i in range(0, n):
    temp = []
    for j in range(0, n):
      temp.append(data[i * n + j])
    encode.append(temp)
  # print_2darray(encode)

  pb0 = check_paraty_bit(0, 0, encode)

  k = math.log2(n)
  paraty_bit_amount = 5 + (k - 2) * 2
  err_area = [[0, 0], [n - 1, n - 1]]
  # print(err_area)

  # check
  i = int(paraty_bit_amount / 2) - 1
  while (i >= 0):
    pbp = int(pow(2, i))
    cr = check_paraty_bit(pbp, 0, encode)
    if (pb0 and not cr):
      print("more than 1 error")
      break
    err_area = set_range(err_area, pbp, 0, n, cr)
    # print(err_area)

    cr = check_paraty_bit(0, pbp, encode)
    if (pb0 and not cr):
      print("more than 1 error")
      break
    err_area = set_range(err_area, 0, pbp, n, cr)
    # print(err_area)
    i -= 1

  if (err_area[0] != err_area[1]):
    print("program error")
  else:
    if (err_area[0] == [0, 0]):
      print("no error")
      return strech(encode)
    else:
      x = err_area[0][0]
      y = err_area[0][1]
      print("error at:", x, y)
      if (encode[x][y]):
        encode[y][x] = 0
      else:
        encode[y][x] = 1

      return strech(encode)


def error():
  num = random.randint(0, 50)
  if num == 0:
    return True
  else:
    return False


def transmition(data):
  for i in range(0, len(data)):
    if (error()):
      if (data[i]):
        data[i] = 0
      else:
        data[i] = 1
  return data


data = "00110001110"
ndata = []
for i in range(0, len(data)):
  ndata.append(int(data[i]))

print("input data     : ", ndata)

ndata = encode(ndata)
print("encoded data   : ", ndata)

ndata = transmition(ndata)
print("transmited data: ", ndata)

ndata = decode(ndata)
print("decoded data   : ", ndata)
