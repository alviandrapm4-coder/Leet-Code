class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        word = s.split()
        lastWord = word[-1]
        return len(lastWord)