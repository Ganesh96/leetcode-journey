# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
         # Helper function to calculate the number of matching letters at the same positions
        def letterMatches(word1, word2):
            matches = 0
            for i in range(len(word1)):
                if word1[i] == word2[i]:
                    matches += 1
            return matches

        # Precompute match scores between all pairs of words
        scoreMap = {word: {} for word in words}  
        for word1 in words:
            for word2 in words:
                score = letterMatches(word1, word2)
                scoreMap[word1][word2] = score

        candidates = words[:]
        while candidates:
            # Step 1: Evaluate each word as a potential guess
            bucketSizes = {}
            for guess in candidates:
                # Calculate the size of the largest bucket for this guess
                matchBuckets = {}
                for word in candidates:
                    score = scoreMap[guess][word]
                    if score not in matchBuckets:
                        matchBuckets[score] = 0
                    matchBuckets[score] += 1
                bucketSizes[guess] = max(matchBuckets.values())

            # Step 2: Choose the word with the smallest largest bucket size
            guessWord = min(bucketSizes, key=bucketSizes.get)

            # Step 3: Make the guess
            score = master.guess(guessWord)
            if score == 6:  # Secret word found
                return

            # Step 4: Filter candidates based on the match score with the guessed word
            candidates = [
                word for word in candidates if scoreMap[guessWord][word] == score
            ]