Day 25:  
405. Convert a Number to Hexadecimal
===
Problem
---
Given an integer, write an algorithm to convert it to hexadecimal. For negative integer, two’s complement method is used.

Note:

All letters in hexadecimal (a-f) must be in lowercase.
The hexadecimal string must not contain extra leading 0s. If the number is zero, it is represented by a single zero character '0'; otherwise, the first character in the hexadecimal string will not be the zero character.
The given number is guaranteed to fit within the range of a 32-bit signed integer.
You must not use any method provided by the library which converts/formats the number to hex directly.
    
    Example 1:
    
    Input:
    26
    Output:
    "1a"
    
    Example 2:
    Input:
    -1
    Output:
    "ffffffff"

Testcase
---
    26
    -27
    0
    -1
    268435455
    -268435456

Solution
---
### 1
```python=
class Solution:
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num >= 0:
            return self.postive_convert_hexadecimal(num)
        else: # num < 0
            num = num*-1 -1
            ans = self.postive_convert_hexadecimal(num)
            tmp = '0'*(8-len(ans)) + ans
            ans = ''
            for char in tmp:
                ans += self.h_to_rh[char]
            i = 0
            for _ in range(7):  # the last char need to keep whatever it is '0' or not
                if ans[0] == '0':
                    ans = ans[1:]
                else:
                    break
            return ans
            
    def postive_convert_hexadecimal(self, num):
        ans = ''
        if num == 0:
            return '0'
        while num > 0:
            num, r = divmod(num, 16)
            ans = self.d_to_h[r] + ans
        return ans
    
    d_to_h = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    h_to_rh = {'0': 'f', '1': 'e', '2': 'd', '3': 'c', '4': 'b', '5': 'a', '6': '9', '7': '8', 
              '8': '7', '9': '6', 'a': '5', 'b': '4', 'c': '3', 'd': '2', 'e': '1', 'f': '0'}
```
一開始沒搞懂題目要求  
誤用了divmod  
而且不知道其實電腦內建負數存法就是就是2補數  
其實可以直接用位元操作來解

### 2
```python=
class Solution:
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        d_to_h = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f')
        ans = ''
        if num == 0:
            return '0'
        while len(ans) < 8 and num != 0:
            ans = d_to_h[num & 15] + ans
            num = num >> 4
        return ans
```
直接用位元操作來解

* Time complexity : O(log(n))
* Space complexity : O(1)
