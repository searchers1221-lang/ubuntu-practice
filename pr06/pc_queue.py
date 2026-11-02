import queue
import threading
import time

q = queue.Queue(maxsize=3)

def producer():
    for i in range(8):
        q.put(i)                 # если очередь полна, поток ждёт здесь
        print(f"производитель положил {i}, в очереди {q.qsize()}", flush=True)
    q.put(None)                  # сигнал конца

def consumer():
    while True:
        item = q.get()
        if item is None:
            break
        time.sleep(0.2)          # потребитель медленнее
        print(f"  потребитель взял {item}", flush=True)

p = threading.Thread(target=producer)
c = threading.Thread(target=consumer)
p.start(); c.start()
p.join(); c.join()
