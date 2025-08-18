import time

limit = 10000

start = time.time()
for i in range(limit):
    a = [x +1 for x in range(10000)]
end = time.time()
duration = end - start
print('comprehension took ', duration)

start = time.time()
for i in range(limit):
    a = []
    app = a.append
    for x in range(10000):
        app(x+1)
end = time.time()
duration = end - start
print('for took ', duration)



