class Solution:
    def nearestValidPoint(self, x: int, y: int, points: list[list[int]]) -> int:
        min_distance = float('inf')
        result_index = -1

        # Iterate through each point with its original index.
        for i, (px, py) in enumerate(points):
            # Step 1: Check if the point is valid.
            if px == x or py == y:
                # Step 2: Calculate the Manhattan distance.
                distance = abs(x - px) + abs(y - py)
                
                # Step 3: If this point is closer, update our result.
                if distance < min_distance:
                    min_distance = distance
                    result_index = i
        
        return result_index