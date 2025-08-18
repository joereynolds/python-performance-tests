from enum import Enum
import time

class Direction(Enum):
    LEFT = (-1, 0)

class Velocity:
    LEFT = (-1, 0)

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def going_left(self) -> bool:
        return self.x == -1 and self.y == 0

velocity = Velocity(-1, 0)

start = time.time()
for i in range(50000000):
    if velocity.going_left():
        pass
end = time.time()
duration = end - start
print('class method comparison took ', duration)

start = time.time()
for i in range(50000000):
    if (velocity.x, velocity.y) == Direction.LEFT.value:
        pass
end = time.time()
duration = end - start
print('enum comparison took ', duration)

start = time.time()
for i in range(50000000):
    if (velocity.x, velocity.y) == Velocity.LEFT:
        pass
end = time.time()
duration = end - start
print('class constant comparison took ', duration)

start = time.time()
for i in range(50000000):
    if velocity.x == -1 and velocity.y == 0:
        pass
end = time.time()
duration = end - start
print('inline comparison took ', duration)
