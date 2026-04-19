class Solution:
    def isPalindrome(self, s: str) -> bool:
        p1 = 0
        p2 = len(s)-1

        p1_isalnum = False
        p2_isalnum = False
        while(p1 < p2):
            p1_isalnum = s[p1].isalnum()
            p2_isalnum = s[p2].isalnum()
            if (p1_isalnum and p2_isalnum):
                if s[p1].lower() != s[p2].lower():
                    return False
                p1+=1
                p2-=1
            if not p1_isalnum:
                p1+=1
            if not p2_isalnum:
                p2-=1
        return True
            
        

    