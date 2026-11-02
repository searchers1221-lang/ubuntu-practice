import threading
import time

lock_a = threading.Lock()
lock_b = threading.Lock()

# Правило: ВСЕГДА сначала A, потом B - в любом потоке.
def thread1():
    with lock_a:
        print("T1 взял A", flush=True)
        time.sleep(0.5)
        with lock_b:
            print("T1 взял B", flush=True)

def thread2():
    with lock_a:
        print("T2 взял A", flush=True)
        time.sleep(0.5)
        with lock_b:
            print("T2 взял B", flush=True)

t1 = threading.Thread(target=thread1, name="T1")
t2 = threading.Thread(target=thread2, name="T2")
t1.start(); t2.start()
t1.join(); t2.join()
print("Готово: взаимоблокировки нет")
