class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        denoms = [amount+1] * (amount+1)
        denoms[0] = 0
        for v in range(1,amount+1):
            for coin in coins:
                if coin<=v:
                    denoms[v] = min(denoms[v],denoms[v-coin]+1)
        return denoms[amount] if denoms[amount]!= amount+1 else -1