n, q = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
import bisect

# x is current distance
def total_within_dist(b, x):
  left = bisect.bisect_left(A, b - x)
  right = bisect.bisect_right(A, b + x)
  return right - left
  
for _ in range(q):
  b, k = map(int, input().split())
  mini = 0
  # The maximum possible distance would either be from b to minimum A or maximum A
  maxi = max(abs(b - A[0]), abs(b - A[-1]))
  
  while mini < maxi:
    mid = (mini + maxi) // 2
    if total_within_dist(b, mid) >= k:
      maxi = mid
    else:
      mini = mid + 1

  print(mini)
