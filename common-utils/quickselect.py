import random
arr = []
def partition(left, right, pivot):
  arr[right], arr[pivot] = arr[pivot], arr[right]

  curr = left
  for i in range(left, right):
    if arr[i] < arr[pivot]:
      arr[curr], arr[i] = arr[i], arr[curr]
    curr += 1
  
  arr[right], arr[curr] = arr[curr], arr[right]

  return curr

def quickselect(left, right):
  if left == right:
    return
  
  pivot = random.randint(left, right)
  pivot = partition(left, right, pivot)
  quickselect(left, pivot - 1)
  quickselect(pivot + 1, right)
