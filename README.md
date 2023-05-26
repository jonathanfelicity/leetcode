# leetcode
## ALGORITHMS
### EASY
1 **TWO NUMBER SUM**
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

```python
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_dict = {}  # Dictionary to store previously seen numbers
        
        for i, num in enumerate(nums):
            complement = target - num
            
            if complement in num_dict:
                return [num_dict[complement], i]
            
            num_dict[num] = i
        
        return []  # No pair found
 
```