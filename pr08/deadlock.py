import faulthandler
import threading
import time

# Через 3 секунды печатает, где стоит каждый поток, и завершает программу.
# Без этой строки программа зависла бы навсегда (остановить: Ctrl+C).
faulthandler.dump_traceback_later(3, exit=True)

lock_a = threading.Lock()
lock_b = threading.Lock()

def thread1():
    with lock_a:
        print("T1 взял A", flush=True)
        time.sleep(0.5)
        with lock_b:                 # ждёт B, который держит T2
            print("T1 взял B", flush=True)

def thread2():
    with lock_b:
        print("T2 взял B", flush=True)
        time.sleep(0.5)
        with lock_a:                 # ждёт A, который держит T1
            print("T2 взял A", flush=True)

t1 = threading.Thread(target=thread1, name="T1")
t2 = threading.Thread(target=thread2, name="T2")
t1.start(); t2.start()
t1.join(); t2.join()
print("Готово (до сюда программа не дойдёт)")
