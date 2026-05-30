class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} #字典:{數字: 位置}
        for i, num in enumerate(nums): #enumerate()可以記錄這是(第幾個[索引])、(是甚麼[值])
            total = target - num #找到另一個數字是多少
            if total in seen :
                return [seen[total], i]
            seen[num] = i
#### 先從第一個a開始 拿來減target得出還差多少 接著去seen裡面找有沒有 沒有就把a存在seen中並紀錄位置i

"""
暴力解法 時間複雜度是O(n^2) 因為要檢索兩輪
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
"""
