class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        matching_bracket = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in matching_bracket:
                if stack and stack[-1] == matching_bracket[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return not stack







    



  

