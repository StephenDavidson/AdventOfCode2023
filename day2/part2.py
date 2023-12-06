import os

with open(os.path.join('day2', 'input.txt'), 'r') as f:
  p_sum = 0
  for line in f.readlines():
    splitlines = line.split(':')
    id = int(splitlines[0].split(' ')[1])
    games_map = {
      "red": 0,
      "blue": 0,
      "green": 0
    }
    games = list(map(lambda x: x.split(','), splitlines[1].split(';')))
    impossible = False
    for game in games:
      for color in game:
        cleaned = color.strip().split(" ")
        if(int(cleaned[0]) > games_map[cleaned[1]]):
          games_map[cleaned[1]] = int(cleaned[0])
    powers = 1
    for k in games_map:
      powers = powers * games_map[k]
    p_sum += powers
  print(p_sum)