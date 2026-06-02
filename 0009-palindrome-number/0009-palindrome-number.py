class Solution:
    def isPalindrome(self, x: int) -> bool:
        change_x = str(x)                   ###先存成字串
        return change_x == change_x[::-1]   ##檢查反過來讀是否相同