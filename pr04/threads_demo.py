import threading

counter = 0

def worker(i):
    global counter
    for _ in range(100_000):
        counter += 1   # не атомарная операция: читаем, прибавляем, записываем

threads = []
for i in range(4):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()          # запускаем все потоки, и только потом ждём

for t in threads:
    t.join()           # ждём завершения всех

print("counter =", counter)
