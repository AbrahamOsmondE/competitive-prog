# D - Iroha and a Grid (ABC 042)
Link to problem: https://atcoder.jp/contests/abc042/tasks/arc058_b
Relevant problem: https://leetcode.com/problems/unique-paths/

## Problem Description

<img width="1128" alt="Screenshot 2024-07-28 at 12 13 00 AM" src="https://github.com/user-attachments/assets/cd80a8a4-3961-4aa7-ae7a-b1077ae13b93">

## Solution
One solution is to subtract the total number of unique paths for the W x H grid with the total number of paths in which we traverse through
the forbidden cells. To illustrate, we will use the example input 

```
7 5 3 2
```

Where -> W = 7, H = 5, B = 3, A = 2

To calculate the number of unique paths where we traverse through the forbidden cells to reach the bottom right, we can observe that there 
are B = 3 different ways that we can "enter" the forbidden cells.

<img width="327" alt="Screenshot 2024-07-28 at 12 17 46 AM" src="https://github.com/user-attachments/assets/8136bb8f-3caa-4703-bc81-6ae20d148afe">

For each entry point, we can easily calculate the number of unique paths to reach that particular entry, we could simply utilize the combinatorial
solution for the Leetcode Unique Paths problem

<img width="343" alt="Screenshot 2024-07-28 at 12 21 34 AM" src="https://github.com/user-attachments/assets/6222f8f8-ba85-422c-9179-ae353b2ea31c">

```
// For a grid of with width W and height H, the total number of unique paths to go from top left to bottom right being able to only go right and down is:
combination(W + H - 2, H)
```

Then from each entry point, we simply use a similar logic to calculate how many ways can we go from the entrypoint to the finish line.

The pseudocode solution would be the following:
```
total = combination(W + H - 2, H - 1)
for b from 0 - B:
  // Values:
  // Height of start_to_entry_point grid = H - A
  // Width of start_to_entry_point grid = b + 1
  // Height of entry_point_to_finish grid = A
  // Width of entry_point_to_finish = W - b

  start_to_entry_point_paths = combination((H - A - 1) + (b + 1 - 1), (b + 1 - 1))
  entry_point_to_finish_paths = combination(W - b - 1 + (A - 1) + (b + 1 - 1), w - b - 1)
  total -= start_to_entry_point_paths * entry_point_to_finish_paths
print(total)
```

https://github.com/user-attachments/assets/d6684aa0-f9c7-40bb-b8a2-8810a301aac2


