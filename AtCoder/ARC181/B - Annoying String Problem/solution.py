t = int(input())

def gcd(a,b):
  if a == 0:
    return b
  return gcd(b % a, a)

def lcm(a,b):
  return (a // gcd(a, b)) * b

for _ in range(t):
  S = input()
  X = input()
  Y = input()
  
  # The solution is derived from the fact that the order of 1 and 0 does not matter.
  countx0 = X.count("0")
  countx1 = X.count("1")
  county0 = Y.count("0")
  county1 = Y.count("1")
  
  newX = ""
  newY = ""
  
  count0diff = countx0 - county0
  count1diff = countx1 - county1
  
  if count0diff == 0:
    print("Yes")
    continue
  elif count0diff > 0:
    newX = "0" * count0diff
  else:
    newY = "0" * (count0diff * -1)
  
  if count1diff > 0:
    newX = "1" * (count1diff)
  else:
    newY = "1" * (count1diff * -1)
  
  if len(newX) == 0 or len(newY) == 0:
    print("No")
    continue
  
  stringWith0 = newX if count0diff > 0 else newY
  stringWith1 = newX if count1diff > 0 else newY
  
  lenLcm = lcm(len(stringWith0), len(stringWith1))
  
  multipleOfS = lenLcm // len(stringWith0)

  # S needs to be a string that can be split into multipleOfS equal parts
  if len(S) % multipleOfS != 0:
    print("No")
    continue
  
  lenOfPart = len(S) // multipleOfS
  if S[:lenOfPart] * multipleOfS == S:
    print("Yes")
  else:
    print("No")
  