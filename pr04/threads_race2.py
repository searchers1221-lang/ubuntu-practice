import threading
import time

counter = 0

def worker(i):
    global counter
    for _ in range(50_000):
        tmp = counter        # 1. читаем
        time.sleep(0)        # 2. отдаём процессор другому потоку
        counter = tmp + 1    # 3. записываем (значение могло устареть)

threads = [threading.Thread(target=worker, args=(i,)) for i in range(4)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print("counter =", counter, "(ожидалось 200000)")
