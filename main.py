def sum_list(l):
  s = 0
  for i in l:
    for j in i:
      s+=int(j)
  return s

