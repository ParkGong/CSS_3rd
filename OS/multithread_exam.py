import threading
from functools import reduce

g_result = 0

def thread_main(*args):
    global g_result
    res = reduce(lambda a, b: a + b, args)
    g_result += res

n = 10000
offset = n // 4

li = [i for i in range(n+1)]
threads = []

for i in range(4):
    th = threading.Thread(target = thread_main,
                          args = li[
                              offset * i + 1 :
                              offset *(i+1) + 1])
    threads.append(th)

for th in threads:
    th.start()

for th in threads:
    th.join()

print("the sum of {} is {}".format(n, g_result))

    
