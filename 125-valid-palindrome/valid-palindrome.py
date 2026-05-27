class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        sLow = s.lower()
        sFilter = []
        for char in sLow:
            if ('a' <= char <= 'z') or ('0' <= char <= '9'):
                sFilter.append(char)
        return sFilter == sFilter[::-1]