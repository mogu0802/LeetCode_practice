'''
 把羅馬數字換成數字代號?1234567 如果出現前一個數字小於就用減的?
 先檢查是否都是羅馬數字?
'''
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_num = {'I':1,
                     'V':5,
                     'X':10,
                     'L':50,
                     'C':100,
                     'D':500, 
                     'M':1000}
        total = 0                                       ###計算數值
        for i in range(len(s)-1):                       ###不能判斷到大於長度
            if roman_num[s[i]] < roman_num[s[i+1]]:     ###左邊小於右邊要用減的
                total -= roman_num[s[i]]
            else:                                       ###左邊大於右邊正常計算
                total += roman_num[s[i]]
        total += roman_num[s[-1]]                       ###把最後一個字加上
        return total

