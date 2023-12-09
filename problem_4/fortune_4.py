# arr = [3, 4, -1, 1]
# arr = [1, 2, 0]
arr = [3, 1, 2]
n = len(arr)

def process(idx, met):
  idx -= 1
  if idx in met:
    return
  if not (0 <= idx <= n - 1): # not indexable
    arr[idx] = -1
    return
  if arr[idx] == idx + 1: # same as index, do nothing
    return
  process(arr[idx], met | {idx})
  arr[idx] = idx + 1

for i in range(n):
  process(arr[i], set())

for i in range(n):
  if arr[i] != i+1:
    print("ans", i+1)
    break
else:
  print("ans", n+1)

