from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        base = strs[0]
        prefix = ""

        if len(strs) <= 1 or strs[0] == "":
            return base

        for i in range(1, len(strs)):
            check = ""
            for j in range(len(base)):
                try:
                    if base[j] == strs[i][j]:
                        check += strs[i][j]
                    
                    else:
                        prefix = ""
                        prefix = check
                        break
                except:
                    pass

            base = check
        prefix = check
        return prefix


sol = Solution()
print(sol.longestCommonPrefix(["aaa","aa","aaa"]))