n = int(input())
s = input()

# R, S, P
dp = [[0,0,0] for _ in range(n + 1)]

for i in range(1, n + 1):
  curr = dp[i - 1]
  char = s[i - 1]
  if char == "R":
    dp[i] = [max(curr[1], curr[2]), 0, max(curr[0], curr[1]) + 1]
  elif char == "S":
    dp[i] = [max(curr[1], curr[2]) + 1, max(curr[0], curr[2]), 0]
  else:
    dp[i] = [0,  max(curr[0], curr[2]) + 1, max(curr[0], curr[1])]

print(max(dp[-1]))