class Solution:
    def sequentialDigits(self, low: int, high: int) -> list[int]:
        digits = "123456789"
        result = list()

        for length in range(2,10):
            for start in range(0,10-length):
                number = int(digits[start:start+length])

                if low <= number <=high:
                    result.append(number)
        result.sort()
        return result