class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for st in strs:
            s += st
            s += '~'
        return s

    def decode(self, s: str) -> List[str]:
        lst = s.split('~')
        lst = lst[:-1]
        return list(lst)