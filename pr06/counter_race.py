import threading
import time

counter = 0

def worker():
    global counter
    for _ in range(10000):
        tmp = counter        # читаем
        time.sleep(0)        # уступаем процессор другому потоку
        counter = tmp + 1    # пишем (значение могло устареть)

threads = [threading.Thread(target=worker) for _ in range(4)]
for t in threads:
    t.start()
for t in threads:
    t.join()
print(f"counter = {counter} (ожидалось 40000)")
