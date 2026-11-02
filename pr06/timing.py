import threading
import time

N = 50000

def run(use_lock):
    counter = 0
    lock = threading.Lock()
    def worker():
        nonlocal counter
        for _ in range(N):
            if use_lock:
                with lock:
                    counter += 1
            else:
                counter += 1
    threads = [threading.Thread(target=worker) for _ in range(4)]
    start = time.perf_counter()
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    return time.perf_counter() - start, counter

for use_lock in (False, True):
    times = [run(use_lock)[0] for _ in range(3)]
    times.sort()
    name = "с блокировкой" if use_lock else "без блокировки"
    print(f"{name}: медиана {times[1]:.4f} с (3 запуска)")
