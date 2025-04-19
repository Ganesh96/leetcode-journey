class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money < children:
            return -1
        
        combos = min(money//8,children)
        for c in range(combos,-1,-1):
            change = money - c * 8
            child = children - c
            if child == 0:
                if change ==0:
                    return c
                else:
                    continue
            if change < child: # hanles atleast 1dollar
                continue
            if change == 4 and child == 1: # checks change is 4 for one person
                continue

            return c
        return -1
