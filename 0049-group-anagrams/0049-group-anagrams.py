import collections

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        
        # Step 1: Initialize a dictionary to store our groups.
        # Using defaultdict(list) is convenient because it automatically creates
        # an empty list for any new key we encounter.
        # The key will be the sorted string (our signature).
        # The value will be the list of anagrams for that signature.
        anagram_map = collections.defaultdict(list)

        # Step 2: Iterate through each word in the input list.
        for word in strs:
            
            # Step 2a: Calculate the signature for the current word.
            # We sort the characters of the word and join them back into a string.
            # This creates the canonical key. e.g., "tea" -> "aet"
            signature = "".join(sorted(word))
            
            # Step 2b: Use the signature to group the original word.
            # Append the original word to the list associated with its signature.
            anagram_map[signature].append(word)
            
        # Step 3: The values of our map are the lists of grouped anagrams.
        # We can simply return a list of these values.
        return list(anagram_map.values())