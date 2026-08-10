class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        limit = min(strs, key=len)
        lst = list(limit)
        for i,s in enumerate(lst):
            for elt in strs:
                if limit == elt:
                    if i == len(ans) and elt[i] == s:
                        ans += s
                    continue
                if s == elt[i]:
                    if i < len(ans) and ans[i] == s:
                        continue
                    else:
                        ans += s
                else:
                    if i < len(ans) and ans[i] != elt[i]:
                        ans = ans[:-1]
                    return ans
        return ans

