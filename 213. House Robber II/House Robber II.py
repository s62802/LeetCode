 class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        elif len(nums) == 1 or len(nums) == 2:
            return max(nums)
        # line is easy than circle, so turn this question to line
        # consider index 0 means not consider index -1 -> 0 ~ len(nums)-2
        # not consider index 0 -> 1 ~ len(nums)-1
        return max(self.rob_line(0, len(nums)-2, nums), self.rob_line(1, len(nums)-1, nums))
        
    def rob_line(self, start, end, nums):
        f = [0]*3
        f[start%3] = nums[start]
        f[(start+1)%3] = max(nums[start], nums[start+1])
        for i in range(start+2, end+1):
            f[i%3] = max(f[(i-1)%3], f[(i-2)%3] + nums[i])
        return max(f[0], f[1], f[2])
