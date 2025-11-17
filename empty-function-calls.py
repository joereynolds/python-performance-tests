import time

limit = 50_000_000

start = time.time()
for i in range(limit):
    pass

end = time.time()

duration = end - start
print('with no function call took ', duration)








def nothing():
    pass

start = time.time()
for i in range(limit):
    nothing()
end = time.time()
duration = end - start
print('null function call took ', duration)
