class Solution:
    def intToRoman(self, num: int) -> str:
        
        hash_table = {
            1: "I",
            2: "II",
            3: "III",
            4: "IV",
            5: "V",
            6: "VI",
            7: "VII",
            8: "VIII",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M",
        }

        if num <= 0 or num >= 4000:
            return ""
    
        string = str(num)
        index = len(string)-1
        result = []
        i = 0

        while index >= 0:
            i += 1
            digit = int(string[index])

            if i == 1:
                if digit != 0:
                    result.append(hash_table[digit])
        
            elif i == 2: #decenas

                if digit >= 1 and digit <= 3:
                    aux = ""
                    for j in range(digit):
                        aux += "X"
                
                    result.insert(0, aux)
            
                elif digit == 4:
                    result.insert(0, "XL")
            
                elif digit >= 5 and digit <= 8:
                    aux = "L"
                    for j in range(5, digit):
                        aux += "X"
                    result.insert(0, aux)
                elif digit == 9:
                    result.insert(0, "XC")
        
            elif i == 3:

                if digit >= 1 and digit <= 3:
                    aux = ""
                    for j in range(digit):
                        aux += "C"
                    result.insert(0, aux)
            
                elif digit == 4:
                    result.insert(0, "CD")
            
                elif digit >= 5 and digit <= 8:
                    aux = "D"
                    for j in range(5, digit):
                        aux += "C"
                    result.insert(0, aux)
            
                elif digit == 9:
                    result.insert(0, "CM")
        
            else:

                if digit >= 1 and digit <= 3:
                    aux = ""
                    for j in range(digit):
                        aux += "M"
                    result.insert(0, aux)
            
            index -= 1
            
        res = "".join(list(result))
        return res