import threading

def thread_main(*args):
    li, n = args
    for i in range(offset * n + 1, offset *(n + 1) + 1):
        li[i] *= 2

n = 100
offset = n // 4

li = [i for i in range(n+1)]
threads = []

for i in range(4):
    th = threading.Thread(target = thread_main,
                          args = (li, i))
    threads.append(th)

for th in threads:
    th.start()

for th in threads:
    th.join()

print(li)

    
