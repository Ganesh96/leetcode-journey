class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded = map(lambda word: f"{len(word)}:/{word}",strs)
        return ''.join(encoded)
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        decoded = []
        index = 0
        while index < len(s):
            delimiter = s.find(':/',index)
            L = int(s[index:delimiter])
            word = s[delimiter+2:delimiter+2+L]
            decoded.append(word)
            index = delimiter +2 + L
        return decoded      

        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))