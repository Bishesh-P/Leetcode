class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word = s.split()
        last_word = word[-1]
        return len(last_word)
        