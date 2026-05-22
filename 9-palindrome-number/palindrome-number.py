class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        #alviandrapiero
        num = str(x)
        if num.startswith('-'):
            nums = [-int(num[1])] + [int(d) for d in num[2:]]
        else:
            nums = [int(d) for d in num]
        return num == num[::-1]