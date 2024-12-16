class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 7 1 5 3 6 4
        # 0-6+4-2+3-2 = +4+3 = 7

        # 1 2 3 4 5
        # 0+1+1+1+1 = 4

        # 7 6 4 3 1
        # 0-1-2-1-2 = 0

        # 30, 76, 12, 98, 55, 1, 88, 42, 67, 35
        # 0 +46 - 64+86-43-54+87-46+25-32 = 46+86+87+25 = 244
        profit = 0
        index = 1
        L = len(prices)
        while(index<L):
            delta_profit = prices[index] - prices[index-1]
            if delta_profit>0:
                profit+=delta_profit
            index+=1
        return profit