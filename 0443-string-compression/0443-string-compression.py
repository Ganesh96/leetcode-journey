class Solution:
    def compress(self, chars: List[str]) -> int:
        read = write = 0
        n = len(chars)

        while read < n:
            curr = chars[read]
            count = 1
            read+=1
            while read < n and chars[read] == curr:
                read += 1
                count += 1

            chars[write] = curr
            write+=1
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write+=1
        return write