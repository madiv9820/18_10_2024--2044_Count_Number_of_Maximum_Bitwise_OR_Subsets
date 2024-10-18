# 2044. Count Number of Maximum Bitwise-OR Subsets

__Type__: Medium <br>
__Topics:__ Array, Backtracking, Bit Manipulation, Enumeration <br>
__LeetCode Link:__ [Count Number of Maximum Bitwise-OR Subsets](https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/description/) <br>
__Reference Video:__ [Count Number of Maximum Bitwise-OR Subsets - Leetcode 2044 - Python](https://youtu.be/_wBj3IMV7tY)
<hr>

Given an integer array `nums`, find the __maximum__ possible __bitwise OR__ of a subset of `nums` and return _the __number of different non-empty subsets__ with the maximum bitwise OR_.

An array `a` is a __subset__ of an array `b` if `a` can be obtained from `b` by deleting some (possibly zero) elements of `b`. Two subsets are considered different if the indices of the elements chosen are different.

The bitwise OR of an array `a` is equal to `a[0] OR a[1] OR ... OR a[a.length - 1]` __(0-indexed)__.
<hr>

### Examples

- __Example 1:__ <br>
__Input:__ nums = [3,1] <br>
__Output:__ 2 <br>
__Explanation:__ The maximum possible bitwise OR of a subset is 3. There are 2 subsets with a bitwise OR of 3:<br> - [3] <br> - [3,1]

- __Example 2:__ <br>
__Input:__ nums = [2,2,2] <br>
__Output:__ 7 <br>
__Explanation:__ All non-empty subsets of [2,2,2] have a bitwise OR of 2. There are 2<sup>3</sup> - 1 = 7 total subsets.

- __Example 3:__ <br>
__Input:__ nums = [3,2,1,5] <br>
__Output:__ 6 <br>
__Explanation:__ The maximum possible bitwise OR of a subset is 7. There are 6 subsets with a bitwise OR of 7: <br> - [3,5] <br> - [3,1,5] <br> - [3,2,5] <br> - [3,2,1,5] <br> - [2,5] <br> - [2,1,5]
<hr>

### Constraints:
- `1 <= nums.length <= 16`
- <code>1 <= nums[i] <= 10<sup>5</sup></code>
<hr>

### Hints:
- Can we enumerate all possible subsets?
- The maximum bitwise-OR is the bitwise-OR of the whole array.