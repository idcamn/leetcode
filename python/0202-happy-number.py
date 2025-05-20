class Solution:
    def isHappy(self, n: int) -> bool:
        answers = []
        numbers = list(str(n))
        answer = 0
        while answer != 1:
            plus = 0
            for num in numbers:
                plus += int(num) ** 2
            answer = plus
            if answer in answers:
                return False
            answers.append(answer)
            numbers = list(str(answer))
        return True