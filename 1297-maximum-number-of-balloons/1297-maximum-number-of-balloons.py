class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon_counts = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}
        
        for char in text:
            if char in balloon_counts:
                balloon_counts[char] += 1

        balloon_counts['l'] //= 2
        balloon_counts['o'] //= 2
        min_count = min(balloon_counts.values())
        return min_count