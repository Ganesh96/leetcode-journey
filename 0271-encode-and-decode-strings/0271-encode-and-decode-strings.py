class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded = map(lambda word: f"{len(word)}:/{word}", strs)

        return ''.join(encoded)
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        decoded = []
        i = 0

        while i < len(s):
            delimiter_idx = s.find(':/', i)

            word_len = int(s[i:delimiter_idx])
            word_start = delimiter_idx + 2
            word_end = word_start + word_len

            decoded.append(s[word_start:word_end])

            i = word_end

        return decoded

        

        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))