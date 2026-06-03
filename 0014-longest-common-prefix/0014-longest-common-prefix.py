'''
用for迴圈? 從第一個的第一個字母開始 如果有就進入for迴圈開始找下一個直到出現不同?
'''
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:                                                ###沒有就回傳空字串
            return ""
        for i in range(len(strs[0])):                               ###拿第一個單字的字母當基準
            for j in range(1, len(strs)):                           ###確定要檢查的字串有幾個
                if i >= len(strs[j]) or strs[j][i] != strs[0][i]:   ###如果基準大於檢查長度或不相同了就停
                    return strs[0][:i]
        return strs[0]                                              ###全部檢查完就是第一個單字
