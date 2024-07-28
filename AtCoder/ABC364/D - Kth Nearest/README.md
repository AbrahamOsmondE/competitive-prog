# D - Kth Nearest
Link to problem: https://atcoder.jp/contests/abc364/tasks/abc364_d

## Problem Description
![Screenshot 2024-07-28 at 11 53 42 PM](https://github.com/user-attachments/assets/2b790210-3eb1-4655-b219-079f3894ce55)

## Solution
A solution for this problem is to use binary search. For each b, we can perform a binary search on array A to find the correct distance.

We perform a sort on A. Then we set the left to be 0, as the difference cannot be less than 0, and we set the right to be 
the greatest distance, which can be obtained by subtracting b from 
A[0] and A[-1] and getting the greater result.

To determine whether we take the left or the right side of the array, we can use the following

```
# x is the current distance we are on
def total_within_dist(b, x):
  left = bisect.bisect_left(A, b - x)
  right = bisect.bisect_right(A, b + x)
  return right - left
```

The above function outputs the number of points Ai that is between b - x and b + x. If this number is less than k, it means that the correct distance must be on the right side of the array. Otherwise, it is on the left side.
