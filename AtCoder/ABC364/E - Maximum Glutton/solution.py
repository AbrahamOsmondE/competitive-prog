n, x, y = list(map(int, input().split()))

inf = float('inf')
dp = [[inf] * (y+1) for _ in range(n+1)]
dp[0][0] = 0

for i in range(1, n+1):
  a, b = map(int, input().split())
  for j in range(i-1, -1, -1):
    for k in range(b, y + 1):
      dp[j + 1][k] = min(dp[j+1][k], dp[j][k-b] + a)

for i in range(n, -1, -1):
  if min(dp[i]) <= x:
    print(min(n, i+1))
    exit()