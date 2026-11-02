import threading
import time

counter = 0
lock = threading.Lock()

def worker():
    global counter
    for _ in range(10000):
        with lock:               # вся цепочка чтение-запись под замком
            tmp = counter
            time.sleep(0)
            counter = tmp + 1

threads = [threading.Thread(target=worker) for _ in range(4)]
for t in threads:
    t.start()
for t in threads:
    t.join()
assert counter == 40000, counter
print(f"counter = {counter} (ожидалось 40000) OK")
