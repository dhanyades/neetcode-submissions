class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        box = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                num = board[r][c]
                b = (r//3) * 3 +(c//3)
                if num == '.':
                    continue

                if num in rows[r] or num in columns[c] or num in box[b]:
                    return False
                rows[r].add(num)
                columns[c].add(num)
                box[b].add(num)
        return True