import os

def hash(v: str):
  curr_val = 0
  for c in v:
    curr_val = ((curr_val + ord(c)) * 17) % 256
  return curr_val

with open(os.path.join('day15', 'input.txt'), 'r') as f:
  m = f.read().strip().split(',')
  boxes = {}
  to_num = 0
  for s in m:
    if '-' in s:
      vals = s.split('-')
      to_num = hash(vals[0])
      if to_num in boxes.keys():
         for i, v in enumerate(boxes[to_num]):
           if vals[0] in v:
             del boxes[to_num][i]
             break
    elif '=' in s:
      vals = s.split('=')
      to_num = hash(vals[0])
      focal_length = vals[1]
      if to_num in boxes.keys():
         found = False
         for i, v in enumerate(boxes[to_num]):
           if vals[0] in v:
             found = True
             break

         if found:
          boxes[to_num][i] = ' '.join(vals)
         else:
          boxes[to_num].append(' '.join(vals))
      else:
        boxes[to_num] = [' '.join(vals)]
  
  total_focusing_power = 0
  for k in boxes:
    box_num = (1 + k)
    if(len(boxes[k])) > 0:
      print(boxes[k])
      for i, lens in enumerate(boxes[k]):
        total_focusing_power = total_focusing_power + box_num * (1 + i) * int(lens.split()[1])
  print(total_focusing_power)