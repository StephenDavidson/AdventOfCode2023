import os

with open(os.path.join('day3', 'input.txt'), 'r') as f:
  star_dict = {}
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
            
            for pos, p in enumerate(m[line_index-1][start:end]):
              pos += start
              if p == '*':
                curr_line = line_index-1
                if(curr_line in star_dict.keys()):
                  if(pos in star_dict[curr_line].keys()):
                    star_dict[curr_line][pos].append(numstring)
                  else:
                    star_dict[curr_line][pos] = [numstring]
                else:
                  star_dict[curr_line] = {pos: [numstring]}
                symbolFound = True
          if line_index < len(m)-1:
            for pos, p in enumerate(m[line_index+1][start:end]):
              pos += start
              if p == '*':
                curr_line = line_index+1
                if(curr_line in star_dict.keys()):
                  if(pos in star_dict[curr_line].keys()):
                    star_dict[curr_line][pos].append(numstring)
                  else:
                    star_dict[curr_line][pos] = [numstring]
                else:
                  star_dict[curr_line] = {pos: [numstring]}
                symbolFound = True
          for pos, p in enumerate(m[line_index][start:end]):
              pos += start
              if p == '*':
                curr_line = line_index
                if(curr_line in star_dict.keys()):
                  if(pos in star_dict[curr_line].keys()):
                    star_dict[curr_line][pos].append(numstring)
                  else:
                    star_dict[curr_line][pos] = [numstring]
                else:
                  star_dict[curr_line] = {pos: [numstring]}
                symbolFound = True
          if(symbolFound):
            break
        hasChecked = True
  
  total = 0
  for row in star_dict.keys():
    for pos in star_dict[row].keys():
      if (len(star_dict[row][pos]) == 2):
        total += int(star_dict[row][pos][0])*int(star_dict[row][pos][1])
  print(total)