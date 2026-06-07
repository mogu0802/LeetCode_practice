'''
要in-place不能用stack 要用替換的
'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return False
        num_1 = 1                           ###第一個數字[0]一定會是對的 不用管
        for num_2 in range(1,len(nums)):
            if nums[num_2] != nums[num_2-1]:###不等於代表是對的數字
                nums[num_1] = nums[num_2]  ###把他搬到對的位置
                num_1 += 1
        return num_1        