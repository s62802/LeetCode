Day 19:  
75. Sort Colors
===
## Problem
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?

## Testcase
    [2,0,2,1,1,0]
    []
    [0,0,0]
    [0,1,1,0]
    [2,2,1,1]
    [0,2,0,2]
    [0,1]
    [1,2,0]

## Solution

### 1 
    class Solution:
        def sortColors(self, nums):
            """
            :type nums: List[int]
            :rtype: void Do not return anything, modify nums in-place instead.
            """
            for num in [1,2]:
                back = 0
                for i in range(len(nums)):
                    if nums[i-back] == num:
                        nums.remove(num)
                        nums.append(num)
                        back += 1
偷吃步解
remove &  append 不算 in-place algorithm

### 2

    class Solution:
        def sortColors(self, nums):
            """
            :type nums: List[int]
            :rtype: void Do not return anything, modify nums in-place instead.
            """
            l = len(nums)
            start = 0
            for i in [0,1]:
                c, nc = start, start
                while True:
                    while c < l and nums[c] != i:
                            c += 1
                    while nc < l and nums[nc] == i:
                            nc += 1
                    if c >= l or nc >= l:
                        break
                    if nc < c:
                        nums[c], nums[nc] = nums[nc], nums[c]
                        start = nc + 1
                    else:
                        start = c + 1
                        c += 1

這題卡很久，感覺為了跳指針寫太複雜，交換那邊也有點複雜，還有第二次迴圈的start
看其他人好像都是nc&c從0開始，只要c對就換，交換nc才+1，如果寫成one-pass就沒有start的問題了

### 3
    class Solution:
        def sortColors(self, nums):
            """
            :type nums: List[int]
            :rtype: void Do not return anything, modify nums in-place instead.
            """
            h, i, t = 0, 0, len(nums)-1

            while i <= t:
                if nums[i] == 0:
                    nums[h], nums[i] = nums[i], nums[h]
                    i += 1
                    h += 1
                elif nums[i] == 1:
                    i += 1
                elif nums[i] == 2:
                    nums[i], nums[t] = nums[t], nums[i]
                    t -= 1
參考別人的one-pass code
這題要很細心，很多判斷式或+=寫錯大部分case還是會過
Time complexity : O(n)
Space complexity : O(1)
