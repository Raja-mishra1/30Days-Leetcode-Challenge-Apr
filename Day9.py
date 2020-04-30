class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        answer = ''
        answer_2 = ''
        for i in S:
            if i == '#':
                answer = answer[:-1]
            else:
                answer += i
        
        for i in T:
            if i == '#':
                answer_2 = answer_2[:-1]
            else:
                answer_2 += i
        return answer == answer_2