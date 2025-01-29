from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change_count = {5: 0, 10: 0}
        for bill in bills:
            if bill == 5:
                change_count[5] += 1
            elif bill == 10:
                if change_count[5] > 0:
                    change_count[5] -= 1
                    change_count[10] += 1
                else:
                    return False
            else:
                if change_count[10] > 0 and change_count[5] > 0:
                    change_count[10] -= 1
                    change_count[5] -= 1
                elif change_count[5] >= 3:
                    change_count[5] -= 3
                else:
                    return False
        return True
