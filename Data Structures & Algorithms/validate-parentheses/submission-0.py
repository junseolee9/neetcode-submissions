class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        paran = {')':'(', ']':'[', '}':'{'}
        for c in s:
            if c in paran:
                if stack and stack[-1] == paran[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack    
        