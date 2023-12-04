import os

def numMatch(s: str, forward: bool):
  nums_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
  }
  for k in nums_dict:
    if(forward and k in s):
      return nums_dict[k]
    if(not forward and k in s[::-1]):
      return nums_dict[k]
  return None
    



with open(os.path.join('day1', 'input2.txt'), 'r') as f:
  t = 0
  for line in f.readlines():
    i = 0
    for c in line:
      if c.isnumeric():
        num1 = c
        break
      if line[i+1].isnumeric():
        num1 = line[i+1]
        break
      if line[i+2].isnumeric():
        num1 = line[i+2]
        break
      if numMatch(line[i:i+5], forward=True):
        num1 = numMatch(line[i:i+5], forward=True)
        break
      i+=1
    j = 0
    reversed = line[::-1]
    for c in reversed:
      if c.isnumeric():
        num2 = c
        break
      if reversed[j+1].isnumeric():
        num2 = reversed[j+1]
        break
      if reversed[j+2].isnumeric():
        num2 = reversed[j+2]
        break
      if numMatch(reversed[j:j+5], forward=False):
        num2 = numMatch(reversed[j:j+5], forward=False)
        break
      j+=1
    t += int(num1 + num2)
  print(t)