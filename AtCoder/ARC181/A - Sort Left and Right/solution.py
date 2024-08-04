T = int(input())

for i in range(T):
  N = int(input())
  arr = list(map(int, input().split()))
  if sorted(arr) == arr:
    print(0)
    continue
  
  currSum = 0
  flag = True
  for index, num in enumerate(arr):
    valid = index*(index+1)//2 == currSum
    if index + 1 == num and valid:
      print(1)
      flag = False
      break
    
    currSum += num
  if flag and arr[-1] == 1 and arr[0] == len(arr):
    print(3)
  elif flag:
    print(2)