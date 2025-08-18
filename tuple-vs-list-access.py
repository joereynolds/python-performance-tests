import time


my_list  = [1,2,3,4,5]
my_tuple = (1,2,3,4,5)

start = time.time()
for i in range(50000000):
    a = my_list[1]
end = time.time()
duration = end - start
print('list access took ', duration)


start = time.time()
for i in range(50000000):
    a = my_tuple[1]
end = time.time()
duration = end - start
print('tuple access took ', duration)
