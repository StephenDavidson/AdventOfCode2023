import os

def hash(v: str):
  curr_val = 0
  for c in v:
    curr_val = ((curr_val + ord(c)) * 17) % 256
  return curr_val

with open(os.path.join('day15', 'input.txt'), 'r') as f:
  m = f.read().strip().split(',')
  print(sum([hash(s) for s in m]))