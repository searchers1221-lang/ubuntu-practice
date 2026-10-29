import sys
import threading

# Переключаем потоки очень часто, чтобы гонка проявилась
sys.setswitchinterval(1e-6)

counter = 0

def worker(i):
    global counter
    for _ in range(1_000_000):
        counter += 1   # чтение, прибавление и запись: не атомарно

threads = [threading.Thread(target=worker, args=(i,)) for i in range(4)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print("counter =", counter, "(ожидалось 4000000)")
