class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[' : #opening
                stack.append(s[i])
            else: #closing
                if len(stack) == 0:  #no opening but closing bracket
                    return False
                if (
                    (stack[-1] == '(' and s[i] ==')') or
                    (stack[-1] == '{' and s[i] == '}') or
                    (stack[-1] == '[' and s[i] == ']')
                ):
                    stack.pop()
                else:
                    return False
        return len(stack) == 0




        
            
        