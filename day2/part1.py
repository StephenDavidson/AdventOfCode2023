import os

with open(os.path.join('day2', 'input.txt'), 'r') as f:
  id_sum = 0
  for line in f.readlines():
    splitlines = line.split(':')
    id = int(splitlines[0].split(' ')[1])
    maxes = {
      "red": 12,
      "blue": 14,
      "green": 13
    }
    games = list(map(lambda x: x.split(','), splitlines[1].split(';')))
    impossible = False
    for game in games:
      for color in game:
        cleaned = color.strip().split(" ")
        if(int(cleaned[0]) > maxes[cleaned[1]]):
          impossible  = True
          break
    if(not impossible):
      id_sum += id
  print(id_sum)