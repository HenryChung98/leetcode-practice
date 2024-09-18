class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        splitSentence = s.split(" ")

        for word in reversed(splitSentence):
            if word:
                return len(word)

sol = Solution()
word = "Hello World"
print(sol.lengthOfLastWord(word))