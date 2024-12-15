class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()  # Split the string into words
        reversed_words = words[::-1]  # Reverse the list of words
        return " ".join(reversed_words)  # Join the words with a single space