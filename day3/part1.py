import os

with open(os.path.join('day3', 'input.txt'), 'r') as f:
  sum_nums = 0
  m = [line.strip() for line in f.readlines()]
  for line_index, l in enumerate(m):
    hasChecked = False
    for char_index, c in enumerate(l):
      if not c.isnumeric():
        hasChecked = False  
      if c.isnumeric() and not hasChecked:
        # find full number
        numstring = ''
        i = char_index
        while True:
          numstring += l[i]
          i+=1
          if i >= len(l):
            break
          if not l[i].isnumeric():
            break

        # check for symbols
        symbolFound = False
        for inc in range(len(numstring)):
          start = char_index-1+inc
          end = char_index+2+inc
          if line_index > 0:
            for p in m[line_index-1][start:end]:
              if not p.isalnum() and p != '.':
                symbolFound = True
          if line_index < len(m)-1:
            for p in m[line_index+1][start:end]:
              if not p.isalnum() and p != '.':
                symbolFound = True
          for p in m[line_index][start:end]:
              if not p.isalnum() and p != '.':
                symbolFound = True
          if(symbolFound):
            sum_nums += int(numstring)
            break

        hasChecked = True
  print(sum_nums)