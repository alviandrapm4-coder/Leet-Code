class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        word = s.split()
        mapPattern, mapWord = {}, {}
        if len(word) != len(pattern):
            return False
        for i in range(len(pattern)):
            a = pattern[i]
            b = word[i]
            if (a in mapPattern and mapPattern[a] != b) or (b in mapWord and mapWord[b] != a):
                return False

            mapPattern[pattern[i]] = word[i]
            mapWord[word[i]] = pattern[i]
        return True
