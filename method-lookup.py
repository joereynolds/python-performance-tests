import time


class Thing:
    def do(self):
        pass


thing = Thing()
limit = 50000000


start = time.time()
for i in range(limit):
    thing.do()
end = time.time()
duration = end - start
print('direct call took ', duration)


y = thing.do
start = time.time()
for i in range(limit):
    y()
end = time.time()
duration = end - start
print('lookup call took ', duration)
