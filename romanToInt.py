class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        num = 0
        for i in range(len(s)):

            if i + 1 < len(s):
                if s[i] == "I":
                    if s[i + 1] == "V" or s[i + 1] == "X":
                        num -= 1
                        continue
                
                if s[i] == "X":
                    if s[i + 1] == "L" or s[i + 1] == "C":
                        num -= 10
                        continue
                
                if s[i] == "C":
                    if s[i + 1] == "D" or s[i + 1] == "M":
                        num -= 100
                        continue

            
            num += dict[s[i]]
            
        return num


sol = Solution()
print(sol.romanToInt('MCMXCIV'))