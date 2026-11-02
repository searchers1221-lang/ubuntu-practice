import sys
import threading
import time

USE_LOCK = len(sys.argv) > 1 and sys.argv[1] == "lock"
accounts = [1000, 1000, 1000]
TOTAL = sum(accounts)
lock = threading.Lock()

def transfer(src, dst, amount):
    a = accounts[src]
    time.sleep(0)
    accounts[src] = a - amount
    b = accounts[dst]
    time.sleep(0)
    accounts[dst] = b + amount

def worker(src, dst):
    for _ in range(5000):
        if USE_LOCK:
            with lock:           # перевод целиком - одна критическая секция
                transfer(src, dst, 1)
        else:
            transfer(src, dst, 1)

t1 = threading.Thread(target=worker, args=(0, 1))
t2 = threading.Thread(target=worker, args=(1, 0))
t1.start(); t2.start()
t1.join(); t2.join()
print("режим:", "с блокировкой" if USE_LOCK else "без блокировки")
print("счета:", accounts, "сумма:", sum(accounts), "(должна быть", TOTAL, ")")
assert sum(accounts) == TOTAL, "сумма изменилась!"
print("assert пройден")
