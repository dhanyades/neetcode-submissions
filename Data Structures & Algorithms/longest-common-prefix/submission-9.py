class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        limit = min(strs, key=len)
        lst = list(limit)
        for i,s in enumerate(lst):
            for elt in strs:
                if elt[i] != s:
                    return ans
            ans += s
        return ans

