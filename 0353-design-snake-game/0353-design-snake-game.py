class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.snake = [[0, 0]]
        self.width = width
        self.height = height
        self.food = food
        self.move_map = {"U": [-1, 0], "D": [1, 0], "L": [0, -1], "R": [0, 1]}
        self.score = 0

    def move(self, direction: str) -> int:
        r, c = self.move_map[direction]
        # get the new head and tail
        head = self.snake[0]
    
        new_head = [head[0] + r, head[1] + c]
        # find the food
        if len(self.food) > 0 and new_head == self.food[0]:
            self.food.pop(0)
            self.score += 1
        else:
            # move the tail
            self.snake.pop()
            if new_head[0] < 0 or new_head[0] >= self.height or new_head[1] < 0 or new_head[1] >= self.width:
                return -1
            elif new_head in self.snake:
                return -1
        
        self.snake.insert(0, new_head)
        
        return self.score
            

            


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)