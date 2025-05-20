class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_tank = 0
        curr_tank = 0
        start_index = 0

        for i in range(len(gas)):
            fuel_gain = gas[i] - cost[i]
            total_tank += fuel_gain
            curr_tank += fuel_gain

            if curr_tank < 0:
                # Can't reach station i+1, reset start
                start_index = i + 1
                curr_tank = 0

        return start_index if total_tank >= 0 else -1
