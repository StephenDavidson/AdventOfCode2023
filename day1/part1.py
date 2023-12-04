import os

with open(os.path.join('day1', 'input1.txt'), 'r') as f:
  t = 0
  for line in f.readlines():
    for c in line:
      if c.isnumeric():
        num1 = c
        break
    for c in line[::-1]:
      if c.isnumeric():
        num2 = c
        break
    t += int(num1 + num2)
  print(t)