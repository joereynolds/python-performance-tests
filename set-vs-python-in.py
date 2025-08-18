import time



my_list  = [1,2,3,4,5]
my_set = {1,2,3,4,5}

start = time.time()
for i in range(50000000):
    if i in my_list:
        continue
end = time.time()
duration = end - start
print('list access took ', duration)


start = time.time()
for i in range(50000000):
    if i in my_set:
        continue
end = time.time()
duration = end - start
print('set access took ', duration)
