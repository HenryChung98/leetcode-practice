dict = {
    "]": "[",
    "}": "{",
    ")": "("
}


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
        # If the character is a closing bracket
            if char in dict:
                # Pop the top element from the stack (if the stack is not empty), otherwise assign a dummy value
                top_element = stack.pop() if stack else '#'
                
                # Check if the popped element matches the corresponding opening bracket
                if dict[char] != top_element:
                    return False
            else:
                # If it's an opening bracket, push it onto the stack
                stack.append(char)

    # In the end, the stack should be empty if the string is valid
        return not stack

sol = Solution()
print(sol.isValid("{{()}"))

