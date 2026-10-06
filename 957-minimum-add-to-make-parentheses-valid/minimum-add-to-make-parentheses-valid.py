class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_count = 0
        need_add = 0
        
        for c in s:
            if c == '(':
                open_count += 1
            else:  # c == ')'
                if open_count > 0:
                    open_count -= 1
                else:
                    need_add += 1
        
        return open_count + need_add

        