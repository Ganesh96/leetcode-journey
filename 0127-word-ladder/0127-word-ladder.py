import collections

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        
        # Step 1: Pre-processing. An essential check and building the adjacency list.
        # If endWord isn't in the list, a path is impossible.
        # A set provides O(1) lookups.
        word_set = set(wordList)
        if endWord not in word_set:
            return 0

        # Build a map from generic words to real words for efficient neighbor finding.
        a_list = collections.defaultdict(list)
        for word in word_set:
            for i in range(len(word)):
                generic_word = f"{word[:i]}*{word[i+1:]}"
                a_list[generic_word].append(word)

        # Step 2: Initialize data structures for BFS.
        # A queue to hold the words to visit and their current path length (level).
        queue = collections.deque([(beginWord, 1)])
        # A set to track visited words to avoid cycles and redundant work.
        visited = {beginWord}

        # Step 3: Begin the BFS traversal.
        while queue:
            # Dequeue the word at the front of the line.
            current_word, level = queue.popleft()
            
            # Step 3a: Find all possible neighbors by generating generic words.
            for i in range(len(current_word)):
                generic_word = f"{current_word[:i]}*{current_word[i+1:]}"
                
            #     # Step 3b: Process each neighbor found in our map.
                for neighbor in a_list[generic_word]:
            #         # If we found the target, we're done. Return the next level.
                    if neighbor == endWord:
                        return level + 1
                    
            #         # If we haven't visited this neighbor yet...
                    if neighbor not in visited:
            #             # ...mark it as visited and add it to the queue.
                        visited.add(neighbor)
                        queue.append((neighbor, level + 1))
                        
        # Step 4: If the queue empties and we never reached the endWord, no path exists.
        return 0