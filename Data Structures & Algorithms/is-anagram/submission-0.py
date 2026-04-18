class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dict = {}
        
        for i in s:
            if i not in s_dict:
                s_dict[i] = 1
            else:
                s_dict[i] +=1
        
        t_dict = {}

        for i in t:
            if i not in s_dict:
                return False
            if i not in t_dict:
                t_dict[i] = 1
            else:
                t_dict[i] +=1
            if t_dict[i] > s_dict[i]:
                return False
        return True
            

    