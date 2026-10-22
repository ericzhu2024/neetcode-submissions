class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0

        for n in bills:
            if n == 5:
                five += 1
            elif n == 10:
                if five > 0:
                    five -= 1
                    ten += 1
                else:
                    return False
            else:
                total = 15
                if ten > 0:
                    total -= 10
                    ten -= 1
                while total > 0 and five > 0:
                    total -= 5
                    five -= 1
                if total != 0:
                    return False
        return True

