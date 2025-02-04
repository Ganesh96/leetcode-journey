class Codec:
    def encode(self, strs):
        return '\U0001f926‍♂️'.join(strs)
        
    def decode(self, s):
        return s.split('\U0001f926‍♂️')