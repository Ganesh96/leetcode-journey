from collections import deque
class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.w = width
        self.h = height
        self.food = food
        self.food_index = 0
        self.points = 0

        self.snake = deque([(0,0)])
        self.s_set = set([(0,0)])
        self.cardinals = {
            'U':(-1,0),
            'D':(1,0),
            'R':(0,1),
            'L':(0,-1)
        }

    def move(self, direction: str) -> int:
        r,c = self.snake[0]
        new_r, new_c = self.cardinals[direction]
        new_r, new_c = new_r+r , new_c+c
        if not(0<=new_r<self.h and 0<=new_c<self.w):
            return -1
        tail = self.snake.pop()
        self.s_set.remove(tail)

        if (new_r,new_c) in self.s_set:
            return -1

        if(self.food_index < len(self.food) and new_r == self.food[self.food_index][0] and new_c == self.food[self.food_index][1]):
            self.food_index+=1
            self.points+=1
            self.snake.append(tail)
            self.s_set.add(tail)
        self.snake.appendleft((new_r,new_c))
        self.s_set.add((new_r,new_c))
        return self.points


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)