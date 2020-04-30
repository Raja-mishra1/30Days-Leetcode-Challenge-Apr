class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        move_l = 0 
        len_str = len(s)
        for dir , amt in shift:
            if dir == 0:
                move_l = move_l + amt
            else:
                move_l -= amt
        move_l = move_l % len_str
        return  s[move_l:] + s[:move_l]