class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for elo in strs:
            els = "".join(sorted(elo))
            ans[els].append(elo)
        return list(ans.values())
                    