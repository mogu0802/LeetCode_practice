class Solution:
    def isValid(self, s: str) -> bool:
        find_list = {")":"(", "]": "[", "}": "{"} 
        symbol = []                                         ###待配對區
        for i in s:                                     
            if i in find_list:                              ###如果是右括號找左括號配對
                top_symbol = symbol.pop() if symbol else "" ###找找有沒有可以配對的 沒有就給一個"""
                if find_list[i] != top_symbol:              ###不符合括號組合
                    return False
            else:                                           ###左括號存起來等待配對
                symbol.append(i)
        return not symbol                                   ###如果裡面沒東西會回傳False加上not就變True了(有東西相反)