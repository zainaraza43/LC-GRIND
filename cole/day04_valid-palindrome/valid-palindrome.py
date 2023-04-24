# beats 88.23%

import re
from math import ceil
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub('[^a-z0-9]', '', s.lower())
        return s[:len(s)//2] == s[ceil(len(s)/2):][::-1]
        
if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome('zainniaz'))
    print(s.isPalindrome('A man, a plan, a canal: Panama'))
    print(s.isPalindrome(' '))