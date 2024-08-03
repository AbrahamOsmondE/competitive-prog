# D - AtCoder Janken 3
Link to problem: https://atcoder.jp/contests/abc365/tasks/abc365_d

# Solution

We iterate through the string.
At every index i, dp[i] will contain an array of length 3 where:
- dp[i][0] -> number of wins so far if we choose rock at index i
- dp[i][1] -> number of wins so far if we choose scissor at index i
- dp[i][2] -> number of wins so far if we choose paper at index i

Thus, to count these values, we check the character at index i

We will use an example where the character at index i == "R"

Since we are not allowed to lose, we will fill dp[i][1] (SCISSOR) with float("-inf") to ensure that when calculating dp[i+1], we will not use this value
```
dp[i][1] = float("inf")
```

dp[i][0] would mean picking Rock, and lead to a draw. If we pick rock now, we won't be allowed to pick rock previously. Thus, we will only be allowed to use the values for scissor and paper at dp[i-1]

```
dp[i][0] = max(dp[i-1][1], dp[i-1][2])
```

dp[i][1] would mean picking Paper, leading to a win. If we pick paper at index i, we are not allowed to pick paper at index i - 1. Thus, we use the maximum between scissor and rock at index i - 1

```
dp[i][2] = max(dp[i-1][0], dp[i-1][1]) + 1
```

We then repeat this for character == "S" and "P", modifying the logic a little bit.

The answer will be the maximum value inside the array dp[-1]