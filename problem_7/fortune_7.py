def ways(x):
  if len(x) == 1: return x != '0'
  if len(x) == 2: return (int(x) <= 26) + (ways(x[0]) and ways(x[1]))
  return ways(x[:-2]) * (int(x[-2:]) <= 26) + ways(x[:-1]) * ways(x[-1])

print (ways('111'))
