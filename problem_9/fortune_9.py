# arr = [2, 4, 6, 2, 5]
arr = [5, 1, 1, 5]

for idx, val in enumerate(arr):
  if idx >= 3: arr[idx] = max(arr[idx], arr[idx] + arr[idx-2], arr[idx] + arr[idx-3])
  elif idx >= 2: arr[idx] = max(arr[idx], arr[idx] + arr[idx-2])
print(max(arr[-2:]))
