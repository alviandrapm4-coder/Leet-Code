class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        l = 0
        r = 0

        while l < len(haystack):
            if haystack[l] == needle[r]:
                l += 1
                r += 1
            else:
                l = l - r + 1
                r = 0

            if r == len(needle):
                return l - r

        return -1