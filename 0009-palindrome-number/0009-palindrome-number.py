class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x !=0):    ### X不能為負 個位數也不能為0 但0是Palindrome
            return False
        else:
            ori_num = x                         ###存初始值
            new_num = 0                         ###用來存相反後的值
            while x >0:
                last_num = x % 10               ###找尾數
                new_num =  new_num*10+last_num  ###把尾數放到頭
                x = x//10                       ###確定x還有沒有值
            return new_num == ori_num           ###是不是palindrome

'''換成字串的寫法 
           change_x = str(x)                   ###先存成字串
        return change_x == change_x[::-1]   ##檢查反過來讀是否相同
'''
       
            