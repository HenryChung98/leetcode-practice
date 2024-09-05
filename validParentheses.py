class Solution:
    def isValid(self, s: str) -> bool:
        is_valid = True

        dict = {
            "[": "]",
            "{": "}",
            "(": ")"
        }
        for i in range(len(s)):

            try:
                if s[len(s) - 1 - i] != dict[s[i]] and s[i + 1] != dict[s[i]]:
                    is_valid = False
            except:
                print('not in dict')
                pass
        return is_valid


sol = Solution()
print(sol.isValid("[])"))