class Solution:
    def calculateScore(self, instructions: List[str], values: List[int]) -> int:
        L = len(instructions)
        visited = set()
        score, index = 0, 0
        
        while(0<=index <L and index not in visited):
            visited.add(index)
            if(instructions[index] == "add"):
                score+=values[index]
                index+=1
            elif(instructions[index]=="jump"):
                index+=values[index]
        return score