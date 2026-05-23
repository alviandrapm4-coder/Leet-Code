class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        res = []
        for word in words:
            mapP, mapW = {}, {}
            is_match = True
        
            for p, w in zip(pattern, word):
                if (p in mapP and mapP[p] != w) or (w in mapW and mapW[w] != p):
                    is_match = False
                    break
                mapW[w] = p
                mapP[p] = w
            if is_match:
                res.append(word)
        return res