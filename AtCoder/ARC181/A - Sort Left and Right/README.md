# A - Sort Left and Right
Link to problem: https://atcoder.jp/contests/arc181/tasks/arc181_a

# Solution
When pressing an integer at index i, all elements below element i will be sorted in ascending order, and all elements above i will be sorted in ascending order. The output can only be 0, 1, 2 or 3.

1. Answer is 0
When the array is already sorted, then we do not need to perform any operation

2. Answer is 1
We iterate through the array. We try to find an element X where index + 1 is equal X (which means that the element is in the correct position), and we check if all elements prior to X is less than X and all elements after X is greater than X 

This means if we perform the operation with k = X, the output will be a sorted array

To efficiently check this, we can simply keep track of the current sum of elements so far. Then we use the arithmetic sum formula to verify the sum is correct

3. Answer is 2
For every array, if we aim to put 1 in position 0 or put N in the last position. On the next step, if we select either 1 or N as k, then the resulting array will be sorted

4. Answer is 3
If N is in position 0, and 1 is in the last position, we need to spend an extra move to shift both of them outside of the edge position. Only then can we follow similar logic to when Answer is 2