# TwoSum Solutions

This repository contains two different solutions for the TwoSum problem from LeetCode.

## Brute Force Solution

The brute force solution is located in the `TwoSum/BruteForce(On^2).py` file. This solution iterates over each element `x` and finds if there is another value that equals to `target - x`.

## Optimised Solution

The optimized solution is located in the `TwoSum/On.py` file. This solution uses a hash table to check for the complement of the current element in constant time.

## Usage

Each solution is encapsulated in a `Solution` class with a `twoSum` method. The method takes a list of integers (`nums`) and a target integer (`target`), and returns the indices of the two numbers such that they add up to `target`.

```python
sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
```
